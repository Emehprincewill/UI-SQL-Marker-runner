from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Redirect to the desired web page
    return redirect("https://61eb-197-210-84-202.ngrok-free.app")

# if __name__ == '__main__':
#     app.run(debug=True)
