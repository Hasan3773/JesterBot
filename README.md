## Jesture Bot
# Inspiration
The goal for this project was to be a music attack bot controlled by hand gestures. You would use one hand to control the robot's movement and the other hand to control the sound played on the Arduino. However, we ran ran into a lot of issues with interfaces, the mediapipe computer vision hand library and the Arduino together, as well as sending data to the Arduino wirelessly.

# What it does
What JesterBot is currently able to do is take in coordinates of your finger from a computer webcam and compute that to directions for the Arduino car. Then the car goes vroom vroom and drives around.

# How we built it
For the software side of the project we used googles mediapipe library for our hand recognition model, then we continued to spend 10 hours going down a rabbit hole of trying to get gesture recognition to work, trying various prebuilt models and even training our own model, however none of which worked and we ran into what we like to call "pip hell" where our environment's would run into countless errors that usually ended up being resolved by resetting our computers 5 times. At the end we ended up just using some distance calculations on the points on your hand on and the location of that point on the screen to control the different movements.

The Arduino Uno is designed to receive the signals of the hand signals as char datatypes through a Bluetooth module, and then uses the information to control the control the 4 TT motors on the robot with a L298N motor controller. The controller has the left and the right side motors hooked up to different channels, allowing the car to turn freely. In order to use the Bluetooth module, the voltage signals from the Due had to be stepped down using a logic level converter. Additionally, as of initial design, a capacitor circuit was designed to power a speaker and play sound, using a transistor amplifying circuit.
