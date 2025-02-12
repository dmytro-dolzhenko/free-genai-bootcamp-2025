package com.langportal.controller;

import com.langportal.dto.DashboardStats;
import com.langportal.dto.RecentSession;
import com.langportal.service.DashboardService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/dashboard")
@RequiredArgsConstructor
@Tag(name = "Dashboard", description = "Dashboard statistics APIs")
public class DashboardController {
    private final DashboardService dashboardService;

    @GetMapping("/recent-session")
    @Operation(summary = "Get most recent study session")
    public ResponseEntity<RecentSession> getRecentSession() {
        RecentSession session = dashboardService.getRecentSession();
        return session != null ? ResponseEntity.ok(session) : ResponseEntity.noContent().build();
    }

    @GetMapping("/stats")
    @Operation(summary = "Get dashboard statistics")
    public ResponseEntity<DashboardStats> getStats() {
        return ResponseEntity.ok(dashboardService.getStats());
    }
}
