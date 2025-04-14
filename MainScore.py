from flask import Flask
from Utils import SCORES_FILE_NAME

# this will be using flask so i can access it from the web

app = Flask(__name__)

def get_score_from_file():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            return file.read().strip()
    except (FileNotFoundError, ValueError):
        return None

@app.route('/')
def score_server():
    score = get_score_from_file()
    if score is not None:
        return f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{score}</div></h1>
            </body>
        </html>
        '''
    else:
        return '''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{ERROR}</div></h1>
            </body>
        </html>
        '''

def get_score_from_file():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            return file.read().strip()
    except (FileNotFoundError, ValueError):
        return None

if __name__ == '__main__':
    from Utils import create_scores_file
    create_scores_file()
    app.run(host='0.0.0.0', port=5000)