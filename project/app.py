from flask import Flask, render_template, request, flash, redirect, url_for
from forms import InfoForm
import os
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        gender = form.gender.data
        phone = form.phone.data
        birth_date = form.birth_date.data
        information = form.information.data
        excel_file = form.excel_file.data

        if excel_file and allowed_file(excel_file.filename):
            filename = secure_filename(excel_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            excel_file.save(file_path)

            # Read the Excel file
            df = pd.read_excel(file_path)
            table_data = df.to_html(classes='table table-striped', index=False)

            return render_template('display_table.html', table_data=table_data)
        else:
            flash('Uploaded file is not an Excel file or has an unsupported extension.', 'error')

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
