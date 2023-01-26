//ex 1
const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.splice(0,1);
console.log(fruits);
//
fruits.sort();
console.log(fruits);
//
fruits.push('Kiwi');
console.log(fruits);
//
const filteredFruits = fruits.filter(fruit => fruit !== "Apples");
console.log(filteredFruits); 
//
fruits.reverse();
console.log(fruits);

// ex 2
// const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// console.log(moreFruits[1][1][0]);
//
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
const checkArray = moreFruits[1];
const checkArray2 = checkArray[1];
console.log(checkArray2[0]);