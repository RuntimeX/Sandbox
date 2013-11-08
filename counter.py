#!/usr/local/bin/python
# -*- coding: utf-8 -*-


class Player(object):
   
    points = 0
    wins = 0
    def __init__(self, name, points = 0, wins = 0, count = 1):
        self.name = name
        self.points = points
        self.wins = wins
        Player.count+=1
        
    def get_name(self, count):
        name = raw_input("Player %i name: " % count)
        confirm = raw_input("Your name is %s. Is this right? (Y/n)" %  name)
        pos = ("yes", "Yes", "y", "Y")
        neg   = ("no", "No", "n", "N")
        try:
            if confirm in pos:
                print("Great %s! Get ready to play!" % name)
            if confirm in neg:
                name = raw_input("Ok Player %n, what is your name?" %Player.playerCount)
        except:
            print("Go to Hell.")
        finally:
            return name
   
    
        
