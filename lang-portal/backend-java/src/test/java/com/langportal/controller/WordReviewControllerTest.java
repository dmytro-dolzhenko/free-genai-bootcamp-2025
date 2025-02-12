package com.langportal.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.langportal.model.WordReview;
import com.langportal.model.WordReviewItem;
import com.langportal.service.WordReviewService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(WordReviewController.class)
@AutoConfigureMockMvc(addFilters = false)
public class WordReviewControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private WordReviewService wordReviewService;

    @Test
    public void testGetWordReview() throws Exception {
        WordReview wordReview = new WordReview();
        wordReview.setId(1L);
        wordReview.setWordId(1L);
        wordReview.setCorrectCount(5);
        wordReview.setTotalCount(10);

        when(wordReviewService.getWordReviewByWordId(1L)).thenReturn(wordReview);

        mockMvc.perform(get("/api/word-reviews/word/1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.wordId").value(1))
                .andExpect(jsonPath("$.correctCount").value(5))
                .andExpect(jsonPath("$.totalCount").value(10));
    }

    @Test
    public void testRecordReview() throws Exception {
        WordReviewItem reviewItem = new WordReviewItem();
        reviewItem.setId(1L);
        reviewItem.setWordId(1L);
        reviewItem.setSessionId(1L);
        reviewItem.setCorrect(true);
        reviewItem.setReviewedAt(LocalDateTime.now());

        Map<String, Boolean> request = new HashMap<>();
        request.put("correct", true);

        when(wordReviewService.recordReview(eq(1L), eq(1L), eq(true))).thenReturn(reviewItem);

        mockMvc.perform(post("/api/word-reviews/word/1/session/1")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(request)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.wordId").value(1))
                .andExpect(jsonPath("$.sessionId").value(1))
                .andExpect(jsonPath("$.correct").value(true));
    }

    @Test
    public void testGetWordReviewHistory() throws Exception {
        WordReviewItem item = new WordReviewItem();
        item.setId(1L);
        item.setWordId(1L);
        item.setSessionId(1L);
        item.setCorrect(true);
        item.setReviewedAt(LocalDateTime.now());

        List<WordReviewItem> items = Arrays.asList(item);
        Page<WordReviewItem> page = new PageImpl<>(items, PageRequest.of(0, 10), 1);

        when(wordReviewService.getReviewsByWordIdPaginated(eq(1L), any(PageRequest.class))).thenReturn(page);

        mockMvc.perform(get("/api/word-reviews/word/1/history")
                .param("page", "0")
                .param("size", "10")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$.content[0].id").value(1))
                .andExpect(jsonPath("$.content[0].wordId").value(1))
                .andExpect(jsonPath("$.content[0].sessionId").value(1))
                .andExpect(jsonPath("$.content[0].correct").value(true));
    }

    @Test
    public void testGetSessionReviews() throws Exception {
        WordReviewItem item = new WordReviewItem();
        item.setId(1L);
        item.setWordId(1L);
        item.setSessionId(1L);
        item.setCorrect(true);
        item.setReviewedAt(LocalDateTime.now());

        List<WordReviewItem> items = Arrays.asList(item);

        when(wordReviewService.getReviewsBySessionId(1L)).thenReturn(items);

        mockMvc.perform(get("/api/word-reviews/session/1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$[0].id").value(1))
                .andExpect(jsonPath("$[0].wordId").value(1))
                .andExpect(jsonPath("$[0].sessionId").value(1))
                .andExpect(jsonPath("$[0].correct").value(true));
    }
} 