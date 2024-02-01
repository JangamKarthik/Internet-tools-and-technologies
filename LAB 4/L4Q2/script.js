function findLeftMostVowelPosition(str) {
    var vowels = "aeiouAEIOU";
    for (var i = 0; i < str.length; i++) {
        if (vowels.indexOf(str[i]) !== -1) {
            return i + 1;
        }
    }
    return -1;
}

function reverseNumberDigits(num) {
    var reversedNum = parseInt(num.toString().split("").reverse().join(""), 10);
    return reversedNum;
}
