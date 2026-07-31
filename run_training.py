from app import create_app
from ml.training.trainer import train_model

app = create_app('dev')
with app.app_context():
    model_path = train_model()
    if model_path:
        print(f"Training successful. Model saved to: {model_path}")
    else:
        print("Training failed.")
