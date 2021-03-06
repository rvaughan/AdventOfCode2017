package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func apply(cur_val int, thing string) int {
	val, _ := strconv.Atoi(thing)

	return cur_val + val
}


func p2() {
	cur_val := 0
	finished := false
	val_map := make(map[int]bool)

	val_map[0] = true

	for !finished {
		f, _ := os.Open("../input.txt")
		defer f.Close()

		scanner := bufio.NewScanner(f)
		for scanner.Scan() {
			cur_val = apply(cur_val, scanner.Text())

			if ok, _ := val_map[cur_val]; ok {
				fmt.Println(cur_val)
				finished = true
				break
			}

			val_map[cur_val] = true
		}
	}
}

func p1() {
	f, _ := os.Open("../input.txt")
	defer f.Close()

	cur_val := 0

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		cur_val = apply(cur_val, scanner.Text())
	}

	fmt.Println(cur_val)
}

func main() {
	p1()
	p2()
}
