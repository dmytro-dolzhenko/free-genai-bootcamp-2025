package com.langportal.controller;

import com.langportal.model.StudySession;
import com.langportal.service.StudySessionService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/study-sessions")
@RequiredArgsConstructor
@Tag(name = "Study Sessions", description = "Study session management APIs")
public class StudySessionController {
    private final StudySessionService studySessionService;

    @PostMapping
    @Operation(summary = "Create new study session")
    public ResponseEntity<StudySession> createStudySession(
            @RequestParam Long groupId,
            @RequestParam Long studyActivityId) {
        return ResponseEntity.ok(studySessionService.createStudySession(groupId, studyActivityId));
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get study session by ID")
    public ResponseEntity<StudySession> getStudySessionById(@PathVariable Long id) {
        return ResponseEntity.ok(studySessionService.getStudySessionById(id));
    }

    @GetMapping("/group/{groupId}")
    @Operation(summary = "Get study sessions by group ID")
    public ResponseEntity<List<StudySession>> getStudySessionsByGroupId(@PathVariable Long groupId) {
        return ResponseEntity.ok(studySessionService.getStudySessionsByGroupId(groupId));
    }

    @GetMapping("/activity/{activityId}")
    @Operation(summary = "Get study sessions by activity ID")
    public ResponseEntity<Page<StudySession>> getStudySessionsByActivityId(
            @PathVariable Long activityId,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(studySessionService.getStudySessionsByActivityId(activityId, PageRequest.of(page, size)));
    }

    @PutMapping("/{id}/complete")
    @Operation(summary = "Complete study session")
    public ResponseEntity<StudySession> completeStudySession(
            @PathVariable Long id,
            @RequestBody Map<String, Integer> results) {
        return ResponseEntity.ok(studySessionService.completeStudySession(
            id,
            results.get("correctCount"),
            results.get("totalCount")
        ));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Delete study session")
    public ResponseEntity<Void> deleteStudySession(@PathVariable Long id) {
        studySessionService.deleteStudySession(id);
        return ResponseEntity.ok().build();
    }
}
