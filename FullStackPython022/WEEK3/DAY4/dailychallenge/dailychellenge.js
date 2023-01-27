// Instructions
// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.
// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).
// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).
// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.
// ex 1
// var sentence = "The movie is not that bad, I like it";
var sentence = "This dinner is not that bad ! You cook well";
// var sentence = "This dinner is bad";
var wordNot = sentence.indexOf("not");
var wordBad = sentence.indexOf("bad");
var newSentence = sentence.replace("not that bad", "good");
if (wordNot < wordBad){
    console.log(newSentence);
} else {
    console.log(sentence);
}
