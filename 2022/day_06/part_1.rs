use std::collections::HashSet;
use std::iter::FromIterator;
use std::fs;

const CHUNK_SIZE: usize = 4;

fn main() {
    let file_contents = fs::read_to_string("input.txt").unwrap();

    let len = file_contents.len();
    for i in 0..len - CHUNK_SIZE {
        let chunk = &file_contents[i..i+CHUNK_SIZE];
        let chunk_set: HashSet<u8> = HashSet::from_iter(chunk.bytes());

        if chunk_set.len() == CHUNK_SIZE {
            println!("{}", i + CHUNK_SIZE);
            break;
        }
    }
}