package com.langportal.service;

import com.langportal.model.Group;
import com.langportal.model.StudyActivity;
import com.langportal.model.StudySession;
import com.langportal.repository.GroupRepository;
import com.langportal.repository.StudyActivityRepository;
import com.langportal.repository.StudySessionRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
public class StudySessionService {
    private final StudySessionRepository studySessionRepository;
    private final GroupRepository groupRepository;
    private final StudyActivityRepository studyActivityRepository;

    public StudySession getStudySessionById(Long id) {
        return studySessionRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Study session not found with id: " + id));
    }

    public Page<StudySession> getStudySessionsByActivityId(Long activityId, Pageable pageable) {
        return studySessionRepository.findByStudyActivityId(activityId, pageable);
    }

    public List<StudySession> getStudySessionsByGroupId(Long groupId) {
        return studySessionRepository.findByGroupId(groupId);
    }

    @Transactional
    public StudySession createStudySession(Long groupId, Long activityId) {
        Group group = groupRepository.findById(groupId)
            .orElseThrow(() -> new RuntimeException("Group not found with id: " + groupId));
        
        StudyActivity activity = studyActivityRepository.findById(activityId)
            .orElseThrow(() -> new RuntimeException("Study activity not found with id: " + activityId));

        StudySession session = new StudySession();
        session.setGroup(group);
        session.setStudyActivity(activity);
        return studySessionRepository.save(session);
    }

    @Transactional
    public StudySession completeStudySession(Long sessionId, Integer correctCount, Integer totalCount) {
        StudySession session = getStudySessionById(sessionId);
        session.setCompletedAt(LocalDateTime.now());
        session.setCorrectCount(correctCount);
        session.setTotalCount(totalCount);
        return studySessionRepository.save(session);
    }

    @Transactional
    public void deleteStudySession(Long id) {
        studySessionRepository.deleteById(id);
    }
}
