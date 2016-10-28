import urllib.request
import os
import threading
import socket

socket.setdefaulttimeout(30)

def download(rgno, cookie):
    global errors

    url = 'https://vtop.vit.ac.in/student/view_photo_2.asp?rgno=' + rgno
    name = rgno + '.jpg'
    img = urllib.request.URLopener()
    img.addheader('Cookie',cookie)
    try:
        img.retrieve(url,name)
    except:
        print('Error downloading ' + rgno)
        errors.append(rgno)
        return
    print (rgno + ' Done')


def cleanup(rng):
    print ('Cleaning up...')
    for i in range(int(rng[0][-4:]), int(rng[2][-4:]) + 1):
        try:
            with open(rng[0][:5] + str(i).zfill(4) + '.jpg','rb') as f:
                if (f.readlines()==[]):
                    f.close()
                    os.remove(rng[0][:5] + str(i).zfill(4) + '.jpg')
        except:
            pass

def main():
    cookie = input("Enter session cookie: ")
    rng = input("Enter range (e.g. 15BCE0000 - 15BCE1111): ")
    rng = rng.split()

    global errors
    threads=[]
    errors=[]

    for i in range(int(rng[0][-4:]), int(rng[2][-4:]) + 1):
        rgno=rng[0][:5] + str(i).zfill(4)
        t=threading.Thread(target=download,args=(rgno,cookie))
        threads.append(t)
        if len(threads)==150:
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            threads=[]
    if threads != []:
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    if errors!=[]:
        print('Retrying...')
        socket.setdefaulttimeout(60)
        for rgno in errors:
            download(rgno,cookie)
    cleanup(rng)
    exit(0)

if __name__ == '__main__':
    main()
