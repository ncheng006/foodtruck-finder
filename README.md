# Food Truck Finder

Food Truck Finder is a web application that helps you discover nearby food trucks in Palo Alto. The application consists of a backend API built with Flask and a frontend built with React.js.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Testing](#testing)
- [Usage](#usage)

## Requirements

- Python 3.7+
- Node.js 12+

## Setup
1. Clone the Repository, foodtruck-finder is the backend and foodtruck-ui built in Flask is the frontend built in React. You will need to create two terminals to start both servers locally.
### Backend
1. CD into foodtruck-finder
2. Create a virtual environment and activate it:
  - python3 -m venv venv
  - source venv/bin/activate
3. Install the required Python packages:
   - pip install -r requirements.txt
4. Set up the SQLite database:
  - python setup_db.py
5. Start the Flask Server
  - python app.py

### Frontend
1. CD into foodtruck-ui
2. npm install
3. npm start

### Testing
1. CD into foodtruck-finder
2. pytest unit-test.py

### Usage
1. CD into foodtruck-finder and start the Flask Server
  - python app.py
2. CD into foodtruck-ui and start the React Server
  - npm start

