console.log("HELLO PAPA PLATOON!")
// Your function(s) should go here that will interact with the webpage or DOM



let user_guesses = []

function guessNum() {
    let user_input = parseInt(document.getElementById('guess_num').value)
    document.getElementById('show_num').innerHTML += `${user_input}, `
    runGame(user_input)
}

let global_num

function generateRandNum() {
    global_num = Math.floor(Math.random() * 101)
    console.log(global_num)
}


function runGame(user_input) {
    
    console.log(global_num)
        
    if (user_input === global_num) {
        // alert("You win!")

        
        alert('you win!')
        window.location.href = '/html-number-guessing-game/'

    } else {
        user_guesses.push(user_input)
        document.getElementById('show_num').textContent = user_guesses
        if (user_input < global_num) {

            document.getElementById('guess').innerHTML = user_input
        } else {
            document.getElementById('guess').innerHTML = user_input
        }
    }
}