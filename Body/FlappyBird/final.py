import time
import dlib
import cv2
import numpy as np
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import flappy_bird_classes as FC
import hand_detect as HD


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
            count_defects = HD.detect_hand(img, FC.hand_pos)
            if count_defects > FC.hand_convex_number:
                cv2.destroyAllWindows()
                HD.detect_hand.open_window_flag = False
                hand_to_detect = False
                tracker.start_track(img, dlib.rectangle(FC.hand_pos[0], FC.hand_pos[1], FC.hand_pos[2], FC.hand_pos[3]))
                track_flag = True
                pos = tracker.get_position()
                track_pos_prev = [(pos.left() + pos.right()) / 2., (pos.top() + pos.bottom()) / 2.]
                # we start the game if there is a hand detected
                start_time = time.time()
                try:
                    FC.one_game_run(cap, tracker, track_pos_prev)
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
