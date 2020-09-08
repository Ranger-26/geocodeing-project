from flask import Flask, render_template, request
from geocode import *
import pandas
from flask import send_file
from werkzeug.utils import secure_filename

app=Flask(__name__)


@app.route("/")
def index():
    return render_template('front.html')



@app.route("/show-df", methods=['POST'])
def success():
    try:
        if request.method=='POST':
            global x
            f=request.files['file']
            b=File(f)
            x=b.modify_file()
            x.to_csv('new')
            return render_template('front.html',text=x.to_html(),dow='hi.html')
    except:
           return render_template('front.html',text='Please make sure you have an address column in your csv file!')

@app.route('/download')
def download():
    return send_file('new',attachment_filename="yourfile.csv", as_attachment=True)







if __name__ == '__main__':
    app.debug=True
    app.run()
