#Learning from our data
import pandas as pd
import numpy as nm
import csv as cs
import os


#List structure ["teamKey",  1st lvl climb t/f, 2nd lvl climb t/f, 3rd lvl climb t/f,  Cargo #, Outlier Chance,  Hatch #, Outlier Chance]
#os.chdir(r'\Users\jpfei\Downloads')













#Opening Lists for Red
red1 = []
red2 = []
red3 = []

#Opening Lists for Blue
blue1 = []
blue2 = []
blue3 = []


#Red Alliance
red1 = ["frc1", True, True, False, 10, 100,  0, 0]
red2 = ["frc2", True, False, True, 5, 20, 5, 20]
red3 = ['frc3', True, False, False, 10, 10, 0, 0]

#Blue Alliance
blue1 = ['frc4', True, False, False, 6, 25, 4, 35]
blue2 = ['frc5', True, False, True, 5, 10, 5, 15]
blue3 = ['frc6', True, True, True, 10, 15, 0, 0]
############################################################################################################################################
                                                      #RED ALLIANCE CARGO CHANCE
############################################################################################################################################


#Red Alliance 1
funFactor = nm.random.randint(100)
if funFactor <= red1[5]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        red1[4] = red1[4] - nm.random.randint(3)
     elif pOm == 2:
        red1[4] = red1[4] + nm.random.randint(3)
     else:
        red1[4] = red1[4] - nm.random.randint(6)
     if red1[4] < 0:
         red1[4] = 0
funFactor = nm.random.randint(100)

#Red Alliance 2
if funFactor <= red2[5]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        red2[4] = red2[4] - nm.random.randint(3)
     elif pOm == 2:
        red2[4] = red2[4] + nm.random.randint(3)
     else:
        red2[4] = red2[4] - nm.random.randint(6)
     if red2[4] < 0:
         red2[4] = 0

#Red Alliance 3
funFactor = nm.random.randint(100)
if funFactor <= red3[5]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        red3[4] = red3[4] - nm.random.randint(3)
     elif pOm == 2:
        red3[4] = red3[4] + nm.random.randint(3)
     else:
        red3[4] = red3[4] - nm.random.randint(6)
     if red3[4] < 0:
        red3[4] = 0
############################################################################################################################################
                                                      #BLUE ALLIANCE CARGO CHANCE
############################################################################################################################################


#Blue Alliance 1
funFactor = nm.random.randint(100)
if funFactor <= blue1[5]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        blue1[4] = blue1[4] - nm.random.randint(3)
     elif pOm == 2:
        blue1[4] = blue1[4] + nm.random.randint(3)
     else:
        blue1[4] = blue1[4] - nm.random.randint(6)
     if blue1[4] < 0:
        blue1[4] = 0

#Blue Alliance 2
funFactor = nm.random.randint(100)
if funFactor <= blue2[5]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        blue2[4] = blue2[4] - nm.random.randint(3)
     elif pOm == 2:
        blue2[4] = blue2[4] + nm.random.randint(3)
     else:
        blue2[4] = blue2[4] - nm.random.randint(6)
     if blue2[4] < 0:
        blue2[4] = 0


#Blue Alliance 3
funFactor = nm.random.randint(100)
if funFactor <= blue1[5]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        blue3[4] = blue3[4] - nm.random.randint(3)
     elif pOm == 2:
        blue3[4] = blue3[4] + nm.random.randint(3)
     else:
        blue3[4] = blue3[4] - nm.random.randint(6)
     if blue3[4] < 0:
        blue3[4] = 0



############################################################################################################################################
                                                       #RED ALLIANCE HATCH CHANCE
############################################################################################################################################
#Red Alliance 1 
funFactor = nm.random.randint(100)
if funFactor <= red1[7]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        red1[6] = red1[6] - nm.random.randint(3)
     elif pOm == 2:
        red1[6] = red1[6] + nm.random.randint(3)
     else:
        red1[6] = red1[6] - nm.random.randint(6)
     if red1[6] < 0:
        red1[6] = 0
#Red Alliance 2
funFactor = nm.random.randint(100)
if funFactor <= red2[7]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        red2[6] = red2[6] - nm.random.randint(3)
     elif pOm == 2:
        red2[6] = red2[6] + nm.random.randint(3)
     else:
        red2[6] = red2[6] - nm.random.randint(6)
     if red2[6] < 0:
        red2[6] = 0
#Red Alliance 3
funFactor = nm.random.randint(100)
if funFactor <= red3[7]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        red3[6] = red3[6] - nm.random.randint(3)
     elif pOm == 2:
        red3[6] = red3[6] + nm.random.randint(3)
     else:
        red3[6] = red3[6] - nm.random.randint(6)
     if red3[6] < 0:
        red3[6] = 0
############################################################################################################################################
                                                       #BLUE ALLIANCE HATCH CHANCE
############################################################################################################################################
#Blue Alliance 1
funFactor = nm.random.randint(100)
if funFactor <= blue1[7]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        blue1[6] = blue1[6] - nm.random.randint(3)
     elif pOm == 2:
        blue1[6] = blue1[6] + nm.random.randint(3)
     else:
        blue1[6] = blue1[6] - nm.random.randint(6)
     if blue1[6] < 0:
        blue1[6] = 0
