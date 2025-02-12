package com.langportal.controller;

import com.langportal.model.StudyActivity;
import com.langportal.service.StudyActivityService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/study-activities")
@RequiredArgsConstructor
@Tag(name = "Study Activities", description = "Study activity management APIs")
public class StudyActivityController {
    private final StudyActivityService studyActivityService;

    @GetMapping
    @Operation(summary = "Get all study activities")
    public ResponseEntity<List<StudyActivity>> getAllStudyActivities() {
        return ResponseEntity.ok(studyActivityService.getAllStudyActivities());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get study activity by ID")
    public ResponseEntity<StudyActivity> getStudyActivityById(@PathVariable Long id) {
        return ResponseEntity.ok(studyActivityService.getStudyActivityById(id));
    }

    @PostMapping
    @Operation(summary = "Create new study activity")
    public ResponseEntity<StudyActivity> createStudyActivity(@RequestBody StudyActivity activity) {
        return ResponseEntity.ok(studyActivityService.createStudyActivity(activity));
    }

    @PutMapping("/{id}")
    @Operation(summary = "Update existing study activity")
    public ResponseEntity<StudyActivity> updateStudyActivity(@PathVariable Long id, @RequestBody StudyActivity activity) {
        return ResponseEntity.ok(studyActivityService.updateStudyActivity(id, activity));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Delete study activity")
    public ResponseEntity<Void> deleteStudyActivity(@PathVariable Long id) {
        studyActivityService.deleteStudyActivity(id);
        return ResponseEntity.ok().build();
    }
}
