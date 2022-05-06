currentWord = "NONES"

wordRows = []
class wordRow {

    constructor () {
        this.displayUsed = false
        this.letters = []

        let div = document.createElement('div');
        div.classList.add("word")
        for (let i = 0; i < 5; i++) {
            this.letters.push(new letterDisplay(div))
        }
        container.appendChild(div)

        wordRows.push({object: this})
    }

    setWord(word) {
        for (let i = 0; i < this.letters.length; i++) {
            this.setLetter(word[i], i)
        }

        this.displayUsed = true
    }

    setLetter(letter = "", id) {
        this.letters[id].setDisplay(letter, id)
    }
}

class letterDisplay {
    constructor (container, defaultDisplay = "") {
        let letter = document.createElement('div');
        letter.classList.add("letter")
        letter.innerHTML = defaultDisplay
        container.appendChild(letter)

        this.letter = letter
    }

    setDisplay(letter, id) {
        this.letter.innerHTML = letter.toUpperCase()

        if (currentWord[id].toUpperCase() == letter.toUpperCase()) {
            this.letter.classList.add("correctLetter")
        } else if (currentWord.toUpperCase().includes(letter.toUpperCase())) {
            this.letter.classList.add("half-correctLetter")
        }

    }
}