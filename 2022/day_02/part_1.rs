use std::fs::File;
use std::io::{self, BufRead};

#[derive(Debug, Eq, PartialEq)]
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

fn calc_round_score(round: &Round) -> i32 {
    let mut result: i32 = match round.response {
        Throw::Rock => 1,
        Throw::Paper => 2,
        Throw::Scissors => 3,
    };
    
    if round.opponent == round.response {
        result += 3;
    } else if 
        (round.opponent == Throw::Rock && round.response == Throw::Paper)
        || (round.opponent == Throw::Paper && round.response == Throw::Scissors)
        || (round.opponent == Throw::Scissors && round.response == Throw::Rock)
    {
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
        let opp = string_to_throw(parts.next().unwrap());
        let res = string_to_throw(parts.next().unwrap());

        let round = Round { opponent: opp, response: res };
        let round_score = calc_round_score(&round);

        total_score += round_score;
        // println!("{:?} -----> {:?}", round, round_score);
    }

    println!("{total_score}");
}
