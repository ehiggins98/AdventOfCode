package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, _ := os.Open("input.txt")
	rdr := bufio.NewReader(file)

	lines := make([]string, 0)

	for line, _ := rdr.ReadString(byte('\n')); line != ""; line, _ = rdr.ReadString(byte('\n')) {
		lines = append(lines, line)
		result := compare(lines, line)
		if result != "" {
			fmt.Println(result)
			return
		}
	}
}

func part1() {
	file, _ := os.Open("input.txt")
	rdr := bufio.NewReader(file)

	line, _ := rdr.ReadString(byte('\n'))

	twoReps := 0
	threeReps := 0
	for line != "" {
		two, three := twoOrThreeRepetitions(line)
		if two {
			twoReps++
		}
		if three {
			threeReps++
		}
		line, _ = rdr.ReadString(byte('\n'))
	}

	fmt.Println(twoReps * threeReps)
}

func twoOrThreeRepetitions(s string) (bool, bool) {
	counts := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		val, ok := counts[s[i]]
		if ok {
			counts[s[i]] = val + 1
		} else {
			counts[s[i]] = 1
		}
	}

	twoReps := false
	threeReps := false
	for _, v := range counts {
		if v == 2 {
			twoReps = true
		}
		if v == 3 {
			threeReps = true
		}
	}

	return twoReps, threeReps
}

func compare(lines []string, line string) string {
	for _, e := range lines {
		if compareStrings(e, line) {
			return commonPart(e, line)
		}
	}
	return ""
}

func compareStrings(l1 string, l2 string) bool {
	differing := 0
	if len(l1) != len(l2) {
		return false
	}

	for i := 0; i < len(l1); i++ {
		if l1[i] != l2[i] {
			differing++
		}
	}
	return differing == 1
}

func commonPart(l1 string, l2 string) string {
	fmt.Println(l1, l2)
	for i := 0; i < len(l1); i++ {
		if l1[i] != l2[i] {
			return l1[:i] + l1[i+1:]
		}
	}
	return ""
}
