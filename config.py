import os

class config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'kunci-rahasia-perpus-2026')

    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '') 
    DB_NAME = os.environ.get('DB_NAME', 'db_perpustakaan_flask')