let rawInput;

let roomWidth;
let roomHeight;
let originalRoomState;
let currentRoomState;
let seatSize;

let seatColours;
let forceDraw = true;
let looping = false;

let neighbourCountingFunc;
let neighbourLimit;

let btnPart1;
let btnPart2;

function preload() {
  rawInput = loadStrings("input.txt");
}

function setup() {
  originalRoomState = rawInput.map((row) => row.split(""));
  roomWidth = originalRoomState[0].length;
  roomHeight = originalRoomState.length;
  seatSize = 7;
  canvasWidth = roomWidth * seatSize;
  canvasHeight = roomWidth * seatSize;

  seatColours = {
    "L": color(0, 30, 80),
    "#": color(0, 50, 180),
    ".": color(0),
  };

  btnPart1 = createButton("part 1");
  btnPart1.mouseClicked(() => reset(1));
  btnPart1.style("font-size", "22px");
  btnPart1.style("margin-right", "8px");

  btnPart2 = createButton("part 2");
  btnPart2.mouseClicked(() => reset(2));
  btnPart2.style("font-size", "22px");

  createCanvas(canvasWidth, canvasHeight);
  background(0);
  fill(255);
  textSize(32);
  text("Press a button to start.", 30, 60);
  noStroke();
  // frameRate(2);
}

function reset(part) {
  if (part == 1) {
    neighbourCountingFunc = countNeighboursAdjacent;
    neighbourLimit = 4;
  } else if (part == 2) {
    neighbourCountingFunc = countNeighboursRay;
    neighbourLimit = 5;
  }
  currentRoomState = originalRoomState;
  forceDraw = true;
  looping = true;
  loop();
}

function draw() {
  if (!looping) {
    noLoop();
    return;
  }

  // Update state.
  var start = new Date();
  oldState = currentRoomState;
  generationResult = doGeneration(currentRoomState);
  currentRoomState = generationResult.state;
  changes = generationResult.numChanges;

  var generationComplete = new Date();

  // Draw current state.
  for (let j = 0; j < roomHeight; j++) {
    for (let i = 0; i < roomWidth; i++) {
      const chairState = currentRoomState[j][i];
      const oldChairState = oldState[j][i];
      if (forceDraw || chairState != oldChairState) {
        const xPos = i * seatSize;
        const yPos = j * seatSize;
        fill(seatColours[chairState] || 0);
        rect(xPos, yPos, seatSize, seatSize);
      }
    }
  }

  forceDraw = false;

  var drawComplete = new Date();
  // console.log(`Sim: ${generationComplete - start}, Draw: ${drawComplete - generationComplete}`);

  if (!changes) {
    looping = false;
    const numSeated = currentRoomState
      .map((row) => row.reduce((acc, curr) => acc + (curr == "#"), 0))
      .reduce((acc, curr) => acc + curr, 0);
    const output = `Occupied seats:\n${numSeated}`;
    fill(255);
    text(output, 30, 60);
  }
}


function occupied(state, x, y) {
  if (y < 0 || y >= state.length) return false;
  const row = state[y];
  if (x < 0 || x >= row.length) return false;
  return row[x] === "#";
}

function countNeighboursAdjacent(state, x, y) {
  const neighbourCoords = [
    [x + 1, y],
    [x + 1, y + 1],
    [x, y + 1],
    [x - 1, y + 1],
    [x - 1, y],
    [x - 1, y - 1],
    [x, y - 1],
    [x + 1, y - 1],
  ];
  return neighbourCoords
    .filter((coord) => occupied(state, coord[0], coord[1]))
    .length;
}

function directionHasNeighbour(state, startX, startY, dX, dY) {
  let x = startX;
  let y = startY;
  while (true) {
    x += dX;
    y += dY;
    
    if (x < 0 || x >= roomWidth || y < 0 || y >= roomHeight) {
      break;
    }
    
    seatState = state[y][x];
    if (seatState == "L") {
      return false;
    } else if (seatState == "#") {
      return true;
    }
  };
  return false;
}

function countNeighboursRay(state, x, y) {
  const directions = [
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
  ];
  return directions
    .filter((dir) => directionHasNeighbour(state, x, y, dir[0], dir[1]))
    .length;
}


function doGeneration(state) {
  const newState = state.map(row => row.slice());

  let numChanges = 0;

  for (let j = 0; j < roomHeight; j++) {
    for (let i = 0; i < roomWidth; i++) {
      const numOccupiedNeighbours = neighbourCountingFunc(state, i, j);

      const currentSeatState = state[j][i];
      let newSeatState = currentSeatState;

      if (currentSeatState == "L") {
        if (numOccupiedNeighbours === 0) {
          newSeatState = "#";
          numChanges++;
        }
      } else if (currentSeatState == "#") {
        if (numOccupiedNeighbours >= neighbourLimit) {
          newSeatState = "L";
          numChanges++;
        }
      }
      newState[j][i] = newSeatState;
    }
  }

  return {
    state: newState,
    numChanges
  };
}
