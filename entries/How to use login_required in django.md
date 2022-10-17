# How to use **login_required** in Django?
1. Create login function

2. In the project's **setting.py**, add this line at the bottom of the file: <br><br>&emsp;**LOGIN\_URL = '*app_name:login_function_name*'**

3. At the beginning of views.py, import the built-in login\_required function: <br><br>&emsp;**from django.contrib.auth.decorators import login_required**

4. Before every function that need to be decorated, add:<br><br>&emsp;**@login_required**