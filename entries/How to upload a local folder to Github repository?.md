# How to upload a local folder to Github repository?
1. *Go to github.com:*
 1. *Create a new repository*
 2. *Copy the* **repository's URL**
2. *Go to terminal, cd to folder that needed to be upload to Github, use these syntax command (hit Return after every command line):*
 1. "**git init**"
 2. "**git add**" *to add all mini folder inside that folder*
 3. "**git commit**" *to commit the change of the files and folder*
 4. "**git remote add origin**" + **repository URL**
 5. "**git push --set-upstream origin master**"
3. *Every time you make a change to a file, use* "**git commit**", then "**git push**"
4. *Every time you add a new file or folder, use* "**git add**", then "**git commit**", then "**git push**"