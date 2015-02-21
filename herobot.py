#!/usr/bin/env python
from clickerheroes import *
from time import *
h = Heroes()
	
def startup():
	h.checkprog()
	sleep(0.5)
	h.selmonster()
	sleep(0.2)
	money = h.getmoney()
	while money < h.heroes[1].price:
		h.click(20)
		money = h.getmoney()
	sleep(5)

def buyhero(ll):
	h.selhero(ll)
	sleep(0.2)
	h.ctrlclick()

def buybetty():
	buyhero(h.heroes[h.BETTY])
	sleep(1)
	h.upgrade()
	sleep(2)

def buymidas():
	buyhero(h.heroes[h.MIDAS])
	sleep(1)
	h.upgrade()
	sleep(2)

def earlygame(start):
	lvl = start
	money = h.getmoney()
	while money < h.heroes[h.FROST].price:
		while money > h.heroes[lvl+1].price:
			lvl += 1
			if lvl == h.NATALIA+2:
				buybetty()
			if lvl == h.AMEN+1:
				buymidas()
		h.selhero(h.heroes[lvl])
		h.ctrlclick()
		sleep(1)
		h.checkprog()
		h.resetcursor()
		if lvl > 17:
			h.upgrade()
			sleep(1)
		money = h.getmoney()

def frostleaf():
	money = h.getmoney()
	while money < 3e30:
		h.upgrade()
		sleep(1)
		h.selhero(h.heroes[h.FROST])
		sleep(1)
		h.ctrlclick()
		sleep(5)
		money = h.getmoney()

def finalupgrade():
	for n in range(0, h.FROST):
		h.selhero(h.heroes[n])
		sleep(0.5)
		h.ctrlclick(10)
		sleep(0.2)
	sleep(1)
	h.upgrade()

def nextgame():
	h.selhero(h.heroes[h.AMEN])
	sleep(1)
	h.ctrlclick(2)
	sleep(0.2)
	h.resetcursor()
	sleep(0.2)
	h.ascend()

count = 0
print "HeroBot started"
while True:
	start = datetime.now()
	startup()
	sleep(1)
	earlygame(1)
	frostleaf()
	finalupgrade()
	print "Reached lvl:",h.getlevel()
	nextgame()
	end = datetime.now()
	count += 1
	print "Round time:", end-start
	print "Ascension count:", count
	sleep(5)

