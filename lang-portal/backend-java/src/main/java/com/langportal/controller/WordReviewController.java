package com.langportal.controller;

import com.langportal.model.WordReview;
import com.langportal.model.WordReviewItem;
import com.langportal.service.WordReviewService;
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
@RequestMapping("/api/word-reviews")
@RequiredArgsConstructor
@Tag(name = "Word Reviews", description = "Word review management APIs")
public class WordReviewController {
    private final WordReviewService wordReviewService;

    @GetMapping("/word/{wordId}")
    @Operation(summary = "Get word review statistics")
    public ResponseEntity<WordReview> getWordReview(@PathVariable Long wordId) {
        return ResponseEntity.ok(wordReviewService.getWordReviewByWordId(wordId));
    }

    @PostMapping("/word/{wordId}/session/{sessionId}")
    @Operation(summary = "Record a word review")
    public ResponseEntity<WordReviewItem> recordReview(
            @PathVariable Long wordId,
            @PathVariable Long sessionId,
            @RequestBody Map<String, Boolean> request) {
        return ResponseEntity.ok(wordReviewService.recordReview(wordId, sessionId, request.get("correct")));
    }

    @GetMapping("/word/{wordId}/history")
    @Operation(summary = "Get word review history")
    public ResponseEntity<Page<WordReviewItem>> getWordReviewHistory(
            @PathVariable Long wordId,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(wordReviewService.getReviewsByWordIdPaginated(wordId, PageRequest.of(page, size)));
    }

    @GetMapping("/session/{sessionId}")
    @Operation(summary = "Get reviews by session")
    public ResponseEntity<List<WordReviewItem>> getSessionReviews(@PathVariable Long sessionId) {
        return ResponseEntity.ok(wordReviewService.getReviewsBySessionId(sessionId));
    }
}
