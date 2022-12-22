# How to add or remove item in request.session
In a list, we used to use list.append(item)/list.remove(item). However, request.session['name'] will not behave like a list. Therefore, we'll have to create a list from request.session['name'], modify the list, then give the request.session that value of list: <br><br>
&emsp;**list_name = request.session['name']**<br><br>
&emsp;**list_name.add(item)** *Or* **list_name.remove(item)**<br><br>
&emsp;**request.session['name'] = list_name**