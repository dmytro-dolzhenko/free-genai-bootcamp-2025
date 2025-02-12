package com.langportal.service;

import com.langportal.dto.DashboardStats;
import com.langportal.dto.RecentSession;
import com.langportal.repository.*;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import jakarta.persistence.EntityManager;
import jakarta.persistence.Query;
import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
public class DashboardService {
    private final EntityManager entityManager;
    private final WordRepository wordRepository;
    private final GroupRepository groupRepository;
    private final StudySessionRepository studySessionRepository;
    private final WordReviewItemRepository wordReviewItemRepository;

    public RecentSession getRecentSession() {
        String sql = """
            SELECT 
                ss.id,
                ss.group_id,
                sa.name as activity_name,
                ss.created_at,
                COUNT(CASE WHEN wri.correct = true THEN 1 END) as correct_count,
                COUNT(CASE WHEN wri.correct = false THEN 1 END) as wrong_count
            FROM study_sessions ss
            JOIN study_activities sa ON ss.study_activity_id = sa.id
            LEFT JOIN word_review_items wri ON ss.id = wri.study_session_id
            GROUP BY ss.id, ss.group_id, sa.name, ss.created_at
            ORDER BY ss.created_at DESC
            LIMIT 1
        """;

        Query query = entityManager.createNativeQuery(sql);
        List<?> result = query.getResultList();

        if (result.isEmpty()) {
            return null;
        }

        Object[] row = (Object[]) result.get(0);
        RecentSession session = new RecentSession();
        session.setId(((Number) row[0]).longValue());
        session.setGroupId(((Number) row[1]).longValue());
        session.setActivityName((String) row[2]);
        session.setCreatedAt((LocalDateTime) row[3]);
        session.setCorrectCount(row[4] != null ? ((Number) row[4]).intValue() : 0);
        session.setWrongCount(row[5] != null ? ((Number) row[5]).intValue() : 0);

        return session;
    }

    public DashboardStats getStats() {
        LocalDateTime sevenDaysAgo = LocalDateTime.now().minusDays(7);

        DashboardStats stats = new DashboardStats();
        stats.setTotalWords((int) wordRepository.count());
        stats.setTotalGroups((int) groupRepository.count());
        stats.setTotalSessions((int) studySessionRepository.count());

        // Calculate total words reviewed and correct rate
        String reviewStats = """
            SELECT 
                COUNT(*) as total_reviews,
                COUNT(CASE WHEN correct = true THEN 1 END) as correct_count
            FROM word_review_items
        """;
        Query reviewQuery = entityManager.createNativeQuery(reviewStats);
        Object[] reviewResult = (Object[]) reviewQuery.getSingleResult();
        
        stats.setWordsReviewed(((Number) reviewResult[0]).intValue());
        long correctCount = ((Number) reviewResult[1]).longValue();
        stats.setCorrectRate(stats.getWordsReviewed() > 0 
            ? (double) correctCount / stats.getWordsReviewed() * 100 
            : 0.0);

        // Calculate last 7 days stats
        String recentStats = """
            SELECT 
                COUNT(DISTINCT ss.id) as sessions,
                COUNT(DISTINCT wri.id) as reviews
            FROM study_sessions ss
            LEFT JOIN word_review_items wri ON ss.id = wri.study_session_id
            WHERE ss.created_at >= :sevenDaysAgo
        """;
        Query recentQuery = entityManager.createNativeQuery(recentStats)
            .setParameter("sevenDaysAgo", sevenDaysAgo);
        Object[] recentResult = (Object[]) recentQuery.getSingleResult();

        stats.setSessionsLast7Days(((Number) recentResult[0]).intValue());
        stats.setWordsReviewedLast7Days(((Number) recentResult[1]).intValue());

        return stats;
    }
}
