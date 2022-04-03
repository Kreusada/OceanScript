function toggleLighting(mode) {
    document.body.classList = mode;
}

function copyToClipboard() {
    var copyText = document.getElementById("output").value;
    if (copyText === "[...]") {
        alert("No oceanscript to copy!")
    }
    else {
        navigator.clipboard.writeText(copyText);
    }
}

function randomChoice(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

function fillWithRandomPhrase() {
    var choice = randomChoice(PLACEHOLDER_COLLECTION);
    document.getElementById("input").value = choice;
    document.getElementById("output").value = encode(choice);
}

function clearTextAreas() {
    var input = document.getElementById("input");
    var output = document.getElementById("output");
    // if (output.value === "[...]") {
    //     alert("No text to clear!");
    // }
    // else {
    //     input.value = "";
    //     output.value = "[...]";
    // }
    // the above is now managed by the checkButtons
    // function which disables the buttons
    input.value = "";
    output.value = "[...]";
}

const PLACEHOLDER_COLLECTION = [
    "The bewildered tourist was lost.",
    "The flu clinic had seen many cases of infectious disease.",
    "It was a story as old as time.",
    "The sports car drove the long and winding road.",
    "Saturday became a cool, wet afternoon.",
    "He was waiting for the rain to stop.",
    "She was upset when it didn't boil.",
    "You have been sleeping for a long time.",
    "You might enjoy a massage.",
    "He was eager to eat dinner.",
]

function checkButtons() {
    if ($("#input").val().length === 0) {
        $("#copyClipboard").attr("disabled", "disabled");
        $("#clearTextAreas").attr("disabled", "disabled");
    }
    else {
        $("#copyClipboard").removeAttr("disabled");
        $("#clearTextAreas").removeAttr("disabled");
    }
}

setInterval(checkButtons, 500)
