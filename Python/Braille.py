from gtts import gTTS
import os


braille = ['⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔',
			'⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚',
			'⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞',
			'⠥','⠧','⠺','⠭','⠽','⠵',
			'⠱','⠰','⠣','⠿','⠀','⠮','⠐','⠼','⠫','⠩',
			'⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌',
			'⠜','⠹','⠈','⠪','⠳','⠻','⠘','⠸']

english = ['0','1','2','3','4','5','6','7','8','9',
			'a','b','c','d','e','f','g','h','i','j',
			'k','l','m','n','o','p','q','r','s','t',
			'u','v','w','x','y','z',
			':',';','<','=',' ','!','"','#','$','%',
			'&','','(',')','*','+',',','-','.','/',
			'>','?','@','[','\\',']','^','_']			

def braille2English(brailleText) :
	return ''.join([english[braille.index(fi)] for ch in brailleText for fi in braille if ch == fi])
def english2Braiile(englishText) :
	return ''.join([braille[english.index(fi)] for ch in englishText.lower() for fi in english if ch == fi])


def read(text): 
	language = 'en'
	gtts = gTTS(text=text, lang=language, slow=False)
	gtts.save("speach.mp3")
	
	os.system("mpg123 speach.mp3")



brailleText = english2Braiile("What you are hearing has been converted to braille and then again to English")

backToEng = braille2English(brailleText)

print(backToEng)
read(backToEng)