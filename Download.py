# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:51:41 2016

"""
import urllib
cookie=raw_input("Enter session cookie: ")
for i in range(10):
	for j in range(100):
	    url='https://vtop.vit.ac.in/student/view_photo_2.asp?rgno=15BCE0'+str(i)+str(j)    
	    name='15BCE0'+str(i)+str(j)+'.jpg'
	    img = urllib.URLopener()
	    img.addheader('Cookie',cookie)
	    
	    img.retrieve(url,name)

