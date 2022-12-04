use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::cmp::max;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn part1() {
    if let Ok(lines) = read_lines("../input.txt") {
        let mut max_calories = 0;
        let mut elf_calories = 0;

        for line in lines {
            if let Ok(calories_str) = line {
                if calories_str.trim().is_empty() {
                    max_calories = max(max_calories, elf_calories);
                    elf_calories = 0;
                }
                else {
                    let calories: i32 = calories_str.parse().unwrap();
                    elf_calories += calories;
                }
            }
        }

        max_calories = max(max_calories, elf_calories);

        println!("Solution for part 1: {}", max_calories);
    }
}

fn part2() {
    if let Ok(lines) = read_lines("../input.txt") {
        let mut elf_calories = 0;
        let mut all_calories = vec![];

        for line in lines {
            if let Ok(calories_str) = line {
                if calories_str.trim().is_empty() {
                    all_calories.push(elf_calories);
                    elf_calories = 0
                }
                else {
                    let calories: i32 = calories_str.parse().unwrap();
                    elf_calories += calories;
                }
            }
        }

        all_calories.push(elf_calories);

        all_calories.sort();

        let max_calories = all_calories[all_calories.len() - 3] + all_calories[all_calories.len() - 2] + all_calories[all_calories.len() - 1];

        println!("Solution for part 2: {}", max_calories);
    }
}

fn main() {
    part1();
    part2();
}
