use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashSet;

fn calculate_priority(c: &char) -> i32 {
    let n = *c as i32;
        
    if n >= 97 {
        // Lowercase
        return n - 97 + 1;
    }
    // Uppercase
    return n - 65 + 27;
}

fn main() {
    let file = File::open("input.txt").unwrap();
    let lines = io::BufReader::new(file).lines();

    let mut priority_total = 0;
    let mut sets = Vec::new();

    for line_result in lines {
        let line = &line_result.unwrap();

        let line_set: HashSet<char> = line.chars().collect();
        sets.push(line_set);

        if sets.len() >= 3 {
            let intersection = &(&sets[0] & &sets[1]) & &sets[2];
            sets.clear();

            let c = intersection.iter().next().unwrap();
            priority_total += calculate_priority(c);
        }
    }

    println!("{}", priority_total);
}
