package com.example.demo;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class DemoApplicationTests {
	Calculator underTest = new Calculator();

	@Test
	void itShouldAddTwoNumbers() {
		// Given
		int numberOne = 20;
		int numberTwo = 30;

		// When
		int result = underTest.add(numberOne, numberTwo);

		// Then
		int expected = 50;
		assertThat(result).isEqualTo(expected);
	}
	
	class Calculator {
		int add(int a, int b) {
			return a + b;
		}
	}
}
