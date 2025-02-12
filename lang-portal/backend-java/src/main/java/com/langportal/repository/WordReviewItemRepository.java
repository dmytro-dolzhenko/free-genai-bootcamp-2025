package com.langportal.repository;

import com.langportal.model.WordReviewItem;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface WordReviewItemRepository extends JpaRepository<WordReviewItem, Long> {
    List<WordReviewItem> findByWordId(Long wordId);
    Page<WordReviewItem> findByWordIdOrderByReviewedAtDesc(Long wordId, Pageable pageable);
    List<WordReviewItem> findBySessionIdOrderByReviewedAtDesc(Long sessionId);
}
