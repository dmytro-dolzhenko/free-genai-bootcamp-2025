package com.langportal.model;

import jakarta.persistence.*;
import lombok.Data;
import org.hibernate.annotations.Type;

import java.util.List;

@Data
@Entity
@Table(name = "words")
public class Word {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String kanji;

    @Column(nullable = false)
    private String romaji;

    @Column(nullable = false)
    private String english;

    @Column(nullable = false, columnDefinition = "jsonb")
    private String parts;  // Stored as JSON string

    @ManyToMany(mappedBy = "words")
    private List<Group> groups;
}
