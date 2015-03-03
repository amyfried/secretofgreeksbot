#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import time
import os
import sys
import random
from cleanup import parseText

#Abgdeztiklmnxoprsufc
greekletters = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", 
				"iota","kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", 
				"sigma", "tau", "upsilon", "phi","chi", "psi", "omega"]

argfile = str(sys.argv[1])
parseText(argfile)

#configuration
MY_CONSUMER_KEY = '......'
MY_CONSUMER_SECRET = '.....'
MY_ACCESS_TOKEN_KEY = '.....'
MY_ACCESS_TOKEN_SECRET = '.......'
auth = tweepy.OAuthHandler(MY_CONSUMER_KEY, MY_CONSUMER_SECRET)
auth.set_access_token(MY_ACCESS_TOKEN_KEY, MY_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


filename=open(argfile,'r')
f=filename.readlines()
filename.close()


#use to know count of words that begin with each letter in the text file
#figure how to make functions better
def counter_function(f):
	count1=0
	count2=0
	count3=0
	count4=0
	for line in f:
		if line[0]=='u':
			count1= count1 + 1
		if line[0]=='v':
			count2= count2 + 1
		if line[0]=='w':
			count3= count3 + 1
		if line[0]=='x':
			count4= count4 + 1
	print count1
	print count2
	print count3
	print count4
#counter_function(f)
#a=14537*   
#b=9675*
#c=17406*
#d=9946*
#e=7818*
#f=6382*
#g=5843*
#i=8303*
#k=1735*
#l=5211*
#m=10709*
#n=6098*
#o=7219*
#p=22171*
#r=8955*
#s=22759*
#t=11389*
#u=16179*
#x=293*
#z=719*

def choose_randgreek(greekletters):
	letter=random.choice(greekletters)
	return letter

#how to get random range
def generateRandomWord(letter):
	key = letter[0]
	if key == 'a':
		word =  f[random.randint(0,14536)]
		return word
	if key == 'b':
		word =  f[random.randint(14537,24211)]
		return word
	if key == 'c':
		word =  f[random.randint(24212,41617)]
		return word
	if key == 'd':
		word =  f[random.randint(41618,51563)]
		return word
	if key == 'e':
		word =  f[random.randint(51564,59381)]
		return word
	if key == 'f':
		word =  f[random.randint(59382,65763)]
		return word
	if key == 'g':
		word =  f[random.randint(65764,71606)]
		return word
	if key == 'i':
		word =  f[random.randint(71607,79909)]
		return word
	if key == 'k':
		word =  f[random.randint(79910,81644)]
		return word
	if key == 'l':
		word =  f[random.randint(81645,86855)]
		return word
	if key == 'm':
		word =  f[random.randint(86856,97564)]
		return word
	if key == 'n':
		word =  f[random.randint(97565,103662)]
		return word
	if key == 'o':
		word =  f[random.randint(103663,110881)]
		return word
	if key == 'p':
		word =  f[random.randint(110882,133052)]
		return word
	if key == 'r':
		word =  f[random.randint(133053,142007)]
		return word
	if key == 's':
		word =  f[random.randint(142008,164766)]
		return word
	if key == 't':
		word =  f[random.randint(164767,176155)]
		return word
	if key == 'u':
		word =  f[random.randint(176156,192334)]
		return word
	if key == 'x':
		word =  f[random.randint(192335,192627)]
		return word
	if key == 'z':
		word =  f[random.randint(192628,193346)]
		return word

def createTweet():
	randgreek1 =choose_randgreek(greekletters)
	randgreek2 =choose_randgreek(greekletters)
	randgreek3 =choose_randgreek(greekletters)

	word1=generateRandomWord(randgreek1)
	word2=generateRandomWord(randgreek2)
	word3=generateRandomWord(randgreek3)

	alltogether = randgreek1 + " " + randgreek2 + " " + randgreek3 + ":" + " " + "This organization secretly means...." + " " + word1 + word2 + word3
	return alltogether.replace("\n", " ")
	
def runTweet():
    for line in f:
        tweeted=createTweet()
        print tweeted
        api.update_status(status=tweeted)
        time.sleep(300)#Tweet every 5 minutes

# allows you to discriminate between importing and opening directly
# if importing then functions wont occur without being called
# if open directly then an calls below will occur
if __name__ == '__main__':
	runTweet()
