import pyttsx3
engine = pyttsx3.init()
string = input("Enter a string.\n")
engine.say(string)
engine.runAndWait()
