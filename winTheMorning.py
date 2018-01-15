#! /usr/bin/python3
# winTheMorning.py
# It's said that if you win the first hour of your day, 
# you'll win the entire day.
# This script is a motivational YouTube video alarm clock.

from selenium import webdriver
from subprocess import call

# Set computer to full volume
call(["amixer", "-D", "pulse", "sset", "Master", "100%", "unmute"])

# Launch YouTube video
url = 'insert_youtube_link_here'
browser = webdriver.Firefox()
browser.get(url)
