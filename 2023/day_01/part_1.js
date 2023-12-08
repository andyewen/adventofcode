const fs = require('fs');
const readline = require('readline');

let sum = 0;

function isDigit(s) {
    s = String(s);
    return s >= '0' && s <= '9';
}

const rl = readline.createInterface({
    input: fs.createReadStream('input.txt'),
});

rl.on('line', (line) => {
    let first;
    let last;
    for (const c of line) {
        if (isDigit(c)) {
            if (first == null) {
                first = c;
            }
            last = c;
        }
    }

    // console.log(line);
    if (first != null && last != null) {
        // console.log(first, last);
        const num = +(first + last);
        // console.log(num);
        sum += num;
    }
});

rl.on('close', () => {
    console.log(`Solution: ${sum}`);
});
