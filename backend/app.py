from backend import app
from backend.models.database import *


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
