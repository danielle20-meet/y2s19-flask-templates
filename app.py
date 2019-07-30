from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def home_page(day=False ,foods= ["Ice Cream","Watermelon","Apple"]):
    return render_template("index.html",day=day,foods=foods)

if __name__ == '__main__':
   app.run(debug =True)
