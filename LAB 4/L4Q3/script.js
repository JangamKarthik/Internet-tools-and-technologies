function riseToTop(paragraphId) {
    var paragraphs = document.getElementsByClassName('paragraph');

    var targetParagraph;
    for (var i = 0; i < paragraphs.length; i++) {
        if (paragraphs[i].id === paragraphId) {
            targetParagraph = paragraphs[i];
            break;
        }
    }

    targetParagraph.style.zIndex = getMaxZIndex(paragraphs) + 1;

    for (var j = 0; j < paragraphs.length; j++) {
        if (paragraphs[j] !== targetParagraph) {
            paragraphs[j].style.zIndex = paragraphs[j].getAttribute('data-original-zindex');
        }
    }
}

function getMaxZIndex(elements) {
    var maxZIndex = 0;
    for (var i = 0; i < elements.length; i++) {
        var zIndex = parseInt(elements[i].style.zIndex, 10);
        if (!isNaN(zIndex) && zIndex > maxZIndex) {
            maxZIndex = zIndex;
        }
    }
    return maxZIndex;
}

document.addEventListener("DOMContentLoaded", function() {
    var paragraphs = document.getElementsByClassName('paragraph');
    for (var i = 0; i < paragraphs.length; i++) {
        paragraphs[i].setAttribute('data-original-zindex', paragraphs[i].style.zIndex);
    }
});
