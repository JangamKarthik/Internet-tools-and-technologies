function generateFibonacci(n) {
    var fibSeries = [];
    for (var i = 0; i < n; i++) {
        fibSeries.push(fibonacci(i));
    }
    document.body.innerHTML += "<h2>Fibonacci Series (First " + n + " Numbers)</h2>";
    document.body.innerHTML += "Fibonacci Series: " + fibSeries.join(", ") + "<br/><br/>";
}

function fibonacci(num) {
    if (num <= 1) return num;
    return fibonacci(num - 1) + fibonacci(num - 2);
}

function generateTableOfSquares(n) {
    var tableContent = "<h2>Table of Numbers and Their Squares (1 to " + n + ")</h2>";
    tableContent += "<table border='1'>";
    tableContent += "<tr><th>Number</th><th>Square</th></tr>";
    for (var i = 1; i <= n; i++) {
        tableContent += "<tr><td>" + i + "</td><td>" + (i * i) + "</td></tr>";
    }
    tableContent += "</table>";
    document.body.innerHTML += tableContent;
}
