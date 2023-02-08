# Computer Vision RPS

This project uses computer vision to play a game of rock-paper-scissors. 

A computer vision model is trained through the use of Teachable Machine, to recognise a human hand in manipulated into postions representative, of rock, paper or scissors. This model is used to compete with a computer in this game

The model consists of four classes:

1. Rock
2. Paper
3. Scissors
4. Nothing

The machine was taught to recognise different selections, through the use of a series of images taken for each class,

for Rock, a clenched fist was held up to the webcam and rotated to capture the representation of the rock option
for Paper, an open palm was held to the camera to capture the selection of paper 
for Scissors, the first two fingers were presented to the camera to represent the scissors option
for nothing, no expression of the hands were presented to the camera, this is a representation of no repsonse in a game of rock-paper-scissors.

# Enviroment requirements

The envrioment used to run this game can be found here:

https://github.com/Ne24/computer-vision-rock-paper-scissors/blob/5535af68eac4fe5bd74959473ad654aa0a907f06/requirements.txt

# Code

# import the random module

## get_computer_choice function

Using the imported random module, this function randomly selects an option out of rock, paper and scissors.

## get_user_choice function

This function accepts input from the user.

## get_winner function

This function compares the choices from the computer and user to determine who wins the game or whether the round results in a tie.

## play function

This function initialises both the computer and user scores to 0,
it calls the get_computer_choice function then the predicition_certainty fucntion, and assigns the values to computer_choice and user_input respectively

If the computer wins a round it's score is increased by one, this is the same if the user wins a round, the first to pass 2 wins is the winner of the competiton. 

```python
def play():
    """Play the rock-paper-scissors game"""
    computer_wins = 0
    user_wins = 0

    while True:

        computer_choice = get_computer_choice()
        user_input =  prediction_certanity()
        game = get_winner(computer_choice,user_input)

        print(f"Computer choice {computer_choice}. User choice {user_input}")

        computer_wins += game[0]
        user_wins += game[1]

        if computer_wins > 2 or user_wins > 2:
            break


    if user_wins > computer_wins:
        print(f"""
        User wins this compettiton
        final score: User: {user_wins} , Computer {computer_wins}
        """)
    else:
        print(f"""
        Computer wins this competition
        final score: Computer:{computer_wins}, User: {user_wins} 
        """)



play()
```

## Game-model-integration

The model is utilised in the get_prediction function, which uses the load_model function from the keras.models module
to load the keras model created in teachable machine. The model is trained on user hand gestures which are used inputs for rock-paper-scissors game.
The webcam is then initalised and the user input (hand gestures or lacktherof) are captured and a prediction is made based on the model, on whether the hand gesture is one of the four options. The model returns its prediction of the 3 scenarios and the associated certainty in an array, the entry with highest certainty is selected as the users selection.

## Future improvements

This code program can be further improved by the addition of a feature that  allows for mutliple users to have their own score history against the computer. Currently the game scores are not saved once the game is restarted. This feature would allow the user to save their score, similar to more advanced games and it will allow different players to play on their respective "profiles".

