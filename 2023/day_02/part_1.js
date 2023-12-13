const fs = require('fs');
const readline = require('readline');

const maximums = {
    'red': 12,
    'green': 13,
    'blue': 14,
};

async function main() {
    const rl = readline.createInterface({
        input: fs.createReadStream('input.txt'),
    });

    let validGames = 0;

    for await (const line of rl) {
        const [game_label_text, rounds_text] = line.split(': ');
        const game_id = +game_label_text.split(' ')[1];

        let gameValid = true;

        const rounds = rounds_text.split('; ');
        for (const round of rounds) {
            const hands = round.split(', ');
            const counter = {
                'red': 0,
                'green': 0,
                'blue': 0,
            };
            for (const hand of hands) {
                const [num_str, colour] = hand.split(' ');
                counter[colour] += +num_str;
            }

            let roundValid = Object.entries(counter).every(([colour, num]) => num <= maximums[colour]);
            if (!roundValid) {
                gameValid = false;
                break;
            }
        }

        if (gameValid) validGames += game_id;
    }

    console.log(validGames);
}

main();
