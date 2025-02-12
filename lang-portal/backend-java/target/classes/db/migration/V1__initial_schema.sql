-- Groups table
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    words_count INTEGER DEFAULT 0
);

-- Words table
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji TEXT,
    romaji TEXT NOT NULL,
    english TEXT NOT NULL,
    parts TEXT,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

-- Word Reviews table
CREATE TABLE IF NOT EXISTS word_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    correct_count INTEGER DEFAULT 0,
    wrong_count INTEGER DEFAULT 0,
    last_reviewed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (word_id) REFERENCES words(id)
);

-- Study Activities table
CREATE TABLE IF NOT EXISTS study_activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    preview_url TEXT
);

-- Study Sessions table
CREATE TABLE IF NOT EXISTS study_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER NOT NULL,
    study_activity_id INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    correct_count INTEGER,
    total_count INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE,
    FOREIGN KEY (study_activity_id) REFERENCES study_activities(id) ON DELETE CASCADE
);

-- Word Review Items table
CREATE TABLE IF NOT EXISTS word_review_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    study_session_id INTEGER NOT NULL,
    correct BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (word_id) REFERENCES words(id) ON DELETE CASCADE,
    FOREIGN KEY (study_session_id) REFERENCES study_sessions(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS word_groups (
  word_id INTEGER NOT NULL,
  group_id INTEGER NOT NULL,
  FOREIGN KEY (word_id) REFERENCES words(id),
  FOREIGN KEY (group_id) REFERENCES groups(id)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_words_kanji ON words (kanji);
CREATE INDEX IF NOT EXISTS idx_words_romaji ON words (romaji);
CREATE INDEX IF NOT EXISTS idx_words_english ON words (english);
CREATE INDEX IF NOT EXISTS idx_groups_name ON groups (name);
CREATE INDEX IF NOT EXISTS idx_study_sessions_group ON study_sessions (group_id);
CREATE INDEX IF NOT EXISTS idx_study_sessions_activity ON study_sessions (study_activity_id);
CREATE INDEX IF NOT EXISTS idx_word_reviews_word ON word_reviews (word_id);
CREATE INDEX IF NOT EXISTS idx_word_review_items_word ON word_review_items (word_id);
CREATE INDEX IF NOT EXISTS idx_word_review_items_session ON word_review_items (study_session_id);

-- Insert initial study activities
INSERT INTO study_activities (name, url, preview_url) VALUES 
('Typing Tutor', 'http://localhost:8080', '/assets/study_activities/typing_tutor.png');