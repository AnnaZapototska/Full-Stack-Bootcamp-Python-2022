// ex 1
// Part I - Review About Arrays
// Write code to remove “Greg” from the people array.
// Write code to replace “James” to “Jason”.
// Write code to add your name to the end of the people array.
// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method
// Write code that gives the index of “Foo”. Why does it return -1 ?
// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

const people = ["Greg", "Mary", "Devon", "James"];
people.splice(0,1);
people.splice(2,3,'Jason');
people.push('Anna');
console.log(`Check array ${people}`);
console.log(people.indexOf("Mary"));
console.log(people.slice(1, 4));
console.log(people.indexOf("Foo")); //because this item doesn't exist in the array
var last = people.pop();
console.log(last);

// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.
// Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
// Hint: take a look at the break statement in the lesson.

let len = people.length;
let i = 0;
for (; len > i; i++){
    console.log(people[i]);
    if (people[i] === 'Jason') { 
        break; 
    }
}

// ex 2
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like  “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

const colors = ["black", "blue", "green", "purple"];
let lenColor = colors.length;
let j = 0;
for (; j < lenColor; j++){
    console.log(`My #${j +1} choice is ${colors[j]}`);
}
// 
let suffix = ["st", "nd", "rd", "th", "th"];
for (let p = 0; p < colors.length; p++) {
    console.log(`My ${p + 1}${suffix[p]} choice is ${colors[p]}`);
  }

// ex 3
// Instructions
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

// let userNumber = prompt("Please enter a number:"); //always returne string 
// let number = parseFloat(userNumber); // change type to number
// let type = typeof(number);
// // you need to write number twice 
// if (isNaN(number)) {
//     console.log("Please enter a valid number.");
// } else {
//     let k = 0;
//     do{
//         userNumber = prompt("Please enter a number:");
//         number = parseFloat(userNumber);
//         k ++;
//     }
//     while (number >= 10)
//     console.log(`You entered a number greater than or equal to 10: ${number} `);
// }

// another solution
// let number;
// while (true) {
//     let userInput = prompt("Please enter a number:");
//     number = parseFloat(userInput);
//     if (isNaN(number)) {
//         console.log("Invalid input.");
//     } else if (number >= 10) {
//         console.log(`You entered a number greater than or equal to 10: ${number} `);
//         break;
//     } else {
//         console.log(`You entered a number less than 10: ${number}`);
//     }
// }


// ex 4
// Review About Objects
// Copy and paste the above object to your Javascript file.
// Console.log the number of floors in the building.
// Console.log how many apartments are on the floors 1 and 3.
// Console.log the name of the second tenant and the number of rooms he has in his apartment.
// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(`The number of floors in the building ${building.numberOfFloors}`);
console.log(`Apartments: ${building.numberOfAptByFloor.firstFloor} , ${building.numberOfAptByFloor.thirdFloor}`);
console.log(`The name ${building.nameOfTenants[1]} and number rooms ${building.numberOfRoomsAndRent.dan[0]}`);
//
var sumRent = building.numberOfRoomsAndRent.dan[1] + building.numberOfRoomsAndRent.sarah[1];
console.log(sumRent);
if (sumRent > building.numberOfRoomsAndRent.dan[1]){
  building.numberOfRoomsAndRent.dan[1]= 1200;
   console.log(building.numberOfRoomsAndRent.dan[1]);
}


// ex 5
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

const family = {
    mother: 42,
    father: 49,
    doughter: 12,
    son: 15,
}
console.log("Keys of the object: ");
for (let key in family) {
    console.log(key);
}

console.log("Values of the object: ");
for (let key in family) {
    console.log(family[key]);
}

// ex 6
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  let sentence = "";
  for (let string in details) {
    sentence += string + " " + details[string] + " ";
  }
  console.log(sentence);


// ex 7
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
let secretSociety = "";
for (let a = 0; a < names.length; a++) {
    secretSociety += names[a][0];
}
console.log(secretSociety)

