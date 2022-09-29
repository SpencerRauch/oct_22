from flask import Flask, render_template  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/path2')          # The "@" decorator associates this route with the function immediately following
def path_2():
    return '<h1>You\'ve reached the second path</h1>'  # Return the string 'Hello World!' as a response

@app.route('/hello/<name>') #path variable we called name, surround by <>
def say_hello(name):
    print("I got the name " + name)
    return f"Hello {name}"

@app.route('/say/<name>/<int:times>') #path variable we called name, surround by <>
def say_name_times(name,times):
    return name * times

@app.route('/template')
def template():
    return render_template("index.html")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
    # app.run(debug=True, host='0.0.0.0')    # to run on local router

#pip install pipenv <--- run this once ever to install pipenv
#pipenv install flask <--- run once per project to setup virtual environment
   #* you may need to prepend with python -m or python3 -m

#to get rid of a virtual env:
    #delete pipfile and pipfile lock
    #run "pipenv --rm" inside the directory

#default data type of a path variable -- string


