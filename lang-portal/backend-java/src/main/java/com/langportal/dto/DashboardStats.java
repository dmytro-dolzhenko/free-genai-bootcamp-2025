package com.langportal.dto;

import lombok.Data;

@Data
public class DashboardStats {
    private Integer totalWords;
    private Integer totalGroups;
    private Integer totalSessions;
    private Integer wordsReviewed;
    private Double correctRate;
    private Integer sessionsLast7Days;
    private Integer wordsReviewedLast7Days;
}
