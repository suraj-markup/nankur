#This is a code for Dobble game


import string 
import random
symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
print(pos1)
print(pos2)
#pos1 and pos2 are same symbol position in card1 and card2

samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
if(pos1==pos2):
    card2[pos1]=samesymbol
    card1[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])

i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1

print(card1)
print(card2)

ch=input("Spot the similar symbol: ")
if(ch==samesymbol): 
    print("Right")
else:
    print("Wrong")


# #speech recognition

# import speech_recognition as sr
# AUDIO_FILE= ("harvard.wav")
# # use audio file as source

# r=sr.Recognizer() # initialize the recognizer

# with sr.AudioFile(AUDIO_FILE) as source:
#     audio=r.record(source) 

# #reads the audio file

# try:
#     print("Audio file Contains " + r.recognize_google(audio))
# except sr.UnknownValueError :
#     print("Google Speech Recgonition could not understand the audio")
# except sr.RequestError :
#     print("Couldn't get the results from google Speech Recognition")