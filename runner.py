from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Redirect to the desired web page
    return redirect("https://a42d-102-90-66-30.ngrok-free.app/")

# if __name__ == '__main__':
#     app.run(debug=True)
