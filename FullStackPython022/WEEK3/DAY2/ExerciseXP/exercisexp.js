// ex1
var favoriteFood = 'cake';
var day = 'dinner';
console.log(`I eat ${favoriteFood} at every ${day}`);

// ex2
    //part1
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
var myWatchedSeriesLength = myWatchedSeries.length;
const myWatchedSeriesSentence = myWatchedSeries.join(", ").replace(/,(?!.*,)/gmi, " and");
console.log(`I watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence}.`);

    //part2
myWatchedSeries.splice(2,2,'friends');
myWatchedSeries.push('breaking bad');
myWatchedSeries.unshift('supernatural');
myWatchedSeries.splice(1,1);
console.log(myWatchedSeries[1].charAt(2));
// delete myWatchedSeries[1];
console.log(myWatchedSeries);

//ex3

var tempIntoC = 25;
var tempIntoF = tempIntoC / 5 * 9 + 32;
console.log( `A ${tempIntoC} °C is ${tempIntoF} °F.`);

//ex 4
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55
// Actual: 55

a = 2;
console.log(a+b) //second expression
// Prediction: 23
// Actual: 23
console.log(3 + 4 + '5');
// Prediction: 75
// Actual: 75

//ex 5
typeof(15)
// Prediction: number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction:number
// Actual:number

typeof("hello")
// Prediction:String
// Actual:String

typeof(true)
// Prediction: boolean
// Actual:boolean

typeof(1 != 2)
// Prediction: boolean
// Actual: boolean

"hamburger" + "s"
// Prediction:hamburgers
// Actual:hamburgers

"hamburgers" - "s"
// Prediction:NaN
// Actual:NaN


"1" + "3"
// Prediction:13
// Actual:13

"1" - "3"
// Prediction:-2
// Actual:-2

"johnny" + 5
// Prediction:johnny5
// Actual:johnny5

"johnny" - 5
// Prediction:NaN
// Actual:NaN

99 * "hello"
// Prediction: NaN
// Actual:NaN

1 != 1
// Prediction: false
// Actual: false

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:false
// Actual:false

//ex 6
5 + "34"
// Prediction:534
// Actual:534

5 - "4"
// Prediction:1
// Actual:1

10 % 5
// Prediction:0
// Actual:0

5 % 10
// Prediction:5
// Actual:5

"Java" + "Script"
// Prediction:JavaScript
// Actual:JavaScript

" " + " "
// Prediction:  
// Actual:  

" " + 0
// Prediction: 0
// Actual: 0

true + true
// Prediction: 2
// Actual:2

true + false
// Prediction:1
// Actual:1

false + true
// Prediction:1
// Actual:1

false - true
// Prediction:-1
// Actual:

!true
// Prediction:false
// Actual:false

3 - 4
// Prediction:-1
// Actual:-1

"Bob" - "bill"
// Prediction:NaN
// Actual:NaN

