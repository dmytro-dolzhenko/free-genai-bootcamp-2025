-- Insert study activities
INSERT INTO study_activities (name, url, preview_url) VALUES
('Flashcards', '/study/flashcards', '/images/flashcards.png'),
('Quiz', '/study/quiz', '/images/quiz.png'),
('Writing Practice', '/study/writing', '/images/writing.png');

-- Insert groups
INSERT INTO groups (name) VALUES ('Verbs');
INSERT INTO groups (name) VALUES ('Nouns');
INSERT INTO groups (name) VALUES ('Adjectives');
INSERT INTO groups (name) VALUES ('Adverbs');

-- Insert verbs
INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '払う', 'harau', 'to pay', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '習う', 'narau', 'to learn', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '開ける', 'akeru', 'to open', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '歩く', 'aruku', 'to walk', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '遊ぶ', 'asobu', 'to play', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '待つ', 'matsu', 'to wait', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '飲む', 'nomu', 'to drink', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '食べる', 'taberu', 'to eat', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '寝る', 'neru', 'to sleep', id FROM groups WHERE name = 'Verbs';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '起きる', 'okiru', 'to wake up', id FROM groups WHERE name = 'Verbs';

-- Insert nouns
INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '本', 'hon', 'book', id FROM groups WHERE name = 'Nouns';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '猫', 'neko', 'cat', id FROM groups WHERE name = 'Nouns';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '犬', 'inu', 'dog', id FROM groups WHERE name = 'Nouns';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '車', 'kuruma', 'car', id FROM groups WHERE name = 'Nouns';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '家', 'ie', 'house', id FROM groups WHERE name = 'Nouns';

-- Insert adjectives
INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '大きい', 'ookii', 'big', id FROM groups WHERE name = 'Adjectives';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '小さい', 'chiisai', 'small', id FROM groups WHERE name = 'Adjectives';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '新しい', 'atarashii', 'new', id FROM groups WHERE name = 'Adjectives';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '古い', 'furui', 'old', id FROM groups WHERE name = 'Adjectives';

INSERT INTO words (kanji, romaji, english, group_id) 
SELECT '良い', 'yoi', 'good', id FROM groups WHERE name = 'Adjectives';
