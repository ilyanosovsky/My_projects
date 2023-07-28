// In the JS file, create a function called playTheGame() that takes no parameter.
// In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).

// If the answer is false, alert “No problem, Goodbye”.

// If his answer is true, follow these steps:
// Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). You then have to check the validity of the user’s number :

// If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
// If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.
// Else (ie. he entered a number between 0 and 10), create a variable named computerNumber where the 
// value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function). Make sure that the number is rounded.

function playTheGame() {
    let play = confirm("Would you like to play the game?");
    if (play === false) {
        alert("No problem, Goodbye");
    } else {
        let userNumber = prompt("Enter a number between 0 and 10");
        if (isNaN(userNumber)) {
            alert("Sorry Not a number, Goodbye");
        } else if (userNumber < 0 || userNumber > 10) {
            alert("Sorry it's not a good number, Goodbye");
        } else {
            let computerNumber = Math.floor(Math.random() * 11);
            console.log(computerNumber);
            compareNumbers(userNumber, computerNumber);
        }
    } 
} 

// Outside of the playTheGame() function, create a new function named compareNumbers(userNumber,computerNumber)
//  that takes 2 parameters : userNumber and computerNumber

// The point of this function is to check if the userNumber is the same as the computerNumber:
// If userNumber is equal to computerNumber, alert “WINNER” and stop the game.

// If userNumber is bigger than computerNumber, alert “Your number is bigger then the computer’s, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

// If userNumber is lower than computerNumber, alert “Your number is smaller then the computer’s, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

// If the user guessed more than 3 times, alert “out of chances” and exit the function.

function compareNumbers(userNumber, computerNumber, attempts = 0) {
    if (attempts >= 3) {
      alert("Out of chances");
      return; // Exit the function
    }
  
    
    if (userNumber > computerNumber) {
      alert("Your number is bigger than the computer's, guess again");
      userNumber = prompt("Enter a number between 0 and 10");
      compareNumbers(userNumber, computerNumber, attempts + 1);
    } else if (userNumber < computerNumber) {
      alert("Your number is smaller than the computer's, guess again");
      userNumber = prompt("Enter a number between 0 and 10");
      compareNumbers(userNumber, computerNumber, attempts + 1);
    } else { (userNumber === computerNumber)
      alert("WINNER");
    }

}


// Call the playTheGame() function to start the game.
