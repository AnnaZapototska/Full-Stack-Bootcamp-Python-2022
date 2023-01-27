// Remove Banana from the array.
// Sort the array in alphabetical order.
// Add “Kiwi” to the end of the array.
// Remove “Apples” from the array. Don’t use the same method as in part 1.
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
// At the end you should see this outcome:



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
// Access and then console.log “Oranges”.
// const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// console.log(moreFruits[1][1][0]);
//
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
const checkArray = moreFruits[1];
const checkArray2 = checkArray[1];
console.log(checkArray2[0]);