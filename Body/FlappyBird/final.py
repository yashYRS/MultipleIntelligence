import time
import dlib
import cv2
import numpy as np
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from classes.flappy_bird_classes import draw, one_game_run
from classes.flappy_bird_classes import width, height, hand_pos, hand_convex_number
from classes.hand_detect import detect_hand


def game_loop():
    # True, if hand gets detected
    track_flag = False
    # dlib correlation tracker initialisation
    tracker = dlib.correlation_tracker()
    # capture the video using opencv video capture
    cap = cv2.VideoCapture(0)
    start_time, end_time = 0, 0

    hand_to_detect = True
    while cap.isOpened() and hand_to_detect:
        # read the frame from webcam
        ret, img = cap.read()
        # img = cv2.flip(img,1)
        if track_flag is False:
            count_defects = detect_hand(img, hand_pos)
            if count_defects > hand_convex_number:
                cv2.destroyAllWindows()
                detect_hand.open_window_flag = False
                hand_to_detect = False
                tracker.start_track(img, dlib.rectangle(hand_pos[0], hand_pos[1], hand_pos[2], hand_pos[3]))
                track_flag = True
                pos = tracker.get_position()
                track_pos_prev = [(pos.left() + pos.right()) / 2., (pos.top() + pos.bottom()) / 2.]
                # we start the game if there is a hand detected
                start_time = time.time()
                try:
                    one_game_run(cap, tracker, track_pos_prev)
                except Exception as e:
                    pass
                end_time = time.time()
                return end_time - start_time


        k = cv2.waitKey(1)
        if k == 27:
            break
    return start_time - end_time


def start_game():
    # print("STARTED- ")
    try:
        time_elapsed = game_loop()
    except Exception as e:
        time_elapsed = 1
    score = time_elapsed/25

    if score > 0.95:
        score = 0.95

    return score


if __name__ == "__main__":
    returned_value = start_game()
    print("RETURNED - ", returned_value)
