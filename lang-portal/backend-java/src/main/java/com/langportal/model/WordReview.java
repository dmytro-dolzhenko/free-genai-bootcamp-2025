package com.langportal.model;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "word_reviews")
public class WordReview {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "word_id", nullable = false)
    private Long wordId;

    @Column(name = "correct_count")
    private Integer correctCount;

    @Column(name = "total_count")
    private Integer totalCount;

    @Column(name = "last_reviewed")
    private LocalDateTime lastReviewed;

    @PrePersist
    @PreUpdate
    protected void onUpdate() {
        lastReviewed = LocalDateTime.now();
    }
}
