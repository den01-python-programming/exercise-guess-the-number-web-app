# Exercise - Guess the number in a Flask web app

This exercise will explore how we can build the *guess a number* functionality into a web app using Python's Flask library. We won't worry about the mechanisms of creating the pages and we won't bother with any HTML, CSS or JavaScript. The exercise files will contain all the relevant files you need to get going and just implement the Python part.

### Getting started with Flask - Hello World

The most basic task we can achieve in Flask is the age-old "*Hello World!*" application. Here's how it looks:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

This code is contained inside this repository in the `src` folder and is called `hello_world_app.py`. To get and run the code, from a terminal run:

```plaintext
user@host:~$ git clone <your-repo-url-here>
user@host:~$ cd <your-repo-name>
user@host:~$ virtualenv .flask_env
user@host:~$ source .flask_env/bin/activate
user@host:~$ pip install flask
user@host:~$ cd src
user@host:~$ python3 hello_world_app.py
```

This will set up the virtual environments and assumes the following:

- [You have Python installed](https://scott3142.uk/python-programming/codelabs/getting-started/index.html)
- [You can activate a virtual environment](https://scott3142.uk/python-programming/codelabs/getting-started/index.html?index=..%2F..index#3)
- [You can install packages inside your virtual environment using pip](https://scott3142.uk/python-programming/codelabs/getting-started/index.html?index=..%2F..index#2)

This code outputs "Hello, World!" in a web browser on your computer's localhost port 5000 (i.e. at [http://localhost:5000](http://localhost:5000)). You can stop the web app running at any time by pressing Ctrl-C in the terminal.

### Building the app

The exercise template contains the following files:

```plaintext
.
+-- README.md
+-- tests/
|   +-- test_app.py
+-- src/
|   hello_world_app.py
|   web-app/
```

and the web-app folder (which is where we'll mostly be working) looks like this:

```plaintext
.
+-- web_app.py
+-- static/
|   +-- <web files we don't need to worry about>
+-- templates/
|   +-- splash.html
|   +-- holding.html
```

Let's take a look at some key lines from the two files we care about:

#### web_app.py
```python
# imports and set up

@app.route("/")
def splash():
    return render_template('splash.html')

@app.route("/playing", methods=['GET','POST'])
def inprogress():

    default_value = '0'
    try:
        current_guess = int(request.form.get('text',default_value))
        # inplement your checking code here

    except:
        guess_message = "Please enter a whole number between " + str(data.lower_bound) + " and " + str(data.upper_bound) + "."

    return render_template('playing.html',guess_message=guess_message,upper_bound=upper_bound,lower_bound=lower_bound)

# run app
```

This file sets up the web server, much like we did in the `Hello World!` section. We won't go much into the inner mechanisms of Flask (you can read more about that [here](https://realpython.com/introduction-to-flask-part-1-setting-up-a-static-site/)) but you should be able to see what's happening in the main part of this file.

Much like any other Python program we've written, we want to implement a check to see if the guess is correct. You can use very similar code to what you developed in the first exercise here. All we're doing is getting the user input and checking it against something we know.

The `try` and `except` loop is there to handle what happens if the user doesn't input a whole number. If this happens, the line `current_guess = int(request.form.get('text',default_value))` will error and the prgram will jump to `guess_message = "Please enter a whole number between " + str(data.lower_bound) + " and " + str(data.upper_bound) + "."`.

The program finally returns the template `playing.html` file and passes it to the server, along with the three variables `guess_message`, `upper_bound` and `lower_bound`. The `playing.html` file reads those variables as follows:

#### playing.html
```html
<!-- Headers ... -->

<section id="header">
	<div class="inner">
    	<img src="{{ url_for('static', filename='images/logo-white.png') }}" style="width:40%; margin-top:-5%;"/>
        {% if 'correctly.' not in guess_message %}
	    <p>Take a guess! Remember, the number is a whole number between {{ lower_bound }} and {{ upper_bound }}.</p><br>
            <form method="POST">
                <input name="text"><br><br>
                <input type="submit">
            </form>
        {% endif %}
        <p> {{ guess_message }} </p>
        <ul class="actions special">
            <li><a href="/" class="button scrolly">Restart</a></li>
        </ul>
	</div>
</section>

<!-- Scripts ... -->
```

The variables are accessed in the HTML with double curly braces `{{ my_variable }}` and the form sends the user data back to `web_app.py` through the route `@app.route("/playing", methods=['GET','POST'])`. If the guess is correct, the form input is not printed and the user's only option is to restart the game.

**Note:** Can you notice the bug in the code? You might want to check out [this article](https://stackoverflow.com/questions/49664010/using-variables-across-flask-routes) and look at using something like the following:

```python
class DataStore():

    #initialise number, lower and upper bounds here
    lower_bound =
    upper_bound =
    number =

data = DataStore()
```

You might be interested in checking out `splash.html` as well. There's not much going on there, except for setting up the initial splash page.

#### splash.html

```html
<!-- Headers ... -->

<section id="header">
	<div class="inner">
		<img src="{{ url_for('static', filename='images/logo-white.png') }}" style="width:40%; margin-top:-5%;"/>
		<h1>Welcome!</h1>
		<p>Can you guess the number I'm thinking of? Do you want to play?</p>
		<ul class="actions special">
			<li><a href="/playing" class="button scrolly">Play!</a></li>
		</ul>
	</div>
</section>

<!-- Scripts ... -->

```

**Note:** *There is no automatic testing for this exercise - you are responsible for writing and running your own tests!*
