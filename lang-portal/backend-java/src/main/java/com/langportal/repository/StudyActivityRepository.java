package com.langportal.repository;

import com.langportal.model.StudyActivity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface StudyActivityRepository extends JpaRepository<StudyActivity, Long> {
}
