package com.langportal.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.langportal.model.Word;
import com.langportal.service.WordService;
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

@WebMvcTest(WordController.class)
@AutoConfigureMockMvc(addFilters = false)
public class WordControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private WordService wordService;

    @Test
    public void testGetAllWords() throws Exception {
        // Prepare test data
        Word word1 = new Word();
        word1.setId(1L);
        word1.setKanji("こんにちは");
        word1.setRomaji("konnichiwa");
        word1.setEnglish("hello");
        word1.setParts("{}");

        Word word2 = new Word();
        word2.setId(2L);
        word2.setKanji("さようなら");
        word2.setRomaji("sayounara");
        word2.setEnglish("goodbye");
        word2.setParts("{}");

        List<Word> words = Arrays.asList(word1, word2);

        // Mock service method
        when(wordService.getAllWords()).thenReturn(words);

        // Perform request and verify
        mockMvc.perform(get("/api/words")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$[0].id").value(1))
                .andExpect(jsonPath("$[0].kanji").value("こんにちは"))
                .andExpect(jsonPath("$[0].english").value("hello"))
                .andExpect(jsonPath("$[1].id").value(2))
                .andExpect(jsonPath("$[1].kanji").value("さようなら"))
                .andExpect(jsonPath("$[1].english").value("goodbye"));
    }

    @Test
    public void testGetWordById() throws Exception {
        Word word = new Word();
        word.setId(1L);
        word.setKanji("こんにちは");
        word.setRomaji("konnichiwa");
        word.setEnglish("hello");
        word.setParts("{}");

        when(wordService.getWordById(1L)).thenReturn(word);

        mockMvc.perform(get("/api/words/1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.kanji").value("こんにちは"))
                .andExpect(jsonPath("$.english").value("hello"));
    }

    @Test
    public void testCreateWord() throws Exception {
        Word newWord = new Word();
        newWord.setKanji("こんにちは");
        newWord.setRomaji("konnichiwa");
        newWord.setEnglish("hello");
        newWord.setParts("{}");

        Word savedWord = new Word();
        savedWord.setId(1L);
        savedWord.setKanji("こんにちは");
        savedWord.setRomaji("konnichiwa");
        savedWord.setEnglish("hello");
        savedWord.setParts("{}");

        when(wordService.createWord(any(Word.class))).thenReturn(savedWord);

        mockMvc.perform(post("/api/words")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(newWord)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.kanji").value("こんにちは"))
                .andExpect(jsonPath("$.english").value("hello"));
    }
} 