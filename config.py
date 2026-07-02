import os

class Config:
    # Secret key used for protecting session data (crucial for backend security)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this-key-12345'
    
    # Define the location of our SQLite database file inside the project directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    
    # Disable tracking modifications to save system resources and memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False