import speech_recognition as sr
import pyttsx3 as pt
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Hey There!")
    print("Welcome to First Aid Bot")
    print("Tell Us What Happened")
    print("We Would be Really Happy To Help You")
    audio=r.listen(source)
    print("Thanks! Processing in Process.....................")
data=r.recognize_google(audio)
"""if(("bleeding" in data) or ("blood" in data))
    print("Tie a cloth over the wound in order to stop bleeding")

"""


