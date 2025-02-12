package com.langportal.repository;

import com.langportal.model.WordReview;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface WordReviewRepository extends JpaRepository<WordReview, Long> {
    Optional<WordReview> findByWordId(Long wordId);
}
