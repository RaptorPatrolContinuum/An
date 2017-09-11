from MiraExternals import *

'''
HUGE CAVEAT:
THE INPUT MUST BE NONEMPTY BECAUSE ShittySI(AutoVision(0,1),AutoVision(0,1))] on empty graph [] doesn't work. but we know that [] is SI to [] so watch out



idea:
Use the compression theorem to know that it's more important to know the SI of object where the basis is large and "L = 1"
then the idea is that for idle time we do:
SI(Vision(x),Vision(y)) as x,y go to infinity
then when we start appending things to the basis we already know what things are isom


problems:
what is the data format?
try:
[[x,y],[yes/no]] as an entry

how to start from where you left off?
then assume that we add each info sequentially,
Look at the "final entry": FE
then FE[0][0] is X and FE[0][1] is Y
then we continue:

problem: 
this function takes a long time


idea:
just run every hour x
'''

SIData = open("SIData.txt","r+")

if len(SIData.read()) == 0:
	print("check what vision shows",AutoVisionString(1,1))
	print("check stats", ShittySI(AutoVisionString(1,1),AutoVisionString(1,1)))
	SIData.write(str([[0,0],ShittySI(AutoVisionString(3000,1),AutoVisionString(3000,1))]))
	
