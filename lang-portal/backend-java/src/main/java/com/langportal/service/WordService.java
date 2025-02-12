package com.langportal.service;

import com.langportal.model.Word;
import com.langportal.repository.WordRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
public class WordService {
    private final WordRepository wordRepository;

    public List<Word> getAllWords() {
        return wordRepository.findAll();
    }

    public Word getWordById(Long id) {
        return wordRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Word not found with id: " + id));
    }

    public List<Word> searchWords(String query) {
        List<Word> results = wordRepository.findByKanjiContainingIgnoreCase(query);
        if (results.isEmpty()) {
            results = wordRepository.findByRomajiContainingIgnoreCase(query);
        }
        if (results.isEmpty()) {
            results = wordRepository.findByEnglishContainingIgnoreCase(query);
        }
        return results;
    }

    @Transactional
    public Word createWord(Word word) {
        return wordRepository.save(word);
    }

    @Transactional
    public Word updateWord(Long id, Word word) {
        Word existingWord = getWordById(id);
        existingWord.setKanji(word.getKanji());
        existingWord.setRomaji(word.getRomaji());
        existingWord.setEnglish(word.getEnglish());
        existingWord.setParts(word.getParts());
        return wordRepository.save(existingWord);
    }

    @Transactional
    public void deleteWord(Long id) {
        wordRepository.deleteById(id);
    }

    public List<Word> getWordsByGroupId(Long groupId) {
        return wordRepository.findByGroupId(groupId);
    }
}
