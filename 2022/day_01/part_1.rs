use std::fs;

fn main() {
    let file_contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");

    let lines = file_contents.lines();

    let mut current_calory_count = 0;
    let mut max_calory_count = 0;

    for line in lines {
        if line.is_empty() {
            if current_calory_count > max_calory_count {
                max_calory_count = current_calory_count;
            }
            current_calory_count = 0;
        } else {
            current_calory_count += line.parse::<i32>().unwrap();
        }
    }
    println!("{max_calory_count}");
}
