console.clear();

const inputContainerEl = document.querySelector(".input-container1");

const textInputEl = document.querySelector("input#text1");

const textDisplay1 = document.getElementById("text10")
const textDisplay2 = document.getElementById("text11")
const textDisplay3 = document.getElementById("text12")
const textDisplay4 = document.getElementById("text13")
const textDisplay5 = document.getElementById("text14")

textDisplay1.textContent = "SERIAL NUMBER";
textDisplay2.textContent = "IP ADDRESS";
textDisplay3.textContent = "MAC ADDRESS";
textDisplay4.textContent = "HOST NAME";
textDisplay5.textContent = "Boot TIME";

const suggestionEl = document.querySelector(".suggestion-container1");

const suggestionE2 = document.querySelector(".suggestion-container2");
const suggestionE3 = document.querySelector(".suggestion-container3");
const suggestionE4 = document.querySelector(".suggestion-container4");
const suggestionE5 = document.querySelector(".suggestion-container5");
const suggestionE6 = document.querySelector(".suggestion-container6");

const svgTabIcon = document.querySelector(".icon.tab-key");
const svgEnterIcon = document.querySelector(".icon.enter-key");

const ENTER_KEYCODE = 13;
const TAB_KEYCODE = 9;
const BACKSPACE_KEYCODE = 8;
const UP_ARROW_KEYCODE = 38;
const DOWN_ARROW_KEYCODE = 40;
const SPACE_KEYCODE = 32;

var wordsArray = [];

let suggestedWord = "";
let suggestedWordsArray = [];
let currentWordIndex = 0;
let insertText = false;

function showDefaultTextBox(){
		textDisplay1.textContent = "SERIAL NUMBER";
		textDisplay2.textContent = "IP ADDRESS";
		textDisplay3.textContent = "MAC ADDRESS";
		textDisplay4.textContent = "HOST NAME";
		textDisplay5.textContent = "Boot TIME";

		textDisplay1.style.color = "rgb(118, 111, 111)";
		textDisplay2.style.color = "rgb(118, 111, 111)";
		textDisplay3.style.color = "rgb(118, 111, 111)";
		textDisplay4.style.color = "rgb(118, 111, 111)";
		textDisplay5.style.color = "rgb(118, 111, 111)";
}


textInputEl.addEventListener("input", e => {
	if (e.data != " ") {
		insertText = true;
	}
	if (insertText == false) {
		textInputEl.value = "";
	}

	let inputValue = e.target.value;
	suggestedWordsArray = filterArray(wordsArray, inputValue);
	suggestedWord = suggestedWordsArray[0];

	textDisplay1.style.color = "#1da1f2";
	textDisplay2.style.color = "#1da1f2";
	textDisplay3.style.color = "#1da1f2";
	textDisplay4.style.color = "#1da1f2";
	textDisplay5.style.color = "#1da1f2";

	textDisplay1.textContent = suggestedWord;
	textDisplay2.textContent = suggestedWord;
	textDisplay3.textContent = suggestedWord;
	textDisplay4.textContent = suggestedWord;
	textDisplay5.textContent = suggestedWord;

	if (suggestedWord != undefined) {
		suggestionEl.innerHTML = suggestedWord;
	}

	if (inputValue.length == 0 || suggestedWordsArray.length == 0) {
		suggestionEl.innerHTML = "";
		showDefaultTextBox();
	}

	if (suggestedWordsArray.length != 0) {
		svgTabIcon.classList.remove("hidden");
		svgEnterIcon.classList.add("hidden");
	} else {
		svgTabIcon.classList.add("hidden");
		svgEnterIcon.classList.remove("hidden");
	}

	if (inputValue.length == 0 || inputValue == suggestedWord) {
		svgTabIcon.classList.add("hidden");
		svgEnterIcon.classList.add("hidden");
	}

	if (textInputEl.value.length == 0) {
		insertText = false;
		showDefaultTextBox();
	}
});

textInputEl.addEventListener("keydown", e => {
	if (e.keyCode == ENTER_KEYCODE) {
		textDisplay1.style.color = "rgb(118, 111, 111)";
		textDisplay2.style.color = "rgb(118, 111, 111)";
		textDisplay3.style.color = "rgb(118, 111, 111)";
		textDisplay4.style.color = "rgb(118, 111, 111)";
		textDisplay5.style.color = "rgb(118, 111, 111)";
		if (textInputEl.value.length == 0) return;
		let inputValue = textInputEl.value;
		let words = inputValue.split(" ");
		for (let i in words) {
			if (words[i].length != 0) {
				wordsArray.push(words[i]);
				textInputEl.value = "";
				suggestionEl.innerHTML = "";
			}
		}
		wordsArray = removeDuplicatesFromArray(wordsArray);
		inputContainerEl.classList.add("animate");
		svgTabIcon.classList.add("hidden");
		svgEnterIcon.classList.add("hidden");
		removeClassAfterAnimationCompletes(inputContainerEl, "animate");
	}

	if (textInputEl.value.length != 0) {
		if (e.keyCode == UP_ARROW_KEYCODE) {
			if (currentWordIndex == 0) return;
			currentWordIndex--;
			suggestionEl.innerHTML = suggestedWordsArray[currentWordIndex];
		}

		if (e.keyCode == DOWN_ARROW_KEYCODE) {
			if (currentWordIndex == suggestedWordsArray.length - 1) return;
			currentWordIndex++;
			suggestionEl.innerHTML = suggestedWordsArray[currentWordIndex];
		}

		if (e.keyCode == BACKSPACE_KEYCODE) {
			currentWordIndex = 0;
		}
	}

	if (suggestedWord != undefined && suggestedWord != "") {
		if (e.keyCode == TAB_KEYCODE) {
			textDisplay1.style.color = "rgb(118, 111, 111)";
			textDisplay2.style.color = "rgb(118, 111, 111)";
			textDisplay3.style.color = "rgb(118, 111, 111)";
			textDisplay4.style.color = "rgb(118, 111, 111)";
			textDisplay5.style.color = "rgb(118, 111, 111)";
			e.preventDefault();
			textInputEl.value = suggestedWordsArray[currentWordIndex];
			suggestionEl.innerHTML = "";
			svgTabIcon.classList.add("hidden");
			svgEnterIcon.classList.add("hidden");
		}
	}
});

removeClassAfterAnimationCompletes(inputContainerEl, "animate");

function removeClassAfterAnimationCompletes(el, className) {
	let elStyles = window.getComputedStyle(inputContainerEl);
	setTimeout(function() {
		el.classList.remove(className);
	}, +elStyles.animationDuration.replace("s", "") * 1000);
}

function filterArray(array, item, reverse = true) {
	if (reverse) {
		return array
			.filter(word => compareTwoStrings(word, item))
			.sort((a, b) => a.length - b.length);
	} else {
		return array
			.filter(word => compareTwoStrings(word, item))
			.sort((a, b) => b.length - a.length);
	}
}

function removeDuplicatesFromArray(array) {
	return [...new Set(array.map(i => i))];
}

function compareTwoStrings(string, subString) {
	let temp = string.split("", subString.length).join("");
	if (subString == temp) return subString;
}
        // Code to close the batch file and local server
        window.addEventListener("beforeunload", () => {
            const xhr = new XMLHttpRequest();
            xhr.open("GET", "./close-server");
            xhr.send();
        });

        // Code to terminate batch file and local server when tab is closed
        window.addEventListener("unload", () => {
            const xhr = new XMLHttpRequest();
            xhr.open("GET", "./terminate-server");
            xhr.send();
        });