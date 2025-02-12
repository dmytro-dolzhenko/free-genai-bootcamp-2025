package com.langportal.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.langportal.model.StudyActivity;
import com.langportal.service.StudyActivityService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.util.Arrays;
import java.util.List;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(StudyActivityController.class)
@AutoConfigureMockMvc(addFilters = false)
public class StudyActivityControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private StudyActivityService studyActivityService;

    @Test
    public void testGetAllStudyActivities() throws Exception {
        StudyActivity activity1 = new StudyActivity();
        activity1.setId(1L);
        activity1.setName("Flashcards");

        StudyActivity activity2 = new StudyActivity();
        activity2.setId(2L);
        activity2.setName("Quiz");

        List<StudyActivity> activities = Arrays.asList(activity1, activity2);

        when(studyActivityService.getAllStudyActivities()).thenReturn(activities);

        mockMvc.perform(get("/api/study-activities")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$[0].id").value(1))
                .andExpect(jsonPath("$[0].name").value("Flashcards"))
                .andExpect(jsonPath("$[1].id").value(2))
                .andExpect(jsonPath("$[1].name").value("Quiz"));
    }

    @Test
    public void testGetStudyActivityById() throws Exception {
        StudyActivity activity = new StudyActivity();
        activity.setId(1L);
        activity.setName("Flashcards");

        when(studyActivityService.getStudyActivityById(1L)).thenReturn(activity);

        mockMvc.perform(get("/api/study-activities/1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("Flashcards"));
    }

    @Test
    public void testCreateStudyActivity() throws Exception {
        StudyActivity newActivity = new StudyActivity();
        newActivity.setName("Flashcards");

        StudyActivity savedActivity = new StudyActivity();
        savedActivity.setId(1L);
        savedActivity.setName("Flashcards");

        when(studyActivityService.createStudyActivity(any(StudyActivity.class))).thenReturn(savedActivity);

        mockMvc.perform(post("/api/study-activities")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(newActivity)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("Flashcards"));
    }

    @Test
    public void testUpdateStudyActivity() throws Exception {
        StudyActivity updatedActivity = new StudyActivity();
        updatedActivity.setId(1L);
        updatedActivity.setName("Updated Flashcards");

        when(studyActivityService.updateStudyActivity(any(Long.class), any(StudyActivity.class)))
                .thenReturn(updatedActivity);

        mockMvc.perform(put("/api/study-activities/1")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(updatedActivity)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("Updated Flashcards"));
    }

    @Test
    public void testDeleteStudyActivity() throws Exception {
        mockMvc.perform(delete("/api/study-activities/1"))
                .andExpect(status().isOk());
    }
} 