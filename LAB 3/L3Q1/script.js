document.addEventListener("DOMContentLoaded", function () {
    const textContainer = document.getElementById("textContainer");
    let fontSize = 20;
    let growing = true;

    function animateText() {
        if (growing) {
            fontSize += 2;
            textContainer.style.fontSize = `${fontSize}pt`;

            if (fontSize >= 50) {
                growing = false;
                textContainer.innerHTML = "TEXT-SHRINKING";
                textContainer.style.color = "blue";
            }
        } else {
            fontSize -= 2;
            textContainer.style.fontSize = `${fontSize}pt`;

            if (fontSize <= 5) {
                textContainer.innerHTML = "TEXT-GROWING";
                textContainer.style.color = "red";
                growing = true;
            }
        }

        setTimeout(animateText, 100);
    }

    animateText();
});
