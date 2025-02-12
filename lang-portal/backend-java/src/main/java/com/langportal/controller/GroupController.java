package com.langportal.controller;

import com.langportal.model.Group;
import com.langportal.service.GroupService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/groups")
@RequiredArgsConstructor
@Tag(name = "Groups", description = "Group management APIs")
public class GroupController {
    private final GroupService groupService;

    @GetMapping
    @Operation(summary = "Get all groups")
    public ResponseEntity<List<Group>> getAllGroups() {
        return ResponseEntity.ok(groupService.getAllGroups());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get group by ID")
    public ResponseEntity<Group> getGroupById(@PathVariable Long id) {
        return ResponseEntity.ok(groupService.getGroupById(id));
    }

    @GetMapping("/search")
    @Operation(summary = "Search groups")
    public ResponseEntity<List<Group>> searchGroups(@RequestParam String query) {
        return ResponseEntity.ok(groupService.searchGroups(query));
    }

    @PostMapping
    @Operation(summary = "Create new group")
    public ResponseEntity<Group> createGroup(@RequestBody Group group) {
        return ResponseEntity.ok(groupService.createGroup(group));
    }

    @PutMapping("/{id}")
    @Operation(summary = "Update existing group")
    public ResponseEntity<Group> updateGroup(@PathVariable Long id, @RequestBody Group group) {
        return ResponseEntity.ok(groupService.updateGroup(id, group));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Delete group")
    public ResponseEntity<Void> deleteGroup(@PathVariable Long id) {
        groupService.deleteGroup(id);
        return ResponseEntity.ok().build();
    }

    @PostMapping("/{groupId}/words/{wordId}")
    @Operation(summary = "Add word to group")
    public ResponseEntity<Group> addWordToGroup(@PathVariable Long groupId, @PathVariable Long wordId) {
        return ResponseEntity.ok(groupService.addWordToGroup(groupId, wordId));
    }

    @DeleteMapping("/{groupId}/words/{wordId}")
    @Operation(summary = "Remove word from group")
    public ResponseEntity<Group> removeWordFromGroup(@PathVariable Long groupId, @PathVariable Long wordId) {
        return ResponseEntity.ok(groupService.removeWordFromGroup(groupId, wordId));
    }
}
