__lab3_term2_json_retriving.py__

For example, suppose an API returned a specific object that the user wants to see.
In response to the key entered by the user, it is necessary to show the corresponding value.
But there are a few cases where the program may behave differently:

♦ if the value corresponding to the key is also an object - in this case you can display the entire object completely,
 or inform the user that it is also an object and display the available keys
 
♦ if the value is a list - you can simply show the whole list, or tell it to be a list,
 ask which item the list item is to display ... implementation options can be many



__The result of the module__ in the screenshots in the \ data_and_images \ lab3_2-1.jpg, lab3_2-11.jpg and lab3_2-111.jpg





__flask_app.py__

This is a web application that allows you to map on the map (location) the mates
(people you are subscribed to) of the specified Twitter account. The value of the "location" field
specified by a comrade is represented on the map by an arbitrary marker type, but also contains
 the name of that comrade (the value of the "screen_name" field).

__The result of the web-app flask_app.py__ in screenshots in \ data_and_images \ lab3_3-1.jpg, lab3_3-11.jpg, lab3_3-111.jpg
and lab3_3-1111.jpg
Also the realisation of this web-app you can find on http://denysger88.pythonanywhere.com/ 