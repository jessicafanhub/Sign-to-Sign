Jessica Fan - Term Project | Spring 2020 

Project Name: Sign To Sign

Description: 

Sign To Sign is an educational sign language learning program that utilizes openCV and pygame. The program includes a play feature and learn feature. The learn feature allows the user to practice memorization of ASL alphabet symbols through openCV. The program uses color detection to detect blue objects in view and allows the user to select the corresponding images with that blue control. Within the learn feature are three different modes, challenge, test, and regular. Challenge mode allows the user to try a score as many correct answers as possible with 60 seconds and test allows the user to keep track of correct, incorrect, and most missed gestures. The regular mode allows users to practice their knowledge of gestures and earn 2 points for every correct answer, and have their points multiplied by 3 for consecutively correct answers. The score decrements by 1 point when incorrect.

The play feature displays a target word and requires the user to catch falling symbols using the same blue control in order to spell out the word. The user must avoid obstacles that fall amongst the symbols while spelling out their words. These obstacles will reset the word progress! The user only has 5 lives and loses lives for each incorrect gesture selected.

Running the project:

The user must run the file: TPMaster.py through terminal. 
This can be accessed by right clicking terminal and selecting “New Terminal at Folder” for mac users and typing the command “python3 TPMaster.py” 
The file “images”, "sounds", "words.txt", and the file “leahleeSans.ttf”  must be placed within the same folder as TPMaster.py 

All import statements at the top of the TPMaster.py:

import pygame as pg 
from pygame.locals import *
import numpy as np
import sys
import cv2
import string
import random 
import math

Listed: pygame, cv2, numpy, sys, string, random, RandomWords

Existing Shortcut Commands:

esc - to return to main menu at any time 


