# How to test Django project on mobile?
1. Mobile phone and django project creating device-laptop-destop use the same wifi.

2. Find Local IP address either by:
 1. Using terminal, type command: <br><br>&emsp;**ifconfig**<br><br>Hit Enter, then check **CSUM**>the **inet** number.
 2. Go to network, go to Advanced, then click TCP/IP tab, get the number in IPv4 Address line.<br><br>

3. In Django project's settings.py, in ALLOWED_HOSTS, in [], type in: <br><br>&emsp;**IP Address number**.
4. Go to terminal run django project with following command:<br><br>&emsp;**python3 manage.py runserver 0.0.0.0:8000**.<br><br>
5. On your mobile phone, open a web browser, enter:<br><br>&emsp;**IP Address number:8000**