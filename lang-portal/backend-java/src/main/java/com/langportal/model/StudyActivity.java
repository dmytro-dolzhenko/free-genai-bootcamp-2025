package com.langportal.model;

import jakarta.persistence.*;
import lombok.Data;

import java.util.List;

@Data
@Entity
@Table(name = "study_activities")
public class StudyActivity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String url;

    @Column(name = "preview_url")
    private String previewUrl;

    @OneToMany(mappedBy = "studyActivity")
    private List<StudySession> studySessions;
}
