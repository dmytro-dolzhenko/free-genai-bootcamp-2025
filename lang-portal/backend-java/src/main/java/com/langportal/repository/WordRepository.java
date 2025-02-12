package com.langportal.repository;

import com.langportal.model.Word;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface WordRepository extends JpaRepository<Word, Long> {
    List<Word> findByKanjiContainingIgnoreCase(String kanji);
    List<Word> findByRomajiContainingIgnoreCase(String romaji);
    List<Word> findByEnglishContainingIgnoreCase(String english);
    
    @Query("SELECT w FROM Word w JOIN w.groups g WHERE g.id = :groupId")
    List<Word> findByGroupId(Long groupId);
}
