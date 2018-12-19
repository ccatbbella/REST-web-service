from flask import Flask, jsonify,request
from locale import atof
app = Flask(__name__)

# input constraints: the input temperature have to be in decimal notation (eg. 2*10^32 is illegal)
# input can be negative or floating point number
@app.route('/convert/fahrenheit/<path:fahrenheitAsString>',methods = ['GET'])
def getTempForFa(fahrenheitAsString):
    try:
        # strip away the / at the end of url
        if fahrenheitAsString[-1] == '/':
            fahrenheitAsString = fahrenheitAsString[:-1]
        # strip away '-' and '.' in the input
        testString = fahrenheitAsString.replace('.', '', 1)
        testString = testString.replace('-','', 1)
        # check if testString is all digits
        if testString.isdigit() == False:
            raise TypeError
        fahrenheit = atof(fahrenheitAsString)
        if fahrenheit < -459.67 or fahrenheit > 1.416833*10**32:
            raise ValueError
        return jsonify(kelvin = 273.15 + (fahrenheit - 32) * (5.0/9.0), rankine = (fahrenheit + 459.67), celsius = (fahrenheit - 32) * (5.0/9.0)) 
    except TypeError:
        return("please enter a valid numerical number")
    except ValueError:
        return("please enter a number between -459.67 and 1.417 x 10^32")

@app.route('/convert/celsius/<path:celsiusAsString>', methods = ['GET'])
def getTempForC(celsiusAsString):
    try:
        if celsiusAsString[-1] == '/':
            celsiusAsString = celsiusAsString[:-1]
        testString = celsiusAsString.replace('.', '', 1)
        testString = testString.replace('-','', 1)
        if testString.isdigit() == False:
            raise TypeError
        celsius = atof(celsiusAsString)
        if celsius < -273.15 or celsius > 10**32:
            raise ValueError
        return jsonify(fahrenheit = celsius * (9./5) + 32, kelvin = celsius + 273.15, rankine = celsius * (9./5) + 491.67)
    except TypeError:
        return("please enter a valid numerical number")
    except ValueError:
        return("please enter a number between -273.15 and 10^32") 


@app.route('/convert/kelvin/<path:kelvinAsString>', methods = ['GET'])
def getTempForK(kelvinAsString):
    try:
        if kelvinAsString[-1] == '/':
            kelvinAsString = kelvinAsString[:-1]
        testString = kelvinAsString.replace('.', '', 1)
        testString = testString.replace('-','', 1)
        if testString.isdigit() == False:
            raise TypeError
        kelvin = atof(kelvinAsString)
        if kelvin < 0 or kelvin > 10**32:
            raise ValueError
        return jsonify(celsius = kelvin - 273.15, rankine = kelvin * (9./5), fahrenheit = 32 + (kelvin - 273.15) * (9./5))
    except TypeError:
        return("please enter a valid numerical number")
    except ValueError:
        return("please enter a number between 0 and 10^32") 


@app.route('/convert/rankine/<path:rankineAsString>/', methods = ['GET'])
def getTempForR(rankineAsString):
    try:
        if rankineAsString[-1] == '/':
            rankineAsString = rankineAsString[:-1]
        testString = rankineAsString.replace('.', '', 1)
        testString = testString.replace('-','', 1)
        if testString.isdigit() == False:
            raise TypeError
        rankine = atof(rankineAsString)
        if rankine < 0 or rankine > (5.0/9.0)* 10**32:
            raise ValueError
        return jsonify(celsius = (rankine - 491.67) * (5./9), fahrenheit = (rankine - 491.67) * (5./9), kelvin = rankine * (5./9))
    except TypeError:
        return("please enter a valid numerical number")
    except ValueError:
        return("please enter a number between 0 and (5/9 * 10^32)") 

if __name__=='__main__':
    app.run()

