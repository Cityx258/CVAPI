# CVAPI 

## This is a computer vision API that will be used to track and follow a face in it's feild of vision

## Technologies used

    (These are just speculations at the moment and are subject to changes)
- opencv2
- fastAPI
- docker

## How it will be used

<p>A raspberry pi zero 2 w will have a camera connected to it. The pi will stream the video
to the server that will handle it. The server will take care of finding the face that it chooses to track
(the first one it finds). It will do it's best to center that face. Since the camera is mounted on a robotic arm, 
the outputs of the API (the movement controls of the robotic arm) are what is going to keep the face in the middle of the frame.</p>

## Basic functionment of the API

<p>Rasbperry Pi zero 2 w sends the video signal to the server for treatment</p>
<p>API receives that video signal</p>
<p>API finds a face and tracks it</p>
<p>API computes what movements to do to keep the face in the middle</p>
<p>API sends the commands (direction controls) back to the raspberry pi zero 2 w</p>
<p>Raspberry Pi zero 2 w receives those commands</p>
<p>Raspberry Pi zero 2 w converts the commands into physical movement on the robotic arm</p>

_repeat until Raspberry Pi 2 w shuts down

## How to start the project

1. git clone https://github.com/Cityx258/CVAPI
2. cd CVAPI
3. uv run fastapi
