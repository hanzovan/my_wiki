# How to import a function from a file\_name.py in Django
1. Create file\_name.py in the same path with manage.py *(Not in the same path with views.py of the app as in Flask)*
2. In views.py, import the function:<br><br>&emsp;**from file\_name import function_name**