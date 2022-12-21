use std::fs::File;
use std::io::{self, BufRead};

#[derive(Debug)]
struct Range {
    bottom: i32,
    top: i32,
}

fn parse_range_str(s: &str) -> Range {
    let mut nums = s.split('-');
    let a = nums.next().unwrap();
    let b = nums.next().unwrap();
    Range {
        bottom: a.parse::<i32>().unwrap(), 
        top: b.parse::<i32>().unwrap(),
    }
}

fn ranges_overlap(a: Range, b: Range) -> bool {
    (a.bottom <= b.bottom && a.top >= b.top)
    || (b.bottom <= a.bottom && b.top >= a.top)
}

fn main() {
    let file = File::open("input.txt").unwrap();
    let lines = io::BufReader::new(file).lines().map(|line| line.unwrap());

    let mut overlapping_count = 0;

    for line in lines {
        let mut ranges = line.split(',');
        
        let range_a = parse_range_str(&ranges.next().unwrap());
        let range_b = parse_range_str(&ranges.next().unwrap());

        overlapping_count += ranges_overlap(range_a, range_b) as i32;
    }

    println!("{overlapping_count}");
}
