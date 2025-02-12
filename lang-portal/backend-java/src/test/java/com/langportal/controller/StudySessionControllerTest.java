package com.langportal.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.langportal.model.StudySession;
import com.langportal.service.StudySessionService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(StudySessionController.class)
@AutoConfigureMockMvc(addFilters = false)
public class StudySessionControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private StudySessionService studySessionService;

    @Test
    public void testGetStudySessionById() throws Exception {
        // Prepare test data
        StudySession session = new StudySession();
        session.setId(1L);
        // Set other necessary properties

        // Mock service method
        when(studySessionService.getStudySessionById(1L)).thenReturn(session);

        // Perform request and verify
        mockMvc.perform(get("/api/study-sessions/1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$.id").value(1));
    }

    @Test
    public void testCreateStudySession() throws Exception {
        StudySession session = new StudySession();
        session.setId(1L);
        // Set other necessary properties

        when(studySessionService.createStudySession(eq(1L), eq(1L))).thenReturn(session);

        mockMvc.perform(post("/api/study-sessions")
                .param("groupId", "1")
                .param("studyActivityId", "1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1));
    }

    @Test
    public void testCompleteStudySession() throws Exception {
        StudySession session = new StudySession();
        session.setId(1L);
        // Set other necessary properties

        Map<String, Integer> results = new HashMap<>();
        results.put("correctCount", 8);
        results.put("totalCount", 10);

        when(studySessionService.completeStudySession(eq(1L), eq(8), eq(10))).thenReturn(session);

        mockMvc.perform(put("/api/study-sessions/1/complete")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(results)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1));
    }
} 