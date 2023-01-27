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
