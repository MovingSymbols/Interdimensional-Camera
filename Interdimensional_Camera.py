# Import the necessary libraries
import cv2 # pip install opencv-python
import openai # '$ pip install openai'
import urllib.request # pip install urllib3
import uuid
import time

openai.api_key = "YOUR_API_KEY_HERE"
# YOU NEED AN API KEY FROM OPENAI.COM FOR THIS TO WORK

'''
Inter-Dimensional (or parallel universe, whatever) Camera
rb@failmail.club Dec 2022

This is a camera that takes pictures from an alternate, parallel reality.

The concept here is that this camera that takes photos, but not normal photos.
It takes photos not from the real world, but from a neighboring dimension (or the
next parallel universe over, if you prefer.)

That's why the photos it takes are always... different.  It's not imaging what's in front
of the lens, it's imaging whatever is in front of the lens FROM ONE DIMENSION OVER.

That's also why the viewfinder is just lines. The camera is always seeing across dimensions,
but only dimly.  When you take a photo, it pierces the veil and gets a high-resolution color
shot (of whatever is in the other dimension) instead of just a dim preview.  Beware that
for the brief moment one can see into this other reality, one can also be seen...

Technically, this program will:
1. open an attached webcam
2. Display a preview video feed (filtered through opencv edge detection for the lines effect)
3. Wait for a keypress: SPACE (take a picture) or Q (for quit)
4. Freeze frame -> take picture -> send picture to openai DALL-E API -> receive AI-generated picture
5. Display AI-generated image in viewfinder
6. Wait for any keypress
7. GOTO 1

The program also saves the original and the AI-generated version of every snapshot
in the 'log' directory for a user's review and amusement.
'''



# Functions
# Exit now
def bail(s):
    from os import sys
    if s: print(s)
    sys.exit(0)

# Print an ASCII text banner
def banner(s):
    import pyfiglet
    result = pyfiglet.figlet_format(s) # , font="slant")
    print(result)



print("Inter-dimensional Camera v0.1")
banner("We Have Such Sights To Show You")
print("calibrating... please wait\n\n")


# Start capturing video from an attached camera
# and display it preview-style modified by opencv canny edge detection

# Import the necessary modules
import cv2

# Use the VideoCapture() function to create a video capture object
# for the attached USB webcam
cap = cv2.VideoCapture(0)

# Use the set() method of the video capture object to set the
# width and height of the preview window
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)

# Use the namedWindow() function to create a window for the preview
cv2.namedWindow("Parallel Universe Preview")


print("YOUR OPTIONS INCLUDE")
print("--------------------")
print("Space = My mind is strong; take an interdimensional photo!")
print("    q = Spare me these twisted visions!\n")



# For canny edge detection filter
#import necessary libraries 
import numpy as np


while True:
    # Use the read() method of the video capture object to capture
    # the next frame from the webcam
    _, frame = cap.read()


    # Use the imshow() function to display the frame in the preview window
    #cv2.imshow("Preview", frame) # This displays the camera feed

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
    edges = cv2.Canny(gray, 150, 216, apertureSize = 3)

    # This displays the edge detection filter version
    cv2.imshow("Parallel Universe Preview", edges)
    

    # Check if the user pressed the "q" key
    # p.s. waitKey(0) will display the window indefinitely until any keypress (suitable for showing images)
    key = cv2.waitKey(1)
    if key == ord("q"): # Quit
        break
    if key == ord(" "):
        # Generate a UUID for the file
        file_uuid = uuid.uuid4()

        # Get the current timestamp
        timestamp = time.strftime("%Y%m%d%H%M%S")

        # Create the file name by combining the UUID and timestamp
        OG_file_name = F"log\{file_uuid}_{timestamp}_0_og.png"
        AI_file_name = F"log\{file_uuid}_{timestamp}_1_ai.jpg"

        
        print(F"Taking photo of dimension #{file_uuid}...")
        print("(There is no going back)")
        
        #cv2.destroyAllWindows()
        #cv2.destroyWindow("Parallel Universe Preview")
        
        # Define the video capture object
        video_capture = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not video_capture.isOpened():
            raise IOError("Cannot open webcam")

        # Capture a single frame from the webcam
        ret, frame = video_capture.read()

        # crop the image using array slices -- it's a NumPy array
        # after all!
        resized_frame = frame[80:576, 0:480] # the stop # is a stop sign, you stop before it not after it
        resized_frame = cv2.resize(resized_frame, (512,512))

        # Save the resized frame to a file
        cv2.imwrite(OG_file_name, resized_frame)

        # Release the video capture object
        video_capture.release()

        print(F"Transmitting image from dimension #{file_uuid}...")

        response = openai.Image.create_variation(
          image=open(OG_file_name, "rb"),
          n=1,
          size="512x512"
        )
        image_url = response['data'][0]['url']


        # Define the URL of the image to download
        image_url = image_url

        # Open the URL and download the image
        response = urllib.request.urlopen(image_url)
        image_data = response.read()

        print("Parting the veil...")

        # Save the downloaded image to a file
        with open(AI_file_name, "wb") as f:
            f.write(image_data)

        # Read the image file into a variable
        image = cv2.imread(AI_file_name)

        # Check if the image was successfully loaded
        if image is None:
            raise IOError("Failed to load the image")

        # Display the image in a window
        cv2.imshow("Parallel Universe Preview", image)

        print("Press any key to go on...")


        # Wait for the user to press any key to close the window
        cv2.waitKey(0)

        print("Re-calibrating, please wait...")
       
        # Use the VideoCapture() function to create a video capture object
        # for the attached USB webcam
        cap = cv2.VideoCapture(0)

        # Use the set() method of the video capture object to set the
        # width and height of the preview window
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)

        # Use the namedWindow() function to create a window for the preview
        #cv2.namedWindow("Parallel Universe Preview")
        

# Use the release() method of the video capture object to release
# the webcam and close the preview window
cap.release()
cv2.destroyAllWindows()


bail("desynchronizing...\ndone")




