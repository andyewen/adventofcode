const fs = require('fs');
const readline = require('readline');

const NON_SYMBOLS = '0123456789.'

const neighbours = [
    {x: -1, y: -1}, {x: +0, y: -1}, {x: +1, y: -1},
    {x: -1, y: +0},                 {x: +1, y: +0},
    {x: -1, y: +1}, {x: +0, y: +1}, {x: +1, y: +1},
];

async function main() {
    const rl = readline.createInterface({
        input: fs.createReadStream('input.txt'),
    });

    const schematic = [];
    for await (let line of rl) {
        line = line.split('');
        schematic.push(line);
    }

    let partNumSum = 0;

    for (let y = 0; y < schematic.length; y++) {
        let numAcc = '';
        let numHasSymbol = false;
        for (let x = 0; x < schematic[y].length; x++) {
            const char = schematic[y][x];
            const isDigit = !isNaN(char);
            if (isDigit) {
                // is number add it to accumulator
                numAcc += char;
                // does it have a symbol nearby?
                if (!numHasSymbol) {
                    numHasSymbol = neighbours.some(({x: dx, y: dy}) => {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (ny < 0 || ny >= schematic.length) return false;
                        if (nx < 0 || nx >= schematic[ny].length) return false;
                        const nChar = schematic[ny][nx];
                        if (!NON_SYMBOLS.includes(nChar)) return true;
                    });
                }
            }

            if (numAcc && (!isDigit || x === schematic[y].length - 1)) {
                // num is over because current char is not a digit or we're on the last char in the
                // line.
                if (numHasSymbol) {
                    partNumSum += +numAcc;
                }
                numAcc = '';
                numHasSymbol = false;
            }
        }
    }

    console.log(partNumSum);
}

main();
