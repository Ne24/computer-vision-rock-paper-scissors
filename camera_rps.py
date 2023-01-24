""""""
import time
import cv2
from keras.models import load_model
import numpy as np

STARTTIME = time.time()

def get_prediction():
    """Gets prediction of the keras model for user hand gestures"""

    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while time.time() - STARTTIME < 3:
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
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction

## create countdown function and call
# def countdown_prediction():
#     start_time = time.time()

#     while start_time - time.time() < 3:
#         prediction_list = get_prediction()
#     pass
#     return prediction_list

# prediction_list = countdown_prediction()


prediction_list = get_prediction()

if prediction_list[0][0] > (prediction_list[0][1] or prediction_list[0][2]):
    print("you chose rock")
elif prediction_list[0][1] > (prediction_list[0][0] or prediction_list[0][2]):
    print("you chose paper")
elif prediction_list[0][0] > (prediction_list[0][1] or prediction_list[0][2]):
    print("you chose scissors")
else:
    print("inconclusive input")
