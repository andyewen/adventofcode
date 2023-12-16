const fs = require('fs');
const readline = require('readline');

const NON_SYMBOLS = '0123456789.'

const neighbours = [
    {x: -1, y: -1}, {x: +0, y: -1}, {x: +1, y: -1},
    {x: -1, y: +0},                 {x: +1, y: +0},
    {x: -1, y: +1}, {x: +0, y: +1}, {x: +1, y: +1},
];

function coordToStr(coord) {
    return `${+coord.x}_${+coord.y}`;
}

function strToCoord(coord) {
    coord = coord.split('_');
    return {x: coord[0], y: coord[1]};
}

async function main() {
    const rl = readline.createInterface({
        input: fs.createReadStream('input.txt'),
    });

    // read entire file into memory as a list of lists of strings.
    const schematic = [];
    for await (let line of rl) {
        schematic.push(line);
    }

    let numsByNeighbourAsteriskCoord = new Map();

    for (let y = 0; y < schematic.length; y++) {
        let numAcc = '';
        let numAsteriskNeighbours = new Set();
        for (let x = 0; x < schematic[y].length; x++) {
            const char = schematic[y][x];
            const isDigit = !isNaN(char);
            if (isDigit) {
                // is number: add it to accumulator
                numAcc += char;
                // does it have an asterisk nearby?
                for (const {x: dx, y: dy} of neighbours) {
                    const nx = x + dx;
                    const ny = y + dy;
                    if (ny < 0 || ny >= schematic.length) continue;
                    if (nx < 0 || nx >= schematic[ny].length) continue;

                    if (schematic[ny][nx] === '*') {
                        // add the asterisk's coord to the set of asterisks this number neighbours.
                        numAsteriskNeighbours.add(coordToStr({x: nx, y: ny}));
                    }
                }
            }

            if (numAcc && (!isDigit || x === schematic[y].length - 1)) {
                // num is complete because current char is not a digit or we're on the last char in
                // the line.
                for (const asteriskCoord of numAsteriskNeighbours) {
                    let nums = numsByNeighbourAsteriskCoord.get(asteriskCoord);
                    if (nums == null) {
                        nums = [];
                        numsByNeighbourAsteriskCoord.set(asteriskCoord, nums);
                    }
                    nums.push(+numAcc);
                }
                numAcc = '';
                numAsteriskNeighbours = new Set();
            }
        }
    }

    const gearRatios = Array.from(numsByNeighbourAsteriskCoord.values())
        .filter((group) => group.length == 2) // Valid geat ratios only have two numbers.
        .map((group) => group[0] * group[1]); // Gear ratios calculated by multiplying the two numbers.

    let gearRatioSum = 0;
    for (const ratio of gearRatios) {
        gearRatioSum += ratio;
    }
    console.log(gearRatioSum);
}

main();
