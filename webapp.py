from flask import Flask
app = Flask(_name_)
@app.route('/')
def Index():
    return "Hello Flask App"
if _name_=="_main_":
    app.run(debug=True)