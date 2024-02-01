let display = document.getElementById('display');
let currentInput = '';
let currentOperation = '';
let isDecimalAdded = false;

function appendNumber(number) {
    currentInput += number;
    updateDisplay();
}

function appendDecimal() {
    if (!isDecimalAdded) {
        currentInput += '.';
        isDecimalAdded = true;
        updateDisplay();
    }
}

function operate(operation) {
    if (currentInput !== '') {
        currentOperation = operation;
        currentInput += operation;
        isDecimalAdded = false;
        updateDisplay();
    }
}

function calculate() {
    try {
        let result = eval(currentInput);
        display.value = result;
        currentInput = result.toString();
        currentOperation = '';
        isDecimalAdded = false;
    } catch (error) {
        display.value = 'Error';
    }
}

function clearDisplay() {
    display.value = '';
    currentInput = '';
    currentOperation = '';
    isDecimalAdded = false;
}

function backspace() {
    currentInput = currentInput.slice(0, -1);
    updateDisplay();
}

function updateDisplay() {
    display.value = currentInput;
}

