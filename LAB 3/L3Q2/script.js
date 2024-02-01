function convertToPigLatin() {
    var inputSentence = document.getElementById("inputSentence").value;
    var pigLatinSentence = encodeToPigLatin(inputSentence);
    displayResult(pigLatinSentence);
}

function encodeToPigLatin(sentence) {
    var words = sentence.split(" ");
    var pigLatinWords = [];

    for (var i = 0; i < words.length; i++) {
        var word = words[i];
        var pigLatinWord = "";

        if (word.length >= 2) {
            pigLatinWord = word.substring(1) + word.charAt(0).toLowerCase() + "ay";
        } else {
            pigLatinWord = word;
        }

        pigLatinWords.push(pigLatinWord);
    }

    return pigLatinWords.join(" ");
}

function displayResult(result) {
    var outputTextArea = document.getElementById("outputTextArea");
    outputTextArea.value += result + "\n";
}

function clearConvertedText() {
    var outputTextArea = document.getElementById("outputTextArea");
    outputTextArea.value = ""; 
}
