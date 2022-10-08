# How to solve "TEMPLATE DOES NOT EXIST" error
- In ***settings.py***:
 - In ***TEMPLATES*** objects:
     - Change ***DIR = []*** to ***DIR = [BASE_DIR/'templates']
- Save change