const fs = require('fs');
const readline = require('readline');

let sum = 0;

function isDigit(s) {
    s = String(s);
    return s >= '0' && s <= '9';
}

function wordToNum(s) {
    const numStrs = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ];

    for (let i = 0; i < numStrs.length; i++) {
        const ns = numStrs[i];
        if (s.startsWith(ns)) {
            return String(i + 1);
        }
    }
    return null;
}

const rl = readline.createInterface({
    input: fs.createReadStream('input.txt'),
});

rl.on('line', (line) => {
    let first;
    let last;
    for (let i = 0; i < line.length; i++) {
        let n;
        if (isDigit(line[i])) {
            n = line[i];
        } else {
            n = wordToNum(line.slice(i));
        }

        if (n != null) {
            if (first == null) {
                first = n;
            }
            last = n;
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
