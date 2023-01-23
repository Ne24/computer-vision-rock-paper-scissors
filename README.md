# Computer Vision RPS

This project uses computer vision to play a game of rock-paper-scissors. 

A computer vision model is trained through the use of Teachable Machine, to recognise a human hand in manipulated into postions representative, of rock, paper and scissors. This is used to compete with a computer in this game

It consists of four classes:

1. Rock
2. Paper
3. Scissors
4. Nothing

The machine was taught to recognise different selections, through the use of a series of images taken for each class,

for Rock, a clenched fist was held up to the webcam and rotated to capture the representation of the rock option
for Paper an open palm was held to the camera to capture the selection of paper 
for Scissors the first two fingers were presented to the camera to represent the scissors option
for nothing no expression of the hands were presented to the camera, this is a representation of no repsonse in a game of rock-paper-scissors

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

This function compares the choices from the computer and user to determine who wins the game or whether it results in a tie.

## play function

This fucntion calls get_computer_choice function then get_user_choice function and assigns the returned values to computer_choice and user_choice respectively
this is then passed into the get_winner function to run compare the choices

```python
def play():
    """Play the rock-paper-scissors game"""

    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice,user_choice)

# plays the rock-paper-scissors game 
play()
```


