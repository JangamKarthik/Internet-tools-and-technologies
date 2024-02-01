const colorNames = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown'];

document.addEventListener('DOMContentLoaded', function () {
    const colorText = document.getElementById('colorText');

    colorText.addEventListener('mouseover', changeBackgroundColor);

    function changeBackgroundColor() {
        const randomColor = getRandomColor();
        document.body.style.backgroundColor = randomColor;
    }

    function getRandomColor() {
        const randomIndex = Math.floor(Math.random() * colorNames.length);
        return colorNames[randomIndex];
    }
});