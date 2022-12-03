use std::fs::File;
use std::io::{self, BufRead};

#[derive(Debug)]
enum Throw {
    Rock,
    Paper,
    Scissors,
}

#[derive(Debug)]
struct Round {
    opponent: Throw,
    response: Throw,
}

fn string_to_throw(s: &str) -> Throw {
    match s {
        "A" => Throw::Rock,
        "B" => Throw::Paper,
        "C" => Throw::Scissors,
        "X" => Throw::Rock,
        "Y" => Throw::Paper,
        "Z" => Throw::Scissors,
        _ => panic!("Not a valid Throw code!"),
    }
}

fn main() {
    let file = File::open("input.txt").unwrap();
    let lines = io::BufReader::new(file).lines();

    let mut rounds = Vec::new();

    for line_result in lines {
        let line = line_result.unwrap();
        let mut parts = line.split(" ");
        let opp = string_to_throw(parts.next().unwrap());
        let res = string_to_throw(parts.next().unwrap());

        rounds.push(Round { opponent: opp, response: res });
    }

    println!("{:?}", rounds);
}
