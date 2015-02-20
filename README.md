# Herobot
I, just like many of you ClickerHeroes players, had the slightly annoying problem of not being able to play ClickerHeroes all the time. Work, friends and other annoying "distractions" kept getting in the way. So, I developed a very simple bot that can take care of Clicker Heroes heros soul farming, while you do your social obligations. This can also be used as a learning example when developing your own bot. 

clickerheroes.py - contains methods the bot uses for controlling the game. 
herobot.py - contains the bot code itself, please modify this according to your playstyle if you'd like. 

To install the bot it requires pyscreenshot, cv2, pytesseract, numpy and pyuserinput. In debian/ubuntu:

	apt-get install python-pip python-numpy python-opencv tesseract-ocr tesseract-ocr-eng git python-xlib
	pip install pyscreenshot pytesseract numpy pyuserinput
	git clone https://github.com/flandree/herobot.git
	cd herobot

Make sure the whole clicker heroes window is open in a web browser, then enter: 

	./herobot.py

Pictures borrowed from reddit user vorksholk. I will update the bot as I progress through and explore the game. Right now it works best for 100-1000HS farming, but with some tweaking it can work for other gameplay styles. 

**Warning:** It only works on www.clickerheroes.com, Kongregate version have some differences, if there is interest i can add support, unless someone else does it. 
