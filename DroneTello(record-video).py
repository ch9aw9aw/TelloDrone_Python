import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # créer un objet VideoWrite, recording to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'),30,(width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

    #On doit lancer le recorder dans une thread separe , sinon blocking options ..
    # pour prevenir les frames d'etre ajoute a la video.

recorder = Thread(target=videoRecorder)
recorder.start()

tello.takeoff()
tello.move_up(100)
tello.rotate_counter_clockwise(360)
tello.land()

keepRecording = False
recorder.join()