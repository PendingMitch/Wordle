const container = document.getElementsByClassName("container")[0]
const inputBox = document.getElementById("inputBox")
const errorBox = document.getElementById("errorBox")
const errorMessage = document.getElementById("errorMessage")

const acceptableCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
const WORD_LENGTH = 5