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

    for await (const line of rl) {
        const [game_label_text, rounds_text] = line.split(': ');
        const game_id = +game_label_text.split(' ')[1];

        const rounds = rounds_text.split(';');
        for (const round of rounds) {
            const han
        }
    }
}

main();
