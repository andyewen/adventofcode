use std::fs::File;
use std::io::{self, BufRead};

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Throw {
    Rock,
    Paper,
    Scissors,
}

#[derive(Debug, Eq, PartialEq)]
enum Result {
    Win,
    Loss,
    Draw,
}

#[derive(Debug)]
struct Round {
    opponent: Throw,
    result: Result,
}

fn string_to_throw(s: &str) -> Throw {
    match s {
        "A" => Throw::Rock,
        "B" => Throw::Paper,
        "C" => Throw::Scissors,
        _ => panic!("Not a valid Throw code!"),
    }
}

fn string_to_result(s: &str) -> Result {
    match s {
        "X" => Result::Loss,
        "Y" => Result::Draw,
        "Z" => Result::Win,
        _ => panic!("Not a valid Result code!"),
    }
}

fn what_beats(throw: &Throw) -> Throw {
    match throw {
        Throw::Rock => Throw::Paper,
        Throw::Paper => Throw::Scissors,
        Throw::Scissors => Throw::Rock,
    }
}

fn what_loses(throw: &Throw) -> Throw {
    match throw {
        Throw::Rock => Throw::Scissors,
        Throw::Paper => Throw::Rock,
        Throw::Scissors => Throw::Paper,
    }
}

fn calc_round_score(round: &Round) -> i32 {
    let response = match round.result {
        Result::Win => what_beats(&round.opponent),
        Result::Loss => what_loses(&round.opponent),
        Result::Draw => round.opponent,
    };

    let mut result: i32 = match response {
        Throw::Rock => 1,
        Throw::Paper => 2,
        Throw::Scissors => 3,
    };
    
    if round.opponent == response {
        result += 3;
    } else if response == what_beats(&round.opponent){
        result += 6
    }
    return result;
}

fn main() {
    let file = File::open("input.txt").unwrap();
    let lines = io::BufReader::new(file).lines();

    let mut total_score = 0;

    for line_result in lines {
        let line = line_result.unwrap();
        let mut parts = line.split(" ");
        let opponent_throw = string_to_throw(parts.next().unwrap());
        let result = string_to_result(parts.next().unwrap());

        let round = Round { opponent: opponent_throw, result: result };
        let round_score = calc_round_score(&round);

        total_score += round_score;
        // println!("{:?} -----> {:?}", round, round_score);
    }

    println!("{total_score}");
}
