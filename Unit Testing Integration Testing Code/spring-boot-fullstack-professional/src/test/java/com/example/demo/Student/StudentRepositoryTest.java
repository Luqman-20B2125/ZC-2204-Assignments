package com.example.demo.Student;

import java.beans.Transient;

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
        String email = "jamila@gmail.com"
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
        String email = "jamila@gmail.com"

        // When
        boolean expected = underTest.selectExistsEmail(email);

        // Then
        assertThat(expected).isFalse();
    }
}
