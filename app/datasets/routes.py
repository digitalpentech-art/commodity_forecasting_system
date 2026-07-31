import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.datasets.mock_pandas import pd
from app import db
from app.models.dataset import Dataset

datasets_bp = Blueprint('datasets', __name__)
UPLOAD_FOLDER = 'data/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@datasets_bp.route('/datasets', methods=['GET'])
@login_required
def list_datasets():
    datasets = Dataset.query.all()
    return render_template('datasets/list.html', datasets=datasets)

@datasets_bp.route('/datasets/upload', methods=['GET', 'POST'])
@login_required
def upload_dataset():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            new_dataset = Dataset(filename=file.filename)
            db.session.add(new_dataset)
            db.session.commit()
            flash('Dataset uploaded successfully')
            return redirect(url_for('datasets.list_datasets'))
        flash('Invalid file format. Please upload a CSV.')
    return render_template('datasets/upload.html')

@datasets_bp.route('/datasets/preview/<int:id>', methods=['GET'])
@login_required
def preview_dataset(id):
    dataset = Dataset.query.get_or_404(id)
    filepath = os.path.join(UPLOAD_FOLDER, dataset.filename)
    df = pd.read_csv(filepath)
    return render_template('datasets/preview.html', data=df.head().to_html())
