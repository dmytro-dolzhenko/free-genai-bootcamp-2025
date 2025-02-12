package com.langportal.model;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "word_review_items")
public class WordReviewItem {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "word_id", nullable = false)
    private Long wordId;

    @Column(name = "session_id", nullable = false)
    private Long sessionId;

    @Column(nullable = false)
    private Boolean correct;

    @Column(name = "reviewed_at", nullable = false)
    private LocalDateTime reviewedAt;
}
