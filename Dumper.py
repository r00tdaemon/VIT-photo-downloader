import urllib
import os
cookie = raw_input("Enter session cookie: ")
rng = raw_input("Enter range (e.g. 15BCE0000 - 15BCE1111): ")
rng = rng.split()

for i in range(int(rng[0][-4:]), int(rng[2][-4:]) + 1):
    url = 'https://vtop.vit.ac.in/student/view_photo_2.asp?rgno=' + rng[0][:5] + str(i).zfill(4)
    name = rng[0][:5] + str(i).zfill(4) + '.jpg'
    img = urllib.URLopener()
    img.addheader('Cookie', cookie)
    img.retrieve(url, name)
    print rng[0][:5] + str(i).zfill(4) + ' Done'
print ('Cleaning up...')
for i in range(int(rng[0][-4:]), int(rng[2][-4:]) + 1):
    with open(rng[0][:5] + str(i).zfill(4) + '.jpg','rb') as f:
        if (f.readlines()==[]):
            f.close()
            os.remove(rng[0][:5] + str(i).zfill(4) + '.jpg')
