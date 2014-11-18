#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from random import randint
# from our keys module (keys.py), import the keys dictionary
from keys import keys
 
argfile = str(sys.argv[1])  # argument taken as string, indicates file to be called for tweets

 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

fock=open('response-message.txt','r')
felon = fock.readLines()
fock.close()

#list of specific strings we want to check for in Tweets
t = ['Hello world!',
    'Hello World!',
    'Hello World!!!',
    'Hello world!!!',
    'Hello, world!',
    'Hello, World!']
 
for line in f:
    fodder = line.split('//',2)
    api.update_status(fodder[0])
    twts = api.search(q="Hello World!")
    for s in twt:
        for g in t:
            if g == s.text:
                sn = s.user.screen_name
                m = "@%s " % (sn) + felon
                s = api.update_status(m, s.id)   
    time.sleep(int(fodder[1]))  # Tweet every 15 minutes, number is in seconds