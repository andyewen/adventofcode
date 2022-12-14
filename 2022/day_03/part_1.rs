use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashSet;

fn main() {
    let file = File::open("input.txt").unwrap();
    let lines = io::BufReader::new(file).lines();

    let mut priority_total = 0;

    for line_result in lines {
        let line = line_result.unwrap();
        let i_middle = line.len() / 2;

        let left = line[..i_middle].chars().collect::<HashSet<_>>();
        let right = line[i_middle..].chars().collect::<HashSet<_>>();

        let mut intersection = left.intersection(&right);

        let c = intersection.next().unwrap();
        let mut n = *c as i32;
        
        if n >= 97 {
            // Lowercase
            n = n - 97 + 1;
        } else {
            // Lowercase
            n = n - 65 + 27;
        }

        priority_total += n;
    }

    
    println!("{}", priority_total);
}
