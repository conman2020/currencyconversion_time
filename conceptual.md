### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
- Python is more for the back-end work while javascript is more for the front-end work typically. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
dict.get('a', 'nothingfound')
dict.get("c") will return None if key is not fount
dict.get("c", "3") will set 3 as the default value to return


try:
    dictExample["Kamal"]
    print('The key exists in the dictionary')
except KeyError as error:
    print("The key doesn't exist in the dictionary")

- What is a unit test?
- a unit test an individual component of your application , BUT SOMETIMES  integration tests
- 

- What is an integration test?
- integraton test tests how one part of your application interacts with another part of your application when two different applications are used and data is exchanged

- What is the role of web application framework, like Flask?
- Flask is a framwework which helps to simplify code needed to be written and duplication of code. as welll as ser

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  One is more of a redirection the other requires a type to be inputted to get to the location 

- How do you collect data from a URL placeholder parameter using Flask?
- 

- How do you collect data from the query string using Flask?

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?
