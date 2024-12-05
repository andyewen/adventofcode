const fs = require('fs');
const readline = require('readline');

async function* sectionGenerator(rl) {
    let acc = [];
    for await (let line of rl) {
        line = line.trim();
        if (line) {
            acc.push(line);
        } else if (acc.length) {
            yield acc;
            acc = [];
        }
    }
    if (acc.length) yield acc;
}

async function parseInput() {
    const rl = readline.createInterface({
        input: fs.createReadStream('input.txt'),
    });

    let seedNums;
    let mappingRangesBySourceType = {};

    let firstSection = true;
    for await (const section of sectionGenerator(rl)) {
        if (firstSection) {
            seedNums = section[0]
                .slice(section[0].search(' ') + 1)
                .split(' ')
                .map((n) => +n);

            firstSection = false; // First line has been processed.
        } else {
            let sectionLabel = section[0]; // a-to-b map:
            let srcDestPart = sectionLabel.slice(0, sectionLabel.search(' ')); // a-to-b
            let [srcType, destType] = srcDestPart.split('-to-');

            let group = mappingRangesBySourceType[srcType];
            if (group == null) {
                group = mappingRangesBySourceType[srcType] = [];
            }
            
            for (const line of section.slice(1)) {
                const [destStart, srcStart, length] = line.split(' ').map((n) => +n);
                group.push({
                    srcType,
                    destType,
                    srcStart,
                    destStart,
                    srcEnd: srcStart + length,
                    destEnd: destStart + length,
                });
            }
        }
    }

    return {seedNums, mappingRangesBySourceType};
}

async function main() {
    const {seedNums, mappingRangesBySourceType} = await parseInput();

    let minLocation = Number.MAX_SAFE_INTEGER;

    for (const seedNum of seedNums) {
        let type = 'seed';
        let num = seedNum;
        while (true) {
            let mapping = mappingRangesBySourceType[type];
            if (!mapping) {
                break;
            }

            const range = mapping.find((range) => 
                num >= range.srcStart && num < range.srcEnd
            );
            if (range) {
                type = range.destType;
                num = range.destStart + (num - range.srcStart);
            } else {
                type = mapping[0].destType;
            }
        }

        if (type === 'location' && num < minLocation) {
            minLocation = num;
        }
    }

    console.log(minLocation);
}

main();
