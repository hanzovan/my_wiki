# How to solve "TEMPLATE DOES NOT EXIST" error
1. *Check if you really have the template file at the right place*
 1. *If not, move the file to the right path and restart server*
 2. *If the path is right and the template really exist, then go to next step*
2. *In* **settings.py**:
 - *In* **TEMPLATES** *objects*:
     - *Change* **DIR = []** *to* **DIR = [BASE_DIR/'templates']**
2. *Save change*