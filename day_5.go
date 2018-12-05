package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func part1() {
	text := readInput()
	fmt.Println(len(minimizePolymer(text)))
}

func part2() {
	orig := readInput()
	min_length := 10000
	for c := 97; c < 123; c++ {
		text := removeUpperAndLower(byte(c), orig)
		text = minimizePolymer(text)

		if len(text) < min_length {
			min_length = len(text)
		}
	}

	fmt.Println(min_length)
}

func readInput() string {
	file, _ := os.Open("input.txt")
	rdr := bufio.NewReader(file)

	text, _ := rdr.ReadString(byte('\n'))

	return text
}

func removeUpperAndLower(char byte, text string) string {
	for i := 0; i < len(text); i++ {
		if int(text[i]) == int(char) || int(text[i]) == int(char)-32 {
			text = text[:i] + text[i+1:]
			i--
		}
	}

	return text
}

func minimizePolymer(text string) string {
	for i := 0; i < len(text)-1; i++ {
		if math.Abs(float64(int(text[i])-int(text[i+1]))) == 32 {
			if len(text) == 2 {
				text = ""
			} else {
				text = text[:i] + text[i+2:]
			}
			i = -1
		}
	}

	return text
}
