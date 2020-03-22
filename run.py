"""
Module 1 launcher
"""
from app import APP

if __name__ == "__main__":
    APP.run(host=APP.config["FLASK_HOST_ADDRESS"], port=APP.config["FLASK_PORT"])
