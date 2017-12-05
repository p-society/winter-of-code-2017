from Tkinter import *
from tkFileDialog import askopenfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

g = Tk()
g.title("Rosei Automation Tool")

titles = ["", "BRF", "LUN", "DIN"]
mon1 = ["MON", "111", "112", "113"]
tue1 = ["TUE", "121", "122", "123"]
wed1 = ["WED", "131", "132", "133"]
thu1 = ["THU", "141", "142", "143"]
fri1 = ["FRI", "151", "152", "153"]
sat1 = ["SAT", "161", "162", "163"]
sun1 = ["SUN", "171", "172", "173"]
mon2 = ["MON", "211", "212", "213"]
tue2 = ["TUE", "221", "222", "223"]
wed2 = ["WED", "231", "232", "233"]
thu2 = ["THU", "241", "242", "243"]
fri2 = ["FRI", "251", "252", "253"]
sat2 = ["SAT", "261", "262", "263"]
sun2 = ["SUN", "271", "272", "273"]
foodcodes1 = [titles, mon1, tue1, wed1, thu1, fri1, sat1, sun1]
foodcodes2 = [titles, mon2, tue2, wed2, thu2, fri2, sat2, sun2]
d1 = {111:"mess1b1", 121:"mess1b2", 131:"mess1b3", 141:"mess1b4", 151:"mess1b5", 161:"mess1b6", 171:"mess1b7"\
	,112:"mess1l1", 122:"mess1l2", 132:"mess1l3", 142:"mess1l4", 152:"mess1l5", 162:"mess1l6", 172:"mess1l7"\
	,113:"mess1d1", 123:"mess1d2", 133:"mess1d3", 143:"mess1d4", 153:"mess1d5", 163:"mess1d6", 173:"mess1d7"}

fpath = []

def preffileopen():
	file1 = askopenfile()
	a = file1.name
	b = a.split("/")
	fpath.append(b[len(b)-1])
	c = "Preferences File: " + fpath[0]
	label = Label(text=c, font=('Arial', 10)).grid(row=1, sticky="w")

def cost():
	with open(fpath[0], "r") as f:
		b = f.readlines()
	b = [x.strip() for x in b]
	f.close()
	a = []
	count1 = count2 = 0
	uc1 = b[2].split()
	uc2 = b[3].split()
	for i in uc1:
		if (i[3] == '1'):
			count1+=10
		elif (i[3] == '2' or i[3] == '3'):
			count1+=25
	for j in uc2:
		if (j[3] == '1'):
			count2+=10
		elif (j[3] == '2' or j[3] == '3'):
			count2+=25
	a.append(count1)
	a.append(count2)
	return a

def booking():
	with open(fpath[0], "r") as f:
		a = f.readlines()
	a = [x.strip() for x in a]
	f.close()
	username = a[0]
	paword = a[1]
	ufc1 = a[2].split()
	ufc2 = a[3].split()
	browser = webdriver.Chrome("chromedriver.exe")
	browser.get("http://172.16.2.200:8080/rosei/login.jsp")
	uname = browser.find_element_by_name('un')
	pword = browser.find_element_by_name('pw')
	uname.send_keys(username)
	pword.send_keys(paword)
	browser.find_element_by_name('submit').click()
	if (len(ufc1) != 0):
		browser.get("http://172.16.2.200:8080/rosei/selectmess.jsp")
		browser.find_element_by_xpath('//*[@id="p1"]').click()
		for j in ufc1:
			r = j[1:len(j)]
			g = int(r)
			xp = "//*[@id=\"" + d1[g] + "\"]"
			if (j[0] == "V" or j[0] == "v"):
				for i in range(2):
					browser.find_element_by_xpath(xp).click()
			elif (j[0] == "N" or j[0] == "n"):
				for i in range(1):
					browser.find_element_by_xpath(xp).click()
		browser.find_element_by_xpath('//*[@id="submit"]').click()
		sleep(2)
		if (len(ufc2) !=0):
			browser.get("http://172.16.2.200:8080/rosei/selectmess.jsp")
			browser.find_element_by_xpath('//*[@id="p2"]').click()
			for j in ufc2:
				r = j[1:len(j)]
				g = int(r) - 100
				xp = "//*[@id=\"" + d1[g] + "\"]"
				if (j[0] == "V" or j[0] == "v"):
					for i in range(2):
						browser.find_element_by_xpath(xp).click()
				elif (j[0] == "N" or j[0] == "n"):
					for i in range(1):
						browser.find_element_by_xpath(xp).click()
			browser.find_element_by_xpath('//*[@id="submit"]').click()
			sleep(2)
			browser.close()
	elif (len(ufc1) == 0 and len(ufc2) != 0):
		browser.get("http://172.16.2.200:8080/rosei/selectmess.jsp")
		browser.find_element_by_xpath('//*[@id="p2"]').click()
		for j in ufc2:
			r = j[1:len(j)]
			g = int(r) - 100
			xp = "//*[@id=\"" + d1[g] + "\"]"
			if (j[0] == "V" or j[0] == "v"):
				for i in range(2):
					browser.find_element_by_xpath(xp).click()
			elif (j[0] == "N" or j[0] == "n"):
				for i in range(1):
					browser.find_element_by_xpath(xp).click()
		browser.find_element_by_xpath('//*[@id="submit"]').click()
		sleep(2)
		browser.close()
	browser.quit()
	q = cost()
	r = sum(q)
	s = "Total Cost: Rs. " + str(r)
	costLabel = Label(text=s, font=('Arial', 12)).grid(row=3, sticky="w")
	binLabel = Label(text="Booking Complete!", font=('Arial', 14, 'bold')).grid(row=2, sticky="w")

f = Button(text = "Select Preferences File", command = preffileopen).grid(row=0, column=0, sticky="w")
spacing = Label(text="                                   ").grid(row=0, column=1)
reg = Button(text = "Register Coupons", command = booking).grid(row=0, column=2)

g.mainloop()
