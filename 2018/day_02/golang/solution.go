package main

import (
	"bufio"
	"fmt"
	"os"
)

func p2() {
	f, _ := os.Open("../input.txt")
	defer f.Close()

	boxids := make(map[string]bool)

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		thing := scanner.Text()

		boxids[thing] = true
	}

	for key, _ := range boxids {
		for int_key, _ := range boxids {
			if key == int_key {
				continue
			}

			pos := 0
			diff := 0
			for pos < len(key) {
				if key[pos] != int_key[pos] {
					diff++
				}

				pos++
			}

			if diff == 1 {
				output := ""
				pos := 0
				for pos < len(key) {
					if key[pos] == int_key[pos] {
						output += string(key[pos])
					}
					pos++
				}

				fmt.Println(output)

				break
			}
		}
	}
}

func p1() {
	f, _ := os.Open("../input.txt")
	defer f.Close()

	two_count := 0
	three_count := 0

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		thing := scanner.Text()

		mymap := make(map[rune]int)

		for _, char := range thing {
			if _, ok := mymap[char]; ok {
				mymap[char]++
			} else {
				mymap[char] = 1
			}
		}

		v2 := 0
		v3 := 0
		for _, val := range mymap {
			if val == 2 {
				v2 = 1
			}

			if val == 3 {
				v3 = 1
			}
		}

		two_count += v2
		three_count += v3
	}

	fmt.Println(two_count * three_count)
}

func main() {
	p1()
	p2()
}
