""""""
import time
import random
import cv2
from keras.models import load_model
import numpy as np
#import manual_rps

def get_computer_choice():
    """Function gets a random choice out of rock, paper, scissors for the computer"""
    choice_list = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(choice_list)
    # computer_choice = computer_choice.lower()
    return computer_choice

def get_winner(computer_choice, user_choice):
    """Determines the winner of the rock-paper-scissors game """
    computer_wins = 0
    user_wins = 0

    if computer_choice == user_choice:
        print("It is a tie!")
    elif computer_choice == "Rock" and user_choice == "Scissors":
        print("You lost")
        computer_wins +=1
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("You lost")
        computer_wins +=1
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("You lost")
        computer_wins +=1
    else:
        print("You won!")
        user_wins +=1
    return computer_wins ,user_wins



STARTTIME = time.time()

def get_prediction():
    """Gets prediction of the keras model for user hand gestures"""

    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time.time() - STARTTIME > 3:
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction

def prediction_certanity():
    """Picks the highest confidence rating of model-predicted user
    hand gesture as user selection from list
    """
    prediction_list = get_prediction()

    if prediction_list[0][0] > (prediction_list[0][1] or prediction_list[0][2]):
        user_input = "Rock"
        print("you chose rock")
    elif prediction_list[0][1] > (prediction_list[0][0] or prediction_list[0][2]):
        user_input = "Paper"
        print("you chose paper")
    elif prediction_list[0][0] > (prediction_list[0][1] or prediction_list[0][2]):
        user_input = "Scissors"
        print("you chose scissors")
    else:
        print("inconclusive input")

    return user_input

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
