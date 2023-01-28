// ex 1
// Instructions
// Part I : function with no parameters
// Create a function called infoAboutMe() that takes no parameter.
// The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// Call the function.

function infoAboutMe() {
    console.log("My name is Anna, I am a 24y.o. My hobbie is coding.");
}

infoAboutMe();


// Part II : function with three parameters
// Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// Call the function twice with the following arguments:
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`Your name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}.`);
}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");


// ex 2
// Instructions
// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.
// Create a function named calculateTip() that takes no parameter.
// Inside the function, use prompt to ask John for the amount of the bill.
// Here are the rules
// If the bill is less than $50, tip 20%.
// If the bill is between $50 and $200, tip 15%.
// If the bill is more than $200, tip 10%.
// Console.log the tip amount and the final bill (bill + tip).
// Call the calculateTip() function.

function calculateTip(){
    var bill = parseFloat(prompt("Please enter the amount of the bill:"));
    var tip = parseFloat();
    if (bill < 50) {
        tip = bill * 0.2;
    } else if (bill >= 50 && bill <= 200) {
        tip = bill * 0.15;
    } else {
        tip = bill * 0.1;
    }
    
    console.log(`The tip amount is $ ${tip}`);
    console.log(`The final bill is $ ${bill + tip}`);
}
calculateTip();


// ex 3
// Instructions
// Create a function call isDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.
// Bonus: Add a parameter divisor to the function.

function isDivisible(divisor){
    var sum = 0;
    for (var i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            console.log(i);
            sum += i;
        }
    }
    console.log(`The sum of all numbers divisible by ${divisor} is ${sum}`);

}
isDivisible(10);


// ex 4
// Add the stock and prices objects to your js file.
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
// Create a function called myBill() that takes no parameters.
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1


const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
shoppingList = ["banana", "orange", "apple"];

function myBill(){
    let total = 0;
    for (let i = 0; i < shoppingList.length; i++) {
        let item = shoppingList[i];
        if (item in stock){
            if (stock[item] > 0){
                total += prices[item];
                stock[item]--;
            } else {
                console.log(`${item} is out of stock. You cannot buy it`)
            }
        } else {
            console.log(`${item} is not available.`)
        }
    }
    return total;
}

console.log("Total bill is $" + myBill());



// ex 5
// Instructions
// Note: Read the illustration (point 4), while reading the instructions
// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// an item price
// and an array representing the amount of change in your pocket.
// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false
// Change will always be represented in the following order: quarters, dimes, nickels, pennies
// To illustrate:
// After you created the function, invoke it like this:
// The value 4.25 represents the item’s price
// The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
// The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due

// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01
//changeEnough(4.25, [25, 20, 5, 0])

function changeEnough(itemPrice, amountOfChange){
    let quarters = amountOfChange[0];
    let dimes = amountOfChange[1];
    let nickels = amountOfChange[2];
    let pennies = amountOfChange[3];
    let amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01);
    if(amount >= itemPrice){
        return true;
    }else{
        return false;
    }
}
console.log(changeEnough(14.11, [2,100,0,0])); 
console.log(changeEnough(0.75, [0,0,20,5]));

// ex 6
// Let’s create functions that calculate your vacation’s costs:
// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.
// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$
// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.
// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().
// Call the function totalVacationCost()
// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.

// function hotelCost(){
//     var night = prompt('How many nights?');
//     if(isNaN(night) || night === ''){
//         night = prompt('Please, enter a valid number.');
//     }
//     return night * 140;
// }

// function planeRideCost() {
//     var place = prompt('Please write your destination:');
//     if(typeof place !== "string" || place === ''){
//         place = prompt('Please enter a valid destination:');
//     }
//     // use swith to check destination
//     switch (place){
//         case "London":
//             return 183;
//         case "Paris":
//             return 220;
//         default:
//             return 300;
//     }
// }

// function rentalCarCost(){
//     var days = prompt('How many days?');
//     var carCost = 40;
//     if(isNaN(days) || days === ''){
//         days = prompt('Please, enter a valid number.');
//     }
//     if (days > 10){
//         carCost = carCost - (carCost * 0.5)
//     }
//     return carCost;
// }

// function totalVacationCost(){
//     let hotelCostSum = hotelCost();
//     let planeCost = planeRideCost();
//     let carCostSum = rentalCarCost();
//     return `The hotel cost $ ${hotelCostSum}, the car cost $ ${carCostSum} and the ride cost $ ${planeCost}`
// }
// console.log(totalVacationCost());

// BONUS

function hotelCost(nights) {
    if (!nights || isNaN(nights)) {
      return 0;
    }
    return nights * 140;
  }
  
  function planeRideCost(place) {
    if (!place || typeof place !== "string") {
      return 0;
    }
    switch (place) {
      case "london":
        return 183;
      case "Paris":
        return 220;
      default:
        return 300;
    }
  }
  
  function rentalCarCost(days) {
    if (!days || isNaN(days)) {
      return 0;
    }
    var carCost = days * 40;
    if (days > 10) {
        carCost = carCost - (carCost * 0.05);
    }
    return carCost;
  }
  
  function totalVacationCost() {
    var nights = prompt("How many nights?");
    var place = prompt("Please write your destination:");
    var days = prompt("How many days?");
    var totalCost = hotelCost(nights) + planeRideCost(place) + rentalCarCost(days);
    return "Total cost of your vacation is $" + totalCost;
  }
  console.log(totalVacationCost())
  