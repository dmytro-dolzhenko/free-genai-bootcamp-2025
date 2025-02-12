package com.langportal.service;

import com.langportal.model.StudySession;
import com.langportal.model.Word;
import com.langportal.model.WordReview;
import com.langportal.model.WordReviewItem;
import com.langportal.repository.WordRepository;
import com.langportal.repository.WordReviewItemRepository;
import com.langportal.repository.WordReviewRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
public class WordReviewService {
    private final WordReviewRepository wordReviewRepository;
    private final WordReviewItemRepository wordReviewItemRepository;
    private final WordRepository wordRepository;

    public WordReview getWordReviewByWordId(Long wordId) {
        return wordReviewRepository.findByWordId(wordId)
            .orElseGet(() -> {
                Word word = wordRepository.findById(wordId)
                    .orElseThrow(() -> new RuntimeException("Word not found with id: " + wordId));
                WordReview review = new WordReview();
                review.setWord(word);
                return wordReviewRepository.save(review);
            });
    }

    @Transactional
    public WordReviewItem recordReview(Long wordId, Long sessionId, boolean correct) {
        Word word = wordRepository.findById(wordId)
            .orElseThrow(() -> new RuntimeException("Word not found with id: " + wordId));

        // Update word review statistics
        WordReview review = getWordReviewByWordId(wordId);
        if (correct) {
            review.setCorrectCount(review.getCorrectCount() + 1);
        } else {
            review.setWrongCount(review.getWrongCount() + 1);
        }
        wordReviewRepository.save(review);

        // Create review item
        WordReviewItem item = new WordReviewItem();
        item.setWord(word);
        item.setCorrect(correct);
        
        StudySession session = new StudySession();
        session.setId(sessionId);
        item.setStudySession(session);

        return wordReviewItemRepository.save(item);
    }

    public List<WordReviewItem> getReviewsByWordId(Long wordId) {
        return wordReviewItemRepository.findByWordId(wordId);
    }

    public Page<WordReviewItem> getReviewsByWordIdPaginated(Long wordId, Pageable pageable) {
        return wordReviewItemRepository.findByWordIdOrderByCreatedAtDesc(wordId, pageable);
    }

    public List<WordReviewItem> getReviewsBySessionId(Long sessionId) {
        return wordReviewItemRepository.findByStudySessionId(sessionId);
    }
}
