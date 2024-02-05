function fib(n) {
    var a = [0, 1];
    var str = "0, 1, ";
    for (var i = 2; i < n; i++) {
        a.push(a[i - 1] + a[i - 2]);
        str += a[i].toString() + ", ";
    }
    document.getElementById("display").textContent = "Fibonacci Sequence: " + str;
}

function sq(n) {
    var str = "Number    Square\n";
    for (var i = 1; i <= n; i++) {
        var squares = i * i;
        str += i.toString() + "              " + squares.toString() + "\n";
    }
    document.getElementById("display").textContent = "Square Table:\n" + str;
}

function table() {
    var value = prompt("Enter n", "5");
    sq(Number(value));
}

function fibonacci() {
    var value = prompt("Enter n", "5");
    fib(Number(value));
}
