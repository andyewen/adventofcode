const fs = require('fs');
const readline = require('readline');

async function main() {
    const rl = readline.createInterface({
        input: fs.createReadStream('input.txt'),
    });

    let powerSum = 0;

    for await (const line of rl) {
        const [game_label_text, rounds_text] = line.split(': ');
        // const game_id = +game_label_text.split(' ')[1];

        let gameMaximums = {
            'red': 0,
            'green': 0,
            'blue': 0,
        };

        const rounds = rounds_text.split('; ');
        for (const round of rounds) {
            const hands = round.split(', ');
            const roundCounter = {
                'red': 0,
                'green': 0,
                'blue': 0,
            };
            for (const hand of hands) {
                const [num, colour] = hand.split(' ');
                roundCounter[colour] += +num;
            }

            for (const [colour, num] of Object.entries(roundCounter)) {
                if (num > gameMaximums[colour]) gameMaximums[colour] = num;
            }
        }

        let gamePower = 1;
        for (const n of Object.values(gameMaximums)) gamePower *= n;
        powerSum += gamePower;
    }

    console.log(powerSum);
}

main();
