# VIT-photo-downloader
Simple python script to get photo of anyone using their registration number. <br>
You need to have a session cookie to use this. You can get it by logging in, pressing F12, go to the network tab and copy the cookie from there.<br>
###Steps to use
1. Login into the student login and press F12 or right-click and inspect element.<br>
![s1](https://github.com/ujjwal96/VIT-photo-downloader/blob/master/Screenshots/s1.JPG)

2. Go to the Network tab and click on the first request. From the request headers copy the cookie value (you may need to refresh the page after switching to network tab) <br>
![s2](https://github.com/ujjwal96/VIT-photo-downloader/blob/master/Screenshots/s2.JPG)

3. Run the script and paste the cookie. Then enter a registration number or you can dump many photos at a time.<br>
![s3](https://github.com/ujjwal96/VIT-photo-downloader/blob/master/Screenshots/s3.JPG)

4. After it stops you can see the photo in your working directory.<br>
![s4](https://github.com/ujjwal96/VIT-photo-downloader/blob/master/Screenshots/s4.JPG)
