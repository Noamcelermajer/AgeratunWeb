from flask import Flask
from routes.appointment_routes import app

if __name__ == '__main__':
    app.run(debug=True)
