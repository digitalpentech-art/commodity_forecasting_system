from app import create_app
from ml.preprocessing.data_processor import get_data_as_dataframe

app = create_app('dev')
with app.app_context():
    df = get_data_as_dataframe()
    print(f"DataFrame shape: {df.shape}")
    print(df.head())
