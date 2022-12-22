# How to disable or enable Enter key in a form input?
1. Create a function to disable Enter button in that input form:<br><br>
&emsp;**function dis_Enter(e) {**<br>
&emsp;&emsp;**if (e.keyCode === 13 || e.which === 13) {**<br>
&emsp;&emsp;&emsp;**e.preventDefault();**<br>
&emsp;&emsp;&emsp;**return false;**<br><br>
2. Set variable for the input field:<br><br>
&emsp;**let input = document.querySelector('input_id');**<br><br>
3. To disable, add an eventlistener:<br><br>
&emsp;**input.addEventListener('keypress', dis_Enter);**<br><br>
4. to enable, remove eventlistener:<br><br>
&emsp;**input.removeEventListener('keypress', dis_Enter);**<br><br>
*Check more in cs50w week5-JavaScript task.html file, or visit https://github.com/hanzovan/cs50w-week5-JavaScript/blob/master/tasks.js*