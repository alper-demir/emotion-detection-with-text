## Installation
Git Repository link: https://github.com/alper-demir/emotion-detection-with-text
1. Clone the project using "git clone", or directly download as a zip file.
2. Create venv file with "py -m venv venv" command in terminal.
3. Activate venv with "./venv/scripts/activate" command in terminal.
4. Install the packages using "pip install -r requirements.txt" command in terminal.
5. As model already has been trained, just use "py app.py" command in terminal to start.
6. Server must be running on port 5000 (localhost:5000) in your browser.
7. Make sure you do these operations in the project's main directory.

## About the game

1. You have a maximum of 3 attempts for each available emotion.
2. When you enter the correct sentence that guesses the emotion, you earn point as your attempt quantity.
3. In first attempt if you write correct sentence you will get 3 points.
4. In your second attempt if you write correct sentence, you will get 2 points.
5. In your last attempt if you write correct sentence you will get 1 point.
6. If in your third attempt you did not write correct sentence there is no point, and it will go next to other emotion. 
7. After each sentence is entered, whether it is correct or incorrect, its percentage distribution among other emotions will be shown.
8. Once all available emotes are finished your total score and a button to play again will be shown.