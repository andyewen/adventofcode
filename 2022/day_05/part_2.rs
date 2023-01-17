use std::fs::File;
use std::io::{self, BufRead};

const NUM_STACKS: usize = 9;

fn process_state_line(stacks: &mut Vec<String>, line: &str) {
    for i in 0..NUM_STACKS {
        let c = line.chars().nth(i * 4 + 1).unwrap();
        if c != ' ' {
            stacks[i].insert(0, c);
        }
    }
}

fn process_action_line(stacks: &mut Vec<String>, line: &str) {
    let words: Vec<_> = line.split(' ').collect();
    let qty = words[1].parse::<i32>().unwrap();
    let src = words[3].parse::<usize>().unwrap() - 1;
    let dest = words[5].parse::<usize>().unwrap() - 1;

    let length = stacks[src].len();
    let chunk = String::from(&stacks[src][length - qty as usize..]);
    stacks[dest].push_str(&chunk);
    stacks[src].replace_range(length - qty as usize.., "");
}

fn main() {
    let file = File::open("input.txt").unwrap();
    let lines = io::BufReader::new(file).lines().map(|line| line.unwrap());

    let mut stacks = vec![String::new(); NUM_STACKS];

    for line in lines {
        if line.starts_with('[') {
            // Initial state lines start with "[".
            process_state_line(&mut stacks, &line);
        } else if line.starts_with("move") {
            // Action phase lines start with "move".
            process_action_line(&mut stacks, &line);
        }
    }

    let output: String = stacks.iter().filter_map(|s| s.chars().last()).collect();
    println!("{output}");
}
