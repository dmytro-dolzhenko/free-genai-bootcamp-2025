package com.langportal.service;

import com.langportal.model.Word;
import com.langportal.model.WordReview;
import com.langportal.model.WordReviewItem;
import com.langportal.model.StudySession;
import com.langportal.repository.WordReviewItemRepository;
import com.langportal.repository.WordReviewRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
public class WordReviewService {
    private final WordReviewRepository wordReviewRepository;
    private final WordReviewItemRepository wordReviewItemRepository;
    private final WordService wordService;
    private final StudySessionService studySessionService;

    public WordReview getWordReviewByWordId(Long wordId) {
        return wordReviewRepository.findByWordId(wordId)
                .orElseGet(() -> {
                    Word word = wordService.getWordById(wordId);
                    WordReview review = new WordReview();
                    review.setWordId(word.getId());
                    review.setCorrectCount(0);
                    review.setTotalCount(0);
                    return wordReviewRepository.save(review);
                });
    }

    @Transactional
    public WordReviewItem recordReview(Long wordId, Long sessionId, boolean correct) {
        Word word = wordService.getWordById(wordId);
        StudySession session = studySessionService.getStudySessionById(sessionId);

        WordReview review = getWordReviewByWordId(wordId);
        review.setCorrectCount(review.getCorrectCount() + (correct ? 1 : 0));
        review.setTotalCount(review.getTotalCount() + 1);
        wordReviewRepository.save(review);

        WordReviewItem item = new WordReviewItem();
        item.setWordId(wordId);
        item.setSessionId(sessionId);
        item.setCorrect(correct);
        item.setReviewedAt(LocalDateTime.now());
        return wordReviewItemRepository.save(item);
    }

    public Page<WordReviewItem> getReviewsByWordIdPaginated(Long wordId, Pageable pageable) {
        return wordReviewItemRepository.findByWordIdOrderByReviewedAtDesc(wordId, pageable);
    }

    public List<WordReviewItem> getReviewsBySessionId(Long sessionId) {
        return wordReviewItemRepository.findBySessionIdOrderByReviewedAtDesc(sessionId);
    }
}
