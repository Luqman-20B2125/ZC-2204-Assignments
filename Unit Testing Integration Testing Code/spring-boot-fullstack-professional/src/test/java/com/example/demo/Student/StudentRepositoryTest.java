package com.example.demo.Student;

import java.beans.Transient;

import com.example.demo.student.Student;
import com.example.demo.student.StudentRepository;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

@DataJpaTest
public class StudentRepositoryTest {
    
    @Autowired
    private StudentRepository underTest;

    @AfterEach
    void tearDown() {
        underTest.deleteAll();
    }

    @Test
    void itShouldCheckIfStudentEmailExists() {
        // Given
        String email = "jamila@gmail.com";
        Student student = new Student("Jamila", email,Gender.FEMALE);
        underTest.save(student);

        // When
        boolean expected = underTest.selectExistsEmail(email);

        // Then
        assertThat(expected).isTrue();
    }

    @Test
    void itShouldCheckIfStudentEmailDoesNotExist() {
        // Given
        String email = "jamila@gmail.com";

        // When
        boolean expected = underTest.selectExistsEmail(email);

        // Then
        assertThat(expected).isFalse();
    }
}
