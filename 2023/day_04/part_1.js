const fs = require('fs');
const readline = require('readline');

const lineRe = /Card\s+\d+:\s+(\d+(?:\s+\d+)*)\s+\|\s+(\d+(?:\s+\d+)*)/;

async function main() {
    const rl = readline.createInterface({
        input: fs.createReadStream('input.txt'),
    });

    let scoreSum = 0;

    for await (let line of rl) {
        const match = line.match(lineRe);
        if (match == null) {
            throw new Error('Line does not match!');
        }

        let cardNums = match[1];
        let winningNums = match[2];

        cardNums = new Set(cardNums.split(/\s+/).map((n) => +n));
        winningNums = new Set(winningNums.split(/\s+/).map((n) => +n));

        const intersection = new Set();
        for (const cardN of cardNums) {
            if (winningNums.has(cardN)) {
                intersection.add(cardN);
            }
        }

        const score = intersection.size > 0 ? 2 ** (intersection.size - 1) : 0;
        scoreSum += score;
    }

    console.log(scoreSum);
}

main();
