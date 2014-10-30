# Configuration

# Flask
DEBUG = True

UPLOAD_FOLDER = "/tmp/uploads"
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # 16MB
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/db.sqlite"
