package com.langportal.dto;

import lombok.Data;

import java.time.LocalDateTime;

@Data
public class RecentSession {
    private Long id;
    private Long groupId;
    private String activityName;
    private LocalDateTime createdAt;
    private Integer correctCount;
    private Integer wrongCount;
}
