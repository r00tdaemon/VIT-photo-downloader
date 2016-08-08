import urllib

cookie=raw_input("Enter session cookie: ")
regno=raw_input("Enter registration number: ")
url='https://vtop.vit.ac.in/student/view_photo_2.asp?rgno='+regno   
name=regno+'.jpg'
img = urllib.URLopener()
img.addheader('Cookie',cookie)
img.retrieve(url,name)

