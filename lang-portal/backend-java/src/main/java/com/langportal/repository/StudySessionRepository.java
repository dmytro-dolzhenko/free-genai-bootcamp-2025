package com.langportal.repository;

import com.langportal.model.StudySession;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface StudySessionRepository extends JpaRepository<StudySession, Long> {
    Page<StudySession> findByStudyActivityId(Long studyActivityId, Pageable pageable);
    List<StudySession> findByGroupId(Long groupId);
}
