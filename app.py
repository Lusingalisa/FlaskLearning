from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# defining the function for the route we have just created.
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)