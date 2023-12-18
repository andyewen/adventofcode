const fs = require('fs');
const readline = require('readline');

const lineRe = /Card\s+(\d+):\s+(\d+(?:\s+\d+)*)\s+\|\s+(\d+(?:\s+\d+)*)/;

function countCards(cardIdMatchingNumbers, id) {
    // Recursive function. Cards are repeatedly processed. There might be a better
    // way where we work through the cards backwards but this works.
    const matching = cardIdMatchingNumbers.get(id);
    let numCards = 1; // This card.
    for (let i = 1; i < matching + 1; i += 1) {
        numCards += countCards(cardIdMatchingNumbers, id + i);
    }
    return numCards;
}

async function main() {
    const rl = readline.createInterface({
        input: fs.createReadStream('input.txt'),
    });

    const cardIdMatchingNumbers = new Map();

    for await (let line of rl) {
        const match = line.match(lineRe);
        if (match == null) {
            throw new Error('Line does not match!');
        }

        let cardId = +match[1];
        let cardNums = match[2];
        let winningNums = match[3];

        cardNums = new Set(cardNums.split(/\s+/).map((n) => +n));
        winningNums = new Set(winningNums.split(/\s+/).map((n) => +n));

        const intersection = new Set();
        for (const cardN of cardNums) {
            if (winningNums.has(cardN)) {
                intersection.add(cardN);
            }
        }

        const cardWinningCount = intersection.size;
        cardIdMatchingNumbers.set(cardId, cardWinningCount);
    }

    let totalCards = 0;
    for (const cardId of cardIdMatchingNumbers.keys()) {
        totalCards += countCards(cardIdMatchingNumbers, cardId);
    }
    console.log(totalCards);
}

main();
