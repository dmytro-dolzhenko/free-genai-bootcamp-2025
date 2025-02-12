package com.langportal.controller;

import com.langportal.model.Word;
import com.langportal.service.WordService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/words")
@RequiredArgsConstructor
@Tag(name = "Words", description = "Word management APIs")
public class WordController {
    private final WordService wordService;

    @GetMapping
    @Operation(summary = "Get all words")
    public ResponseEntity<List<Word>> getAllWords() {
        return ResponseEntity.ok(wordService.getAllWords());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get word by ID")
    public ResponseEntity<Word> getWordById(@PathVariable Long id) {
        return ResponseEntity.ok(wordService.getWordById(id));
    }

    @GetMapping("/search")
    @Operation(summary = "Search words")
    public ResponseEntity<List<Word>> searchWords(@RequestParam String query) {
        return ResponseEntity.ok(wordService.searchWords(query));
    }

    @PostMapping
    @Operation(summary = "Create new word")
    public ResponseEntity<Word> createWord(@RequestBody Word word) {
        return ResponseEntity.ok(wordService.createWord(word));
    }

    @PutMapping("/{id}")
    @Operation(summary = "Update existing word")
    public ResponseEntity<Word> updateWord(@PathVariable Long id, @RequestBody Word word) {
        return ResponseEntity.ok(wordService.updateWord(id, word));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Delete word")
    public ResponseEntity<Void> deleteWord(@PathVariable Long id) {
        wordService.deleteWord(id);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/group/{groupId}")
    @Operation(summary = "Get words by group ID")
    public ResponseEntity<List<Word>> getWordsByGroupId(@PathVariable Long groupId) {
        return ResponseEntity.ok(wordService.getWordsByGroupId(groupId));
    }
}
