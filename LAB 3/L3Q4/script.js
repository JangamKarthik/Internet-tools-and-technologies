function generateThreeLetterWords() {
    var fiveLetterWordInput = document.getElementById("fiveLetterWordInput").value;
    var generatedWords = generateWords(fiveLetterWordInput);

    document.getElementById("outputTextArea").value = generatedWords.join("\n");
}

function generateWords(fiveLetterWord) {
    var threeLetterWords = [];

    if (fiveLetterWord.length === 5) {
        for (var i = 0; i < 5; i++) {
            for (var j = 0; j < 5; j++) {
                for (var k = 0; k < 5; k++) {
                    if (i !== j && j !== k && i !== k) {
                        var word = fiveLetterWord[i] + fiveLetterWord[j] + fiveLetterWord[k];
                        threeLetterWords.push(word);
                    }
                }
            }
        }
    }

    return threeLetterWords;
}

function clearInputAndOutput() {
    document.getElementById("fiveLetterWordInput").value = "";
    document.getElementById("outputTextArea").value = "";
}
