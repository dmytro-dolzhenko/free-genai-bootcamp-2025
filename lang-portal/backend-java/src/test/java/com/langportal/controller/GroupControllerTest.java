package com.langportal.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.langportal.model.Group;
import com.langportal.service.GroupService;
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
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(GroupController.class)
@AutoConfigureMockMvc(addFilters = false)
public class GroupControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private GroupService groupService;

    @Test
    public void testGetAllGroups() throws Exception {
        Group group1 = new Group();
        group1.setId(1L);
        group1.setName("Test Group 1");

        Group group2 = new Group();
        group2.setId(2L);
        group2.setName("Test Group 2");

        List<Group> groups = Arrays.asList(group1, group2);

        when(groupService.getAllGroups()).thenReturn(groups);

        mockMvc.perform(get("/api/groups")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$[0].id").value(1))
                .andExpect(jsonPath("$[0].name").value("Test Group 1"))
                .andExpect(jsonPath("$[1].id").value(2))
                .andExpect(jsonPath("$[1].name").value("Test Group 2"));
    }

    @Test
    public void testGetGroupById() throws Exception {
        Group group = new Group();
        group.setId(1L);
        group.setName("Test Group");

        when(groupService.getGroupById(1L)).thenReturn(group);

        mockMvc.perform(get("/api/groups/1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("Test Group"));
    }

    @Test
    public void testCreateGroup() throws Exception {
        Group newGroup = new Group();
        newGroup.setName("New Group");

        Group savedGroup = new Group();
        savedGroup.setId(1L);
        savedGroup.setName("New Group");

        when(groupService.createGroup(any(Group.class))).thenReturn(savedGroup);

        mockMvc.perform(post("/api/groups")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(newGroup)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("New Group"));
    }

    @Test
    public void testUpdateGroup() throws Exception {
        Group updatedGroup = new Group();
        updatedGroup.setId(1L);
        updatedGroup.setName("Updated Group");

        when(groupService.updateGroup(eq(1L), any(Group.class))).thenReturn(updatedGroup);

        mockMvc.perform(put("/api/groups/1")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(updatedGroup)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("Updated Group"));
    }

    @Test
    public void testDeleteGroup() throws Exception {
        mockMvc.perform(delete("/api/groups/1"))
                .andExpect(status().isOk());
    }
} 