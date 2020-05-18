# Jessica Fan - Term Project - jlfan
# As of now, this program must be run through terminal
# Basic Resources Referenced:
# Basic Pygame Overview: https://www.youtube.com/watch?v=FfWpgLFMI7w
# Button Events: https://www.youtube.com/watch?v=P-UuVITG7Vg 
# Button Function: https://www.youtube.com/watch?v=kK4xhHr1QeQ
# Splash and End Screens: https://www.youtube.com/watch?v=rLrMPg-GCqo
# Control Screen: https://www.youtube.com/watch?v=Ox0HnIzLakE
# ASL PNGS: http://suuasl.blogspot.com/2011/05/abc.html

import pygame as pg 
from pygame.locals import *
import numpy as np
import sys
import cv2
import string
import random 
import math

pg.init()
# create the screen 
gameHeight = 600
gameWidth = 800
screen = pg.display.set_mode((gameWidth,gameHeight))

# correct/incorrect/newWord sounds: http://www.wavsource.com/sfx/sfx3.htm
# bomb : https://opengameart.org/content/bombexplosion8bit
correctSound = pg.mixer.Sound('sounds/chime.wav')
incorrectSound = pg.mixer.Sound('sounds/wrong.wav')
bombSound = pg.mixer.Sound('sounds/bomb.wav')
#newWord = pg.mixer.Sound('sounds/nextLvl.wav')

# font : https://www.dafont.com/212-leahlee-sans.font
font = pg.font.Font("leahleeSans.ttf", 24)
fontL = pg.font.Font("leahleeSans.ttf", 40)
fontM = pg.font.Font("leahleeSans.ttf", 30)
fontXL = pg.font.Font("leahleeSans.ttf", 90)

# Title of window
pg.display.set_caption("Sign to Sign")

# Logo : made using canva.com
logo = pg.image.load("images/LOGOVER12.png")
logoX = 260
logoY = 160

# learn : made using canva.com
button1 = pg.image.load("images/learnButton.png")
button1X = 100
button1Y = 270
oneWidth, oneHeight = button1.get_width(), button1.get_height()
oneRect = pg.Rect((button1X, button1Y), (oneWidth, oneHeight))

# play : made using canva.com
button2 = pg.image.load("images/playButton.png")
button2X = 570
button2Y = 270
twoWidth, twoHeight = button1.get_width(), button1.get_height()
twoRect = pg.Rect((button2X, button2Y), (twoWidth, twoHeight))

# help
ctrl = font.render("Help", True, (34,34,34))
ctrlX = 10
ctrlY = 5
ctrlW, ctrlH = ctrl.get_width(), ctrl.get_height()
controlRect = pg.Rect((ctrlX, ctrlY), (ctrlW, ctrlH))
screen.blit(ctrl, (ctrlX, ctrlY))

# bomb: https://pngtree.com/element/down?id=MTU0OTgwOA==&type=1&time=1587855427&token=Yzc4MGQ2MThjMDBhNWQzMjg0NzVmNjEzZTk1Zjk0Mzc=&t=0
bomb = pg.image.load("images/bomb.png").convert_alpha()

# set up
statDict = {}
for letter in string.ascii_lowercase:
    statDict[letter] = 0

# https://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

# words.txt: pulled from https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/
wordList = []
contents = readFile("words.txt")
for line in contents.split("\n"):
    wordList.append(line.strip())

for word in wordList:
    if len(word) > 10:
        wordList.remove(word)

for word in wordList:
    word = word.lower()

def showLogo():
    screen.blit(logo, (logoX, logoY))

def showButtons():
    screen.blit(button1, (button1X,button1Y))
    screen.blit(button2, (button2X,button2Y))
    screen.blit(ctrl, (ctrlX, ctrlY))

def controlScreen():
    while True:
        screen.fill((213,227,(191)))
        text = font.render("How to Play:", True, (34,34,34))
        textX, textY = (350, 10)
        textW, textH = text.get_width(), text.get_height()
        screen.blit(text, (textX, textY))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    mainMenu()
        pg.display.update()
    
# main loop, the program begins here 
def mainMenu():
    while True:
        # color of screen 
        screen.fill((213, 227, 191))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if oneRect.collidepoint(x,y):
                    learnOptionsLoop()
                elif twoRect.collidepoint(x,y):
                    playLoop(wordList)
                elif controlRect.collidepoint(x,y):
                    controlScreen()
        showLogo()
        showButtons()
        pg.display.update()

def learnOptionsLoop():
        while True:
            heading = fontL.render("Select Mode: ", True, (105,105,105))
            reg = fontM.render("Regular", True, (105,105,105))
            regX = 340
            regY = 150
            regW, regH = reg.get_width(), reg.get_height()
            regRect = pg.Rect((regX, regY), (regW, regH))
            chal = fontM.render("Challenge", True, (105,105,105))
            chalX = 330
            chalY = 300
            chalW, chalH = chal.get_width(), chal.get_height()
            chalRect = pg.Rect((chalX, chalY), (chalW, chalH))
            test = fontM.render("Test", True, (105,105,105))
            testX = 355
            testY = 450
            testW, testH = test.get_width(), test.get_height()
            testRect = pg.Rect((testX, testY), (testW, testH))
            screen.blit(reg, (regX, regY))
            screen.blit(chal, (chalX, chalY))
            screen.blit(test, (testX, testY))
            screen.blit(heading, (315, 5))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        mainMenu()
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if regRect.collidepoint(x,y):
                        learnLoop()
                    elif chalRect.collidepoint(x,y):
                        learnChal()
                    elif testRect.collidepoint(x,y):
                        learnTest(statDict)
            pg.display.update()

# Color Detection Algorithm: 
# https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/
def learnLoop(score=0, consecCorrect=0):
    running = True
    cvRect = None
    cap = cv2.VideoCapture(0)
    learnMode = learnFeature(screen, score, 0, 0, consecCorrect)
    letter = learnMode.generateNewLetter()
    options = learnMode.constructOptions(letter)
    while running:
        ret, frame = cap.read()
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(bluecnts)>0:
            blue_area = max(bluecnts, key=cv2.contourArea)
            (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
            cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
            xg = -1 * xg + 1200
            cvRect = pg.Rect((xg, yg), (wg, hg))   

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pg.surfarray.make_surface(frame)
        screen.fill((213, 227, 191))
        screen.blit(frame, (0,0))
        
        learnMode.displayScore()
        learnMode.displayTargetLetter(letter)
        learnMode.displayOptions(options)
        correctRect = learnMode.getCorrectRect(letter)
        if cvRect != None:
            for rect in learnMode.getAllRects():
                if cvRect.colliderect(rect) and rect == correctRect:
                    learnMode.correctAnswer()
                    pg.time.delay(300)
                    correctSound.play()
                    learnLoop(learnMode.getScore(), learnMode.getConsecCorrect())
                elif cvRect.colliderect(rect) and rect != correctRect:
                    learnMode.incorrectAnswer(letter)
                    pg.time.delay(300)
                    incorrectSound.play()
                    running = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    mainMenu()
        pg.display.update()

    while not running:
        learnMode.displayCorrect(letter)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    learnLoop(learnMode.getScore(), learnMode.getConsecCorrect())
                if event.key == pg.K_ESCAPE:
                    mainMenu()
    
        pg.display.update()

# Color Detection Algorithm: 
# https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/
def learnChal(correct=0, timer=60):
    running = True
    cvRect = None
    clock = pg.time.Clock()
    cap = cv2.VideoCapture(0)
    learnMode = learnFeature(screen, 0, correct)
    letter = learnMode.generateNewLetter()
    options = learnMode.constructOptions(letter)
    while running:
        ret, frame = cap.read()
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(bluecnts)>0:
            blue_area = max(bluecnts, key=cv2.contourArea)
            (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
            cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
            xg = -1 * xg + 1200
            cvRect = pg.Rect((xg, yg), (wg, hg))   

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pg.surfarray.make_surface(frame)
        screen.fill((213, 227, 191))
        screen.blit(frame, (0,0))

        learnMode.startChallenge()
        learnMode.displayTargetLetter(letter)
        learnMode.displayOptions(options)
        correctRect = learnMode.getCorrectRect(letter)

        seconds = clock.tick()/1000.0
        timer -= seconds
        displayTimer = math.trunc(timer)
        timerText = "Time: "+ str(displayTimer)
        time1 = fontM.render(timerText, True, (255,255,255))
        screen.blit(time1, (10,10))

        if displayTimer == 0:
            running = False
        if cvRect != None:
            for rect in learnMode.getAllRects():
                if cvRect.colliderect(rect) and rect == correctRect:
                    learnMode.correctAnswer()
                    pg.time.delay(300)
                    correctSound.play()
                    learnChal(learnMode.getCorrect(), timer)
                elif cvRect.colliderect(rect) and rect != correctRect:
                    learnMode.incorrectAnswer(letter)
                    pg.time.delay(300)
                    incorrectSound.play()
                    learnChal(learnMode.getCorrect(), timer)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    mainMenu()

        pg.display.update()

    while not running:
        learnMode.challengeEndScreen()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    learnChal(0, 60)
                if event.key == pg.K_ESCAPE:
                    mainMenu()
    
        pg.display.update()

# Color Detection Algorithm: 
# https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/
def learnTest(statDict, correct=0, incorrect=0):
    running = True
    cvRect = None
    cap = cv2.VideoCapture(0)
    learnMode = learnFeature(screen, 0, correct, incorrect, 0, statDict)
    letter = learnMode.generateNewLetter()
    options = learnMode.constructOptions(letter)
    while running:
        ret, frame = cap.read()
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(bluecnts)>0:
            blue_area = max(bluecnts, key=cv2.contourArea)
            (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
            cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
            xg = -1 * xg + 1200
            cvRect = pg.Rect((xg, yg), (wg, hg))   

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pg.surfarray.make_surface(frame)
        screen.fill((213, 227, 191))
        screen.blit(frame, (0,0))
        
        learnMode.testLearn()
        learnMode.displayTargetLetter(letter)
        learnMode.displayOptions(options)
        correctRect = learnMode.getCorrectRect(letter)
        if cvRect != None:
            for rect in learnMode.getAllRects():
                if cvRect.colliderect(rect) and rect == correctRect:
                    learnMode.correctAnswer()
                    pg.time.delay(500)
                    correctSound.play()
                    learnTest(learnMode.getStats(), learnMode.getCorrect(), learnMode.getIncorrect())
                elif cvRect.colliderect(rect) and rect != correctRect:
                    learnMode.incorrectAnswer(letter)
                    pg.time.delay(500)
                    incorrectSound.play()
                    learnTest(learnMode.getStats(), learnMode.getCorrect(), learnMode.getIncorrect())

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    mainMenu()
        pg.display.update()
  
def createBlocks(word, speed):
    onScreen = []
    for n in range(0,7):
        onScreen.append(Gesture(screen, speed))
    if word != "":
        for letter in word:
            onScreen.append(Gesture(screen, speed, letter))
    random.shuffle(onScreen)
    while len(onScreen) > 13:
        for letter in onScreen:
            if letter.getLetter() not in word:
                onScreen.remove(letter)
    return onScreen
        
def generateRandomWord():
    return random.choice(wordList)

def displayTargetWord(word):
    text = fontL.render(word, True, (255,255,255))
    textX = 10
    textY = 500
    screen.blit(text, (textX, textY))

def displayWordProgress(prog):
    text = fontL.render(prog, True, (0,255,0))
    textX = 10
    textY = 500
    screen.blit(text, (textX, textY))

def displayScore(score):
    text = fontL.render("Completed: " + str(score), True, (255,255,255))
    textX = 10
    textY = 550
    screen.blit(text, (textX, textY))

def getLetters(gestureList):
    letters = []
    for gesture in gestureList:
        letters.append(gesture.getLetter())
    return letters

# heart image: https://ya-webdesign.com/imgdownload.html
def displayLives(numLost):
    numHearts = 5 - numLost
    imgX = 10
    heart = pg.image.load("images/life.png")
    heart = pg.transform.scale(heart, (15,15))
    for n in range(0, numHearts):
        screen.blit(heart, (imgX, 490))
        imgX += 30

def createObstacles(score, speed):
    bombs = []
    if score < 2:
        num = 2
    elif score >= 2 and score < 5:
        num = 4
    elif score >= 5:
        num = 6 
    for n in range(0, num):
        bombs.append(Obstacle(screen, speed))
    return bombs


# Color Detection Algorithm: 
# https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/
def playLoop(wordList, score=0, numLost =0, speed=4):
    cap = cv2.VideoCapture(0)
    running = True
    clock = pg.time.Clock()
    word = generateRandomWord()
    wordForDisplay = word
    gestureList = createBlocks(word, speed)
    bombsList = createObstacles(score, speed)
    cvRect = None
    correctRect = False
    wordFinish = False
    correctRects = []
    correctGestureObj = []
    wordProg = ""
    while running:
        ret, frame = cap.read()
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange (hsv, lower_blue, upper_blue)

        bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

        if len(bluecnts)>0:
            blue_area = max(bluecnts, key=cv2.contourArea)
            (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
            cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
            xg = -1 * xg + 1200
            if xg+wg < gameWidth and xg+wg > 0 and yg+hg < gameHeight and yg+hg > 0:
                cvRect = pg.Rect((xg, yg), (wg, hg)) 
            
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pg.surfarray.make_surface(frame)
        screen.fill((213, 227, 191))
        screen.blit(frame, (0,0))

        displayTargetWord(wordForDisplay)
        if wordProg != "":
            displayWordProgress(wordProg)
        displayScore(score)
        displayLives(numLost)

        currentLetter = list(word)[0]
        
        for gesture in gestureList:
            if gesture.getPos() > gameHeight:
                gestureList.pop(gestureList.index(gesture))
            gesture.displayGesture()
            gesture.fall()
        
        for bomb in bombsList:
            if bomb.getPos() > gameHeight:
                bombsList.pop(bombsList.index(bomb))
            bomb.displayObstacle()
            bomb.fall()
        
        if len(gestureList) <= 5:
            new = createBlocks(word, speed)
            for gesture in new:
                gestureList.append(gesture)
                if gesture.getLetter() == currentLetter:
                    correctGestureObj.append(gesture)

        if correctGestureObj == []:
            for gesture in gestureList:
                if gesture.getLetter() == currentLetter:
                    correctGestureObj.append(gesture)
                    correctRect = True
        
        if cvRect != None and correctRect: 
            for answer in correctGestureObj:
                if cvRect.colliderect(answer.getRect()):
                    correctSound.play()
                    gestureList.pop(gestureList.index(answer))
                    correctGestureObj = []
                    wordProg += currentLetter 
                    word = word[1:]
                    if len(word) == 0:
                        score += 1
                        if score >= 1 and score < 5:
                            playLoop(wordList, score, numLost, 6)
                        if score >= 5:
                            playLoop(wordList, score, numLost, 8)
                        else: 
                            playLoop(wordList, score, numLost)

        if cvRect != None:
            for gesture in gestureList:
                gestRect = gesture.getRect()
                if cvRect.colliderect(gestRect) and gesture not in correctGestureObj:
                    incorrectSound.play()
                    gestureList.remove(gesture) 
                    numLost += 1
                    if numLost == 5:
                        running = False 

            for bomb in bombsList:
                bombRect = bomb.getRect()
                if cvRect.colliderect(bombRect):
                    bombSound.play()
                    bombsList.remove(bomb)
                    word = wordForDisplay
                    wordProg = ""
                                     
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    mainMenu()
        pg.display.update()

        # game over: https://www.clipartkey.com/view/iRhhRww_game-over-transparent-game-over/
        while not running:
            gameOver = pg.image.load("images/gameover.png")
            gameOver = pg.transform.scale(gameOver, (400,120))
            if score == 1:
                text = "You completed "+ str(score) + " word!"
            else:
                text = "You completed "+ str(score) + " words!"
            text1 = fontL.render(text, True, (34,34,34))
            text2 = fontM.render("Press 'c' to play again!", True, (34,34,34))
            screen.fill((213,227,(191)))
            screen.blit(text1, (250, 340))
            screen.blit(text2, (290,555))
            screen.blit(gameOver, (200, 180))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        mainMenu()
                    if event.key == pg.K_c:
                        playLoop(wordList)
            pg.display.update()

class learnFeature(object):
    def __init__(self, screen, score=0, correct=0, incorrect=0, consecCorrect=0, statDict={}):
        self.score = score 
        self.correct = correct
        self.incorrect = incorrect
        self.consecCorrect = consecCorrect
        self.screen = screen
        self.options = []
        self.font = pg.font.Font("leahleeSans.ttf", 63)
        self.fontS = pg.font.Font("leahleeSans.ttf", 30)
        self.rects = []
        self.secondsLeft = 90
        self.statDict = statDict

        # creates a dict that maps letters to their .png's
        self.letterDict = {}
        for letter in string.ascii_lowercase:
            imageName = "images/"+letter+".png"
            self.letterDict[letter] = imageName 
        
    def getAllRects(self):
        return self.rects

    def getScore(self):
        return self.score

    def getCorrect(self):
        return self.correct

    def getIncorrect(self):
        return self.incorrect

    def getConsecCorrect(self):
        return self.consecCorrect

    def getStats(self):
        return self.statDict

    def getSeconds(self):
        return self.secondsLeft

    def generateNewLetter(self):
        return random.choice(string.ascii_letters).lower()

    def displayTargetLetter(self, letter):
        text = self.font.render(letter, True, (255,255,255))
        textX = 400
        textY = 0
        self.screen.blit(text, (textX, textY))

    def constructOptions(self, letter):
        self.options = []
        self.options = [letter]
        while len(self.options) < 4:
            other = random.choice(string.ascii_letters).lower()
            if other not in self.options:
                self.options.append(other)
        random.shuffle(self.options)
        return self.options
    
    def displayOptions(self, options):
        optX = 50
        optY = 300
        self.rects = []
        for option in self.options:
            opt = pg.image.load(self.letterDict[option])
            opt = pg.transform.scale(opt, (100,100))
            optWidth, optHeight = opt.get_width(), opt.get_height()
            optRect = pg.Rect((optX, optY), (optWidth, optHeight))
            screen.blit(opt, (optX,optY))
            optX += 185
            self.rects.append(optRect)
    
    def getCorrectRect(self, letter):
        index = self.options.index(letter)
        return self.rects[index]

    def displayScore(self):
        scoreX = 0
        scoreY = 0
        message = "Score: "+ str(self.getScore())
        text = self.font.render(message, True, (255,255,255))
        self.screen.blit(text, (scoreX, scoreY))

    def isStreak(self):
        if self.consecCorrect > 1:
            return True 
        else:
            return False
        
    def correctAnswer(self):
        self.correct += 1
        self.consecCorrect += 1
        if self.isStreak():
            self.score += 2 * 3
        else:
            self.score += 2

    def incorrectAnswer(self, letter):
        self.incorrect += 1
        self.consecCorrect = 0 
        self.score -= 1
        if self.statDict != {}:
            self.statDict[letter] += 1
 
    def displayCorrect(self, letter):
        screen.fill((213,227,(191)))
        text = self.font.render("The correct answer for " + letter + " was: ", True, (34,34,34))
        text2 = self.fontS.render("Press 'c' to continue!", True, (34,34,34))
        image = pg.image.load(self.letterDict[letter])
        image = pg.transform.scale(image, (200,200))
        self.screen.blit(text, (100,0))
        self.screen.blit(text2, (300,560))
        self.screen.blit(image, (300, 220))
    
    def startChallenge(self):
        secondsLeft = 90
        count1 = "Correct: "+ str(self.correct)
        text1 = self.fontS.render(count1, True, (255,255,255))
        self.screen.blit(text1, (10, 560))

    def challengeEndScreen(self):
        screen.fill((213,227,(191)))
        text = self.font.render("You got " + str(self.correct) + " gestures correct!", True, (34,34,34))
        text2 = self.fontS.render("Press 'c' to begin a new challenge!", True, (34,34,34))
        self.screen.blit(text, (130, 230))
        self.screen.blit(text2, (240, 320))

    def testLearn(self):
        letters = ""
        if self.mostMissed() == "N/A":
            letters = "N/A"
        elif len(self.mostMissed()) > 1 and isinstance(self.mostMissed(), list):
            for letter in self.mostMissed():
                letters += letter +", "
        else:
            letters = self.mostMissed()[0]
        count1 = "Correct: "+ str(self.correct)
        count2 = "Incorrect: "+ str(self.incorrect)
        freqMiss = "Most missed: "+ letters
        text1 = self.fontS.render(count1, True, (255,255,255))
        text2 = self.fontS.render(count2, True, (255,255,255))
        text3 = self.fontS.render(freqMiss, True, (255,255,255))
        self.screen.blit(text1, (10, 530))
        self.screen.blit(text2, (10, 560))
        self.screen.blit(text3, (10, 500))

    def mostMissed(self):
        lettersMissed =[]
        high = max(self.statDict.values())
        if high != 0:
            for letter in self.statDict:
                if self.statDict[letter] == high:
                    lettersMissed.append(letter)
            return lettersMissed
        return "N/A"
            
class Gesture(object):
    def __init__(self, screen, speed, letter=""):
        self.imgX = random.randrange(10, 750, 100)
        self.imgY = random.randrange(-1000, -75, 100)
        self.speed = speed
        
        if letter != "":
            self.letter = letter
        else:
            self.letter = random.choice(string.ascii_lowercase)
        self.screen = screen
        self.letterDict = {}
        for letter in string.ascii_lowercase:
            imageName = "images/"+letter+".png"
            self.letterDict[letter] = imageName 

    def fall(self):
        self.imgY += self.speed 

    def getPos(self):
        return self.imgY

    def getCoord(self):
        return (self.imgX, self.imgY)

    def getLetter(self):
        return self.letter.lower()

    def displayGesture(self):
        self.letter = self.letter.lower()
        img = pg.image.load(self.letterDict[self.letter]).convert_alpha()
        img = pg.transform.scale(img, (75,75))
        imgRect = pg.Rect((self.imgX, self.imgY), (75, 75))
        self.screen.blit(img, (self.imgX,self.imgY))

    def getRect(self):
        return pg.Rect((self.imgX, self.imgY), (75, 75))

class Obstacle(object):
    def __init__(self, screen, speed):
        self.imgX = random.randrange(10, 730, 90)
        self.imgY = random.randrange(-1500, -100, 90)
        self.screen = screen
        self.speed = speed

    def fall(self):
        self.imgY += self.speed

    def getPos(self):
        return self.imgY

    def displayObstacle(self):
        img = bomb
        img = pg.transform.scale(img, (75,75))
        imgRect = pg.Rect((self.imgX, self.imgY), (75, 75))
        self.screen.blit(img, (self.imgX,self.imgY))

    def getRect(self):
        return pg.Rect((self.imgX, self.imgY), (50, 50))

mainMenu()
