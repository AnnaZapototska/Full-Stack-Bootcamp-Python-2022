// ex 1
// Instructions
// Prompt the user for several words (separated by commas).
// Put the words into an array.
// Console.log the words one per line, in a rectangular frame as seen below.
// Check out the Hints and Requirements below.


function createFrame(){
  const words = prompt('Enter your sentansice');
  let arrayWords = words.split(" ");
  console.log(arrayWords);
  let longestWord = 0;
  for (let i = 0; i< arrayWords.length; i++){
    if(longestWord < arrayWords[i].length){
      longestWord = arrayWords[i].length;
    }
  }

  let ifram = '*'.repeat(longestWord + 4) + '\n';
  for (let i = 0; i < arrayWords.length; i++){
    ifram += '* ' + arrayWords[i] + ' ' + (longestWord + arrayWords[i].length) + '* ' + "\n";
    // ifram += '* ' + arrayWords[i] + ' ' + longestWord + '*\n'
  }

  ifram += "*".repeat(longestWord + 4) + '\n';
  console.log(ifram);

  
}
createFrame();
