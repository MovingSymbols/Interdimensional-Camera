# Inter-Dimensional Camera
This is a simple art project: *a camera that takes pictures from one dimension over* (or from a parallel universe, whatever.)  

It does this by using an art-generating AI to create a photo that is similar to (but not the same as) whatever the camera sees. When you take a photo, you don't see the camera's output, you see the AI's rendition.  It's like taking photos from across dimensions.

That's why the photos it takes are always... different.  It's not imaging the reality that is in front
of the lens, it's imaging whatever reality is in front of the lens FROM ONE DIMENSION OVER.

That's also why the viewfinder is just lines. The camera is always seeing across dimensions, but only dimly.  When you take a photo, it pierces the veil and gets a high-resolution color shot (of whatever is in the other dimension) instead of just a dim preview.

## How It Works
Technically, this program will:
1. open an attached webcam
2. Display a preview video feed (filtered through opencv edge detection for the lines effect)
3. Wait for a keypress: SPACE (take a picture) or Q (for quit)
4. Freeze frame -> take picture -> send picture to openai DALL-E API -> receive AI-generated picture
5. Display AI-generated image in viewfinder
6. Wait for any keypress
7. GOTO 1

The program also saves the original and the AI-generated version of every snapshot in the 'log' directory for a user's review and amusement.

## Requirements
Python, a web camera, some python libraries (see the code for which ones) and most importantly, an OpenAI API key (openai.com)

There should also be a 'log' directory present in which to store images.
