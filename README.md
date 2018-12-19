# REST-web-service
## answer3.py is a web service server written with flask framework
### The web service exposes the following endpoints:
* /convert/fahrenheit/
* /convert/celsius/
* /convert/kelvin/
* /convert/rankine/
### Each of the endpoints receives a tempertaure, and returns a JSON object of that temperature converted into the other three temperature scales.  
* Input temperature can be negative or positive, integer or floating number  
* Input temperature has to be a valid number in decimal notation, Scientic notation not accepted :( 
* Example input:  
    * http://localhost:5000/convert/kelvin/20.78/  
* Example output:  
    * {"celsius":-252.36999999999998,"fahrenheit":-422.26599999999996,"rankine":37.404}  
* Can handle invalid input type and values  
    * Eg. convert/fahrenheit/badinput/
    * Eg. convert/fahrenheit/0..32/

