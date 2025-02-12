package com.langportal.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.langportal.dto.DashboardStats;
import com.langportal.dto.RecentSession;
import com.langportal.service.DashboardService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(DashboardController.class)
@AutoConfigureMockMvc(addFilters = false)
public class DashboardControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private DashboardService dashboardService;

    @Test
    public void testGetRecentSession() throws Exception {
        RecentSession recentSession = new RecentSession();
        // Set properties based on your DTO structure
        
        when(dashboardService.getRecentSession()).thenReturn(recentSession);

        mockMvc.perform(get("/api/dashboard/recent-session")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON));
    }

    @Test
    public void testGetStats() throws Exception {
        DashboardStats stats = new DashboardStats();
        // Set properties based on your DTO structure

        when(dashboardService.getStats()).thenReturn(stats);

        mockMvc.perform(get("/api/dashboard/stats")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON));
    }
} 