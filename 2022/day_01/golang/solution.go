package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

func p2() {
	f, _ := os.Open("../input.txt")
	defer f.Close()

	all_calories := []float64{}
	elf_calories := 0.0

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		calories, _ := strconv.Atoi(scanner.Text())
		if calories == 0 {
			all_calories = append(all_calories, elf_calories)
			elf_calories = 0.0
		} else {
			elf_calories += float64(calories)
		}
	}

	all_calories = append(all_calories, elf_calories)

	sort.Float64s(all_calories)

	calories := 0.0
	for i := 1; i < 4; i++ {
		calories += all_calories[len(all_calories)-i]
	}

	fmt.Println(calories)
}

func p1() {
	f, _ := os.Open("../input.txt")
	defer f.Close()

	max_calories := 0.0
	elf_calories := 0.0

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		calories, _ := strconv.Atoi(scanner.Text())
		if calories == 0 {
			max_calories = math.Max(max_calories, elf_calories)
			elf_calories = 0.0
		} else {
			elf_calories += float64(calories)
		}
	}

	max_calories = math.Max(max_calories, elf_calories)

	fmt.Println(max_calories)
}

func main() {
	p1()
	p2()
}
