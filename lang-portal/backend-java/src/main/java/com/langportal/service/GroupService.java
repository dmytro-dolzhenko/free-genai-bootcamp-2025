package com.langportal.service;

import com.langportal.model.Group;
import com.langportal.model.Word;
import com.langportal.repository.GroupRepository;
import com.langportal.repository.WordRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
public class GroupService {
    private final GroupRepository groupRepository;
    private final WordRepository wordRepository;

    public List<Group> getAllGroups() {
        return groupRepository.findAll();
    }

    public Group getGroupById(Long id) {
        return groupRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Group not found with id: " + id));
    }

    public List<Group> searchGroups(String query) {
        return groupRepository.findByNameContainingIgnoreCase(query);
    }

    @Transactional
    public Group createGroup(Group group) {
        return groupRepository.save(group);
    }

    @Transactional
    public Group updateGroup(Long id, Group group) {
        Group existingGroup = getGroupById(id);
        existingGroup.setName(group.getName());
        return groupRepository.save(existingGroup);
    }

    @Transactional
    public void deleteGroup(Long id) {
        groupRepository.deleteById(id);
    }

    @Transactional
    public Group addWordToGroup(Long groupId, Long wordId) {
        Group group = getGroupById(groupId);
        Word word = wordRepository.findById(wordId)
            .orElseThrow(() -> new RuntimeException("Word not found with id: " + wordId));
        
        group.getWords().add(word);
        group.setWordsCount(group.getWordsCount() + 1);
        return groupRepository.save(group);
    }

    @Transactional
    public Group removeWordFromGroup(Long groupId, Long wordId) {
        Group group = getGroupById(groupId);
        Word word = wordRepository.findById(wordId)
            .orElseThrow(() -> new RuntimeException("Word not found with id: " + wordId));
        
        group.getWords().remove(word);
        group.setWordsCount(group.getWordsCount() - 1);
        return groupRepository.save(group);
    }
}
