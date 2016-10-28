import urllib.request

cookie=input("Enter session cookie: ")
regno=input("Enter registration number: ")
url='https://vtop.vit.ac.in/student/view_photo_2.asp?rgno='+regno   
name=regno+'.jpg'
img = urllib.request.URLopener()
img.addheader('Cookie',cookie)
if ('image/jpg' in str(img.open(url).info())):
    img.retrieve(url,name)
else:
    print ("Invalid number")
