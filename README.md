# -Finger-Counting
# Overview
This Python project uses OpenCV and MediaPipe to detect hand gestures in real-time through a webcam. It counts the number of fingers held up by analyzing hand landmarks and displays the count on the video feed.

# Features
Real-time hand tracking using MediaPipe's Hands module.
Accurate detection of fingers held up based on hand landmarks.
Dynamic display of the finger count on the video feed.
Includes a mirrored view for intuitive interaction.

# Technologies Used
Python: Core programming language.
OpenCV: For video capture and image processing.
MediaPipe: For hand gesture detection and landmark extraction.

# How It Works
The application detects key landmarks on the hand (e.g., fingertips and joints).
By comparing the relative positions of these landmarks, the application determines which fingers are extended.
Displays the number of fingers held up in real time on the video feed.
