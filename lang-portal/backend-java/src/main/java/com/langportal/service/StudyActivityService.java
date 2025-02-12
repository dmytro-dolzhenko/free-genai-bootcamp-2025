package com.langportal.service;

import com.langportal.model.StudyActivity;
import com.langportal.repository.StudyActivityRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
public class StudyActivityService {
    private final StudyActivityRepository studyActivityRepository;

    public List<StudyActivity> getAllStudyActivities() {
        return studyActivityRepository.findAll();
    }

    public StudyActivity getStudyActivityById(Long id) {
        return studyActivityRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Study activity not found with id: " + id));
    }

    @Transactional
    public StudyActivity createStudyActivity(StudyActivity activity) {
        return studyActivityRepository.save(activity);
    }

    @Transactional
    public StudyActivity updateStudyActivity(Long id, StudyActivity activity) {
        StudyActivity existingActivity = getStudyActivityById(id);
        existingActivity.setName(activity.getName());
        existingActivity.setUrl(activity.getUrl());
        existingActivity.setPreviewUrl(activity.getPreviewUrl());
        return studyActivityRepository.save(existingActivity);
    }

    @Transactional
    public void deleteStudyActivity(Long id) {
        studyActivityRepository.deleteById(id);
    }
}
