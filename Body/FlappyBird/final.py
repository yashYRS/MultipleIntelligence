
import dlib
import cv2
import numpy as np
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from classes.flappy_bird_classes import draw, game, frame
from classes.flappy_bird_classes import width, height, hand_pos, hand_convex_number
from classes.hand_detect import detect_hand

track_flag = False  # track flag indicate whether we have a hand detected and start tracking
tracker = dlib.correlation_tracker()  # dlib correlation tracker initialisation

cap = cv2.VideoCapture(0)   # capture the video using opencv video capture

hand_to_detect = True 
while cap.isOpened() and hand_to_detect:
    ret, img = cap.read() #read the frame from webcam
    #img = cv2.flip(img,1) 
    if not track_flag:
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
            game.start(cap, tracker, track_pos_prev)
            frame.start()
            break 
 
    k = cv2.waitKey(1)
    if k == 27:
        break
