// ex 1
// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by youself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

let i = 0;
let stars = '';
for (; i <= 5; i++) {
    stars = stars + " " + '*';
    console.log(stars);
}
console.log("\n")

for (let k = 1; k <= 6; k++) {
    let row = "";
    for (let j = 1; j <= k; j++) {
        row += "* ";
    }
    console.log(row);
}





