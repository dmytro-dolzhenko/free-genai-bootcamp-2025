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

    @ManyToOne
    @JoinColumn(name = "word_id", nullable = false)
    private Word word;

    @Column(name = "correct_count")
    private Integer correctCount = 0;

    @Column(name = "wrong_count")
    private Integer wrongCount = 0;

    @Column(name = "last_reviewed")
    private LocalDateTime lastReviewed;

    @PrePersist
    @PreUpdate
    protected void onUpdate() {
        lastReviewed = LocalDateTime.now();
    }
}
