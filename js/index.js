function createDisplay() {
    for (let i = 0; i < WORD_LENGTH; i ++) {
        new wordRow()
    }
}

function newGuess() {
    if (! correctWord(inputBox.value)) {return}
    
    let guess = inputBox.value
    console.log(guess)
    setNextWord(guess)


    inputBox.value = ""
}

function displayError(type) {
    errorBox.style.display = "flex"

    if (typeof(type) == "string") {
        errorMessage.innerHTML = type
        return
    }
    
    errorMessage.innerHTML = "Unknown Error Occurred"
}

$('#submitButton').click((e) => {
    e.preventDefault()
    newGuess()
})

function correctWord(word) {
    if (word.length != WORD_LENGTH) {
        displayError("Word not at the right length - " + WORD_LENGTH)
        return false
    }

    for (let i = 0; i < word.length; i++) {
        let letter = word[i]
        if (! acceptableCharacters.includes(letter.toLowerCase())) {
            displayError("Word contains illegal character: " + letter)
            return false
        }
    }

    return true
}


function setNextWord(word) {
    for (let i = 0; i < wordRows.length; i++) {
        if (wordRows[i].object.displayUsed != true) {
            wordRows[i].object.setWord(word)
            return
        }
    }
}



createDisplay()