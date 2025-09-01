// Use the preview (eye) button in the top right corner to view the console print outs.

function randomChoice(item) {
  return Math.floor(Math.random() * item.length);
}

function ears() {
  const earOptions = ["pointy", "rounded", "small"];
  const index = randomChoice(earOptions);
  return earOptions[index];
}

function feet() {
  const feetOptions = ["talons", "human feet", "hobbit feet"];
  const index = randomChoice(feetOptions);
  return feetOptions[index];
}

function hair() {
  const hairOptions = ["bald", "short", "medium", "long"];
  const index = randomChoice(hairOptions);
  return hairOptions[index];
}

function race() {
  const raceOptions = ["elf", "human", "halfling"];
  const index = randomChoice(raceOptions);
  return raceOptions[index];
}

function characterName() {
  const name = prompt("What do you want to name your character?");
  return name;
}

function createCharacter() {
  const name = characterName();
  return `${name} is a ${race()} with ${hair()} hair, ${ears()} ears, and ${feet()}.`;
}

console.log(createCharacter());
