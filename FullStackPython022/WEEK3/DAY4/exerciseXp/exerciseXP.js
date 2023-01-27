//ex 1
let x = 1;
let y = 3;
if (x > y){
    console.log(`${x} is the biggest number`)
} else {
    console.log(`${y} is the biggest number`)
}

// ex 2
var newDog = 'Chihuahua';
// var newDog = 'banana';
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog == 'Chihuahua'){
    console.log(`I love Chihuahuas, it's my favorite dog breed`);
} else {
    console.log(`I dont care, I prefer cats`);
}
// ex 3
// let userNumber = prompt("Please enter a number:");
let userNumber = parseFloat(prompt("Please enter a number:"));
if (userNumber % 2 === 0){
    console.log(`${userNumber} is an even number`);
} else {
    console.log(`${userNumber} is an odd number`);
}
// ex 4
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
// const users = [];
if (users.length === 0) {
    console.log("No one is online");
  } else if (users.length === 1) {
    console.log(users[0] + " is online");
  } else if (users.length === 2) {
    console.log(users[0] + " and " + users[1] + " are online");
  } else {
    console.log(users[0] + ", " + users[1] + " and " + (users.length - 2) + " more are online");
  }
  