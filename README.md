# Flask-Calulator-app
An application for addition,multiplication,substraction and division.

OBJECTIVE:
- To create a web API.
- To perform calulations from the user inputs. Two integers are taken as inputs on the web page, and then calulation will be done.
- The page will consist of drop down to choose the operations, two boxes for the user input of two integers and a button "calculate" to show the result in a next page.
- Perform testing of the API using Postman.


LIBRARIES USED:
-   flask:    Flask is a web framework for designing web API,web Applications.
-   request:  The Request, in Flask, is an object that contains all the data sent from the Client to Server. 
-   render_template: It is used to implement the structure and style in the web page.
-   jsonify: It helps in converting the objects into json.


POSTMAN:
Postman is an application used for testing the working of api.
In order to test the api made we configured the postman into "request type html>post>raw>json".
 (NOTE:Using POST instead of GET would prevent the client from having to worry about encoding values and data size, since data would be sent in the body, rather than as a URL parameter.)
