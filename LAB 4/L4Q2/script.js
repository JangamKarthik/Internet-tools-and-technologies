function leftvowel() {
    var txt = document.getElementById("input").value;
    var str = "aeiou";
    var pos = -1;
    for (var i = 0; i < 5; i++) {
        var a = txt.indexOf(str.charAt(i));
        if (a == -1) {
            continue;
        } else if (pos == -1)
            pos = a;
        else if (pos > a)
            pos = a;
    }
    document.getElementById("output").textContent = "Left Most Vowel Position: " + pos.toString();
}

function reverse() {
    var txt = document.getElementById("input").value;
    var reversedString = "";
    for (var i = 0; i < txt.length; i++) {
        reversedString = txt.charAt(i) + reversedString;
    }
    document.getElementById("output").textContent = "Reversed String: " + reversedString;
}