#Blue Alliance 2
funFactor = nm.random.randint(100)
if funFactor <= blue2[7]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        blue2[6] = blue2[6] - nm.random.randint(3)
     elif pOm == 2:
        blue2[6] = blue2[6] + nm.random.randint(3)
     else:
        blue2[6] = blue2[6] - nm.random.randint(6)
     if blue2[6] < 0:
        blue2[6] = 0
#Blue Alliance 3
funFactor = nm.random.randint(100)
if funFactor <= blue3[7]:
     print(funFactor)
    
     pOm = nm.random.randint(3)
     if pOm == 1:
        blue3[6] = blue3[6] - nm.random.randint(3)
     elif pOm == 2:
        blue3[6] = blue3[6] + nm.random.randint(3)
     else:
        blue3[6] = blue3[6] - nm.random.randint(6)
     if blue3[6] < 0:
        blue3[6] = 0

############################################################################################################################################
                                                       #RED ALLIANCE CLIMES
############################################################################################################################################
#Red Alliance 1
funFactor - nm.random.randint(6)
if funFactor == 1 | funFactor == 2 | funFactor == 3 & red1[1] == True:
    red1[1] = True
else:
    red1[1] = False
#
if funFactor == 4 | funFactor == 5 & red2[1] == True:
    red1[2] = True
else:
    red1[2] = False
#
if funFactor == 6 & red1[1] == True:
    red1[3] = True
else:
    red1[3] = False
#

#Red Alliance 2
funFactor - nm.random.randint(6)
if funFactor == 1 | funFactor == 2 | funFactor == 3 & red2[1] == True:
    red2[1] = True
else:
    red2[1] = False
#
if funFactor == 4 | funFactor == 5 & red2[1] == True:
    red2[2] = True
else:
    red2[2] = False
#
if funFactor == 6 & red2[1] == True:
    red2[3] = True
else:
    red2[3] = False
#
#Red Alliance 3
funFactor - nm.random.randint(6)
if funFactor == 1 | funFactor == 2 | funFactor == 3 & red3[1] == True:
    red3[1] = True
else:
    red3[1] = False
#
if funFactor == 4 | funFactor == 5 & red3[1] == True:
    red3[2] = True
else:
    red3[2] = False
#
if funFactor == 6 & red3[1] == True:
    red3[3] = True
else:
    red3[3] = False
#
############################################################################################################################################
                                                       #BLUE ALLIANCE CLIMES
###########################################################################################################################################
#blue Alliance 1
funFactor - nm.random.randint(6)
if funFactor == 1 | funFactor == 2 | funFactor == 3 & blue1[1] == True:
    blue1[1] = True
else:
    blue1[1] = False
#
if funFactor == 4 | funFactor == 5 & blue2[1] == True:
    blue1[2] = True
else:
    blue1[2] = False
#
if funFactor == 6 & blue1[1] == True:
    blue1[3] = True
else:
    blue1[3] = False
#



#Blue Alliance 2
funFactor - nm.random.randint(6)
if funFactor == 1 | funFactor == 2 | funFactor == 3 & blue2[1] == True:
    blue2[1] = True
else:
    blue2[1] = False
#
if funFactor == 4 | funFactor == 5 & blue2[1] == True:
    blue2[2] = True
else:
    blue2[2] = False
#
if funFactor == 6 & blue2[1] == True:
    blue2[3] = True
else:
    blue2[3] = False
#

#Blue Alliance 3
funFactor - nm.random.randint(6)
if funFactor == 1 | funFactor == 2 | funFactor == 3 & blue3[1] == True:
    blue3[1] = True
else:
    blue3[1] = False
#
if funFactor == 4 | funFactor == 5 & blue3[1] == True:
    blue3[2] = True
else:
    blue3[2] = False
#
if funFactor == 6 & blue3[1] == True:
    blue3[3] = True
else:
    blue3[3] = False
#
############################################################################################################################################
                                                       #RED ALLIANCE GAME LOGIC
###########################################################################################################################################
#Red alliance 1

#Cargo
red1P = red1[4] ** 3
#Hatch
red1P = red1P + red1[6] ** 2
#Level 1
if red1[1] == True:
    red1P = red1P + 3
#Level 2
if red1[2] == True:
    red1P = red1P + 6
#Level 3
if red1[3] == True:
    red1P = red1P + 12

#Red alliance 2
#Cargo
red2P = red2[4] ** 3
#Hatch
red2P = red2P + red2[6] ** 2
#Level 1
if red2[1] == True:
    red2P = red2P + 3
#Level 2
if red2[2] == True:
    red2P = red2P + 6
#Level 3
if red2[3] == True:
    red2P = red2P + 12

    
#Red alliance 3
#Cargo
red3P = red3[4] ** 3
#Hatch
red3P = red3P + red3[6] ** 2
#Level 1
if red3[1] == True:
    red3P = red3P + 3
#Level 2
if red3[2] == True:
    red3P = red3P + 6
#Level 3
if red3[3] == True:
    red3P = red3P + 12


#Red Alliance Ranking Points

############################################################################################################################################
                                                       #BLUE ALLIANCE GAME LOGIC
###########################################################################################################################################


print(red1)
print(red2)
print(red3)
print(blue1)
print(blue2)
print(blue3)