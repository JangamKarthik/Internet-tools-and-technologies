document.addEventListener("DOMContentLoaded", function() {
    generateTable();
});

function generateTable() {
    var resultTableContainer = document.getElementById("resultTableContainer");
    var table = document.createElement("table");

    var headerRow = table.insertRow(0);
    var headerCell1 = headerRow.insertCell(0);
    var headerCell2 = headerRow.insertCell(1);
    var headerCell3 = headerRow.insertCell(2);
    headerCell1.textContent = "Number";
    headerCell2.textContent = "Square";
    headerCell3.textContent = "Cube";

    for (var i = 0; i <= 10; i++) {
        var row = table.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);

        cell1.textContent = i;
        cell2.textContent = calculateSquare(i);
        cell3.textContent = calculateCube(i);
    }

    resultTableContainer.appendChild(table);
}

function calculateSquare(number) {
    return number * number;
}

function calculateCube(number) {
    return number * number * number;
}

