# import io
# import random
# import picamera
# from PIL import Image

# prior_image = None
# motion_count = 0
# motion_try = False
# current_image = None

# def detect_motion(camera):
#     global prior_image
#     global motion_try
#     global current_image
#     stream = io.BytesIO()
#     camera.capture(stream, format='jpeg', use_video_port=True)
#     stream.seek(0) 
#     print(current_image, "current_image")
#     print(prior_image, "prior_image")
#     if prior_image == None:
#         prior_image = Image.open(stream)
#         return False
#     else:
#         if motion_try == True:
#             current_image = Image.open(stream)
#         # result = random.randint(0, 10) == 0
#         # prior_image = current_image
#         # return result
#         if prior_image is current_image:
#             return False
#         else:
#             prior_image = current_image
#             motion_try = True
#             return True


# # class recording(object):
# #     def __init__(self):
# #         self.size = 0

# #     def write(self, s):
# #         self.size += len(s)

# #     def flush(self):
# #         print('flushing bytes', self.size)

# with picamera.PiCamera() as camera:
#     camera.resolution = (1280, 720)
#     stream = picamera.PiCameraCircularIO(camera, seconds=5)
#     camera.start_recording(stream, format="h264")
#     try:
#         while True:
#             camera.wait_recording(1)
#             if detect_motion(camera):
#                 motion_count += 1
#                 print("Motion detected!", motion_count)
#                 #once motion is detected, split the recording into two to record the frames after motion for comparison
#                 camera.split_recording("after.h264")
#                 #include ten seconds before motion for comparison as well
#                 stream.copy_to('before.h264', seconds=5)
#                 stream.clear()
#                 #wait until there is no more motion, then split the recording back
#                 # while detect_motion(camera):
#                 #     camera.wait_recording(1)
#                 #     print("Still Recording", motion_count)
#                 print("No more motion!")
#                 camera.split_recording(stream)

#     finally:
#         camera.stop_recording()
#         print("camera stopped")

# import io
# import random
# import picamera
# from PIL import Image

# prior_image = None

# def detect_motion(camera):
#     global prior_image
#     stream = io.BytesIO()
#     camera.capture(stream, format='jpeg', use_video_port=True)
#     stream.seek(0)
#     if prior_image is None:
#         prior_image = Image.open(stream)
#         return False
#     else:
#         current_image = Image.open(stream)
#         # Compare current_image to prior_image to detect motion. This is
#         # left as an exercise for the reader!
#         result = None
#         if current_image is prior_image:
#             result = False
#         else:
#             result = True
#             prior_image = current_image
#         # Once motion detection is done, make the prior image the current
#         return result

# with picamera.PiCamera() as camera:
#     camera.resolution = (1280, 720)
#     stream = picamera.PiCameraCircularIO(camera, seconds=10)
#     camera.start_recording(stream, format='h264')
#     try:
#         while True:
#             camera.wait_recording(1)
#             if detect_motion(camera):
#                 print('Motion detected!')
#                 # As soon as we detect motion, split the recording to
#                 # record the frames "after" motion
#                 camera.split_recording('after.h264')
#                 # Write the 10 seconds "before" motion to disk as well
#                 stream.copy_to('before.h264', seconds=10)
#                 stream.clear()
#                 # Wait until motion is no longer detected, then split
#                 # recording back to the in-memory circular buffer
#                 while detect_motion(camera):
#                     camera.wait_recording(1)
#                 print('Motion stopped!')
#                 camera.split_recording(stream)
#     finally:
#         camera.stop_recording()

import os
import picamera
import numpy as np
from picamera.array import PiMotionAnalysis
import subprocess
import keyboard
from time import sleep

# A simple demo of sub-classing PiMotionAnalysis to construct a motion detector

MOTION_MAGNITUDE = 100   # the magnitude of vectors required for motion
MOTION_VECTORS = 20     # the number of vectors required to detect motion
motion = 0

class MyMotionDetector(PiMotionAnalysis):
    def analyse(self, a):
        global motion
        # Calculate the magnitude of all vectors with pythagoras' theorem
        a = np.sqrt(
            np.square(a['x'].astype(np.float)) +
            np.square(a['y'].astype(np.float))
            ).clip(0, 255).astype(np.uint8)
        # Count the number of vectors with a magnitude greater than our
        # threshold
        vector_count = (a > MOTION_MAGNITUDE).sum()
        if vector_count > MOTION_VECTORS:
            print('Detected motion!')
            motion = 0
        else:
            print('No motion!', motion)
            motion += 1

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    with MyMotionDetector(camera) as motion_detector:
        camera.start_recording(
            os.devnull, format='h264', motion_output=motion_detector)
        try:
            while True:
                camera.wait_recording(1)
                if motion > 6000:
                    break
        finally:
            camera.stop_recording()
            camera.close()