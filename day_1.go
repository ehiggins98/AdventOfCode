package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	fmt.Println(part_2())
}

func part_1() {
	f, _ := os.Open("input.txt")
	rdr := bufio.NewReader(f)

	line, _ := rdr.ReadString(byte('\n'))
	result := 0
	for line != "" {
		i, _ := strconv.Atoi(line[:len(line)-1])
		result += i
		line, _ = rdr.ReadString(byte('\n'))
	}
	fmt.Println(result)
}

func part_2() int {
	seen := make(map[int]bool)
	result := 0

	for true {
		f, _ := os.Open("input.txt")
		rdr := bufio.NewReader(f)

		line, _ := rdr.ReadString(byte('\n'))
		for line != "" {
			i, _ := strconv.Atoi(line[:len(line)-1])
			result += i
			_, in_seen := seen[result]

			if !in_seen {
				seen[result] = true
			} else {
				return result
			}

			line, _ = rdr.ReadString(byte('\n'))
		}
	}
	return 0
}
