use std::fs;

fn main() {
    let file_contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");

    let lines = file_contents.lines();

    let mut current_calory_count = 0;
    let mut elf_calory_counts: Vec<i32> = Vec::new();

    for line in lines {
        if line.is_empty() {
            elf_calory_counts.push(current_calory_count);
            current_calory_count = 0;
        } else {
            current_calory_count += line.parse::<i32>().unwrap();
        }
    }

    elf_calory_counts.sort();

    let top_three_sum = elf_calory_counts.iter().rev().take(3).sum::<i32>();

    println!("{top_three_sum}")
}
