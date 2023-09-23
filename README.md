# Set Up

To install requirenments:

pip install -r requirements.txt

# Instructions:
## Load Questions:
1. Read the CSV file and load questions into a suitable data structure (like a list or dictionary).
2. Shuffle the questions to ensure a different order every time the quiz is taken.

## Quiz Interaction:
1. Prompt the user to start the quiz. Ask what level of difficulty they want. The difficulty is measured by the $ value of the question (as they are jeopardy questions). Easy is 200-400. Medium is 400-700. Hard is 700-1000. Extra hard is question that are labeled as "Final Jeopardy!". Ask how long the quiz should be. Minimum of 3 questions, maximum of 30.
2. Use ChatGPT to ask the questions to the user.
3. Have the user first answer the question as a free response (no multiple choice)
4. If the free response answer is incorrect: Use ChatGPT to generate 4 total multiple choice answers given the answer in the CSV (meaning 1 of the four is the answer directly from the csv, the other 3 are chatgpt generated. They should look like the answer in the CSV to not give away that the other answers are AI generated). User must choose the correct one answer.
5. Collect the user’s response and compare it to the correct answer from your data structure using ChatGPT.
6. Keep score of correct and incorrect answers.
7. After the game is over, ask user if they want to play again or to exit

## Scoring & Feedback:
1. After the quiz ends, calculate the final score and % correct. 
2. Use ChatGPT to generate a customized message based on the user’s performance.

# Reward:
A large bowl of pho and a ticket to Oppenheimer
