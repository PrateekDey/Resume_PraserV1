import os
import json
import CleanData as cd
import Section as sc
import ExtractEdu as ee
from werkzeug.utils import secure_filename

from flask import Flask, render_template, request

app = Flask(__name__)

with open('config.json', 'r') as c:
    params = json.load(c)['params']


@app.route('/')
def index():
    return render_template('index.html')


app.config['UPLOAD_FOLDER'] = params['upload_location']


def converttotext(s):
    return '\n'.join(s)


@app.route("/extract", methods=['GET', 'POST'])
def extract():
    if request.method == 'POST':
        f = request.files['file1']
        loc = os.path.join(
           app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(loc)
        cdf = cd.getfile(loc)
        info = sc.division(cdf)
        expiernce = converttotext(info['EXPERIENCE'])
        edu = ee.extract(info['EDUCATION'])
        print(edu.keys())
        return render_template('resume.html', phd=edu['PH.D'], master=edu['M.TECH'], bachelor=edu['B.SC'], secondary=edu['SECONDARY'])


if __name__ == '__main__':
    app.run(debug=True)
