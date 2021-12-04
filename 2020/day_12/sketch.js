let bgColour;

let rawInput;
let navInstructions;
let currentInstructionIndex;

let x = 0;
let y = 0;
let direction = 0;

function preload() {
  rawInput = loadStrings("input.txt");
}

function setup() {
  navInstructions = rawInput
    .filter((line) => line)
    .map((line) => ({
      action: line.charAt(0), 
      value: ~~line.slice(1),
    }));
  console.log(navInstructions);
  
  currentInstructionIndex = 0;

  createCanvas(600, 600);
  bgColour = color(0, 20, 80);
}

function doInstruction(instruction) {
  const directionToAction = {
    0: "E",
    90: "S",
    180: "W",
    270: "N",
  };

  let { action } = instruction;
  const { value } = instruction;

  if (action == "F") {
    action = directionToAction[direction];
  }

  switch (action) {
    case "N":
      y -= value;
      break;
    case "E":
      x += value;
      break;
    case "S":
      y += value;
      break;
    case "W":
      x -= value;
      break;
    case "L":
      direction -= value;
      break;
    case "R":
      direction += value;
      break;
  }
  direction %= 360;
  if (direction < 0) {
    direction += 360;
  }
}

function draw() {
  const done = currentInstructionIndex >= navInstructions.length;
  if (!done) {
    currentInstruction = navInstructions[currentInstructionIndex];

    doInstruction(currentInstruction);

    currentInstructionIndex++;
  }
  
  noStroke();
  fill(255);

  push();

  background(bgColour);
  translate(width / 2, height / 2);
  scale(0.1);
  
  ellipse(x, y, 60);

  pop();

  if (done) {
    textSize(16);
    text(`X: ${x}\nY: ${y}\nD: ${x + y}`, 10, 25);
  }
}
