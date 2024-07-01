# API Development and Documentation Final Project

## Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

> View the [Frontend README](./frontend/README.md) for more details.

### Learning Notes

In order for the requests to be processed properly, 
CORS utilizes headers to specify what the server will allow:

Access-Control-Allow-Origin
  What client domains can access its resources. For any domain use *
Access-Control-Allow-Credentials
  Only if using cookies for authentication - in which case its value must be true
Access-Control-Allow-Methods
  List of HTTP request types allowed
Access-Control-Allow-Headers
  List of http request header values the server will allow, particularly useful if you use any custom headers

### Development Notes 

pip install aniso8601 --upgrade  
pip install Click --upgrade  
pip install Flask --upgrade  
pip install Flask-Cors --upgrade  
pip install Flask-RESTful --upgrade  
pip install Flask-SQLAlchemy --upgrade  
pip install itsdangerous --upgrade  
pip install Jinja2 --upgrade  
pip install MarkupSafe --upgrade  
pip install psycopg2-binary --upgrade  
pip install pytz --upgrade  
pip install six --upgrade  
pip install SQLAlchemy --upgrade  
pip install Werkzeug --upgrade  

cd C:\ReSkill\Python\Trivia79\Trivia7\
cd C:\ReSkill\Python\Trivia79\Trivia7\basicFlaskapp7
python -m virtualenv envTrivia7
cd envTrivia7\Scripts
activate.bat
cd C:\ReSkill\Python\Trivia79\Trivia7\basicFlaskapp7
__init__.py		
		
 migrate Commands
  flask db init
  flask db migrate -m " Comments "
  flask db upgrade

Running the flask app

> set FLASK_APP=basicFlaskapp
> set FLASK_ENV=development
> __init__.py

curl https://pokeapi.co/api/v2/move/47 | jq "-"

curl https://pokeapi.co/api/v2/move/47 | jq "."

curl https://pokeapi.co/api/v2/move/47 | jq (.)

curl https://pokeapi.co/api/v2/move/47 -o C:\ReSkill\Python\Trivia7\basicFlaskapp\curlfile.txtcurl https://pokeapi.co/api/v2/move/47 | jq "-"

curl https://pokeapi.co/api/v2/move/47 | jq "."

curl https://pokeapi.co/api/v2/move/47 | jq (.)

curl https://pokeapi.co/api/v2/move/47 -o C:\ReSkill\Python\Trivia7\basicFlaskapp\curlfile.txt

curl http://127.0.0.1:5000/  | jq "."
http://127.0.0.1:5000/smiley