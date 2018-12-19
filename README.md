# REST-web-service
## answer3.py is a web service server written with flask framework
### The web service exposes the following endpoints:
* /convert/fahrenheit/
* /convert/celsius/
* /convert/kelvin/
* /convert/rankine/
### Each of the endpoints receives a tempertaure, and returns a JSON object of that temperature converted into the other three temperature scales.
* Some example input: 
        * http://localhost:5000/convert/fahrenheit/-212/
        * http://localhost:5000/convert/kelvin/20.78/
        * http://localhost:5000/convert/celsius/32/
* Input temperature has to be a valid number in decimal notation. (Scientic notation not accepted :( )
