from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Redirect to the desired web page
    return redirect("https://6590-197-210-78-111.ngrok-free.app/")

# if __name__ == '__main__':
#     app.run(debug=True)
