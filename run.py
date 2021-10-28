from app import create_app
from flask import Flask
import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port, debug=False)