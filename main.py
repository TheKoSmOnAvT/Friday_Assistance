import speech_recognition as sr
import sys
import webbrowser
import os
from gtts import gTTS
import pyaudio
import pygame

def speak(audioString):
	Speck_machine = gTTS(text=audioString, lang='en')
	Speck_machine.save("audio.mp3")
	pygame.mixer.init()
	pygame.mixer.music.load("audio.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	pygame.mixer.music.stop()
	pygame.mixer.music.unload()


def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Tell")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)

	try:
		zadanie = r.recognize_google(audio, language="en-EN").lower()
		print("you say: " + zadanie)
	except sr.UnknownValueError:
		zadanie = command()

	return zadanie

def makeSomething(zadanie):
	if 'open google' in zadanie  or 'google' in zadanie:
		speak('YUP')
		url = 'https://google.com'
		webbrowser.open(url)
	elif 'who is max' in zadanie or 'whois max' in zadanie:
		speak('max is loshara')
	elif 'stop' in zadanie:
		speak('okey, good day and good night')
		sys.exit()
	elif 'hello friday' in zadanie:
		speak('Hello, my creator, what i can do for you?')
	elif 'open my programs' in zadanie:
		speak('no problems')
		os.system(r'D:\github_repository\voice_assistance\scripts\steam.py')
		os.system(r'D:\github_repository\voice_assistance\scripts\kaspersky.py')
		os.system(r'D:\github_repository\voice_assistance\scripts\browser.py')
	elif 'secret' in zadanie:
		webbrowser.open('https://i.pinimg.com/originals/84/c0/7d/84c07d50db7aab993a0c5cfc17b7094b.jpg')
		speak('ja ja ja ja ja ja ЪЪЪЪЪЪ')



speak("wake up samurai")
while True:
	makeSomething(command())