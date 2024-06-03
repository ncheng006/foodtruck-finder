# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from math import sin, cos, sqrt, atan2, radians

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

R = 6373.0

def calculate_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

@app.route('/api/foodtrucks', methods=['GET'])
def getfoodtrucks():
    try:
        user_lat = float(request.args.get('lat'))
        user_lon = float(request.args.get('lon'))
        radius = float(request.args.get('radius', 5))
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid latitude or longitude'}), 400
    conn = sqlite3.connect('foodtrucks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, Latitude, Longitude FROM foodtrucks")
    rows = cursor.fetchall()
    conn.close()

    nearby_trucks = []
    for row in rows:
        name, lat, lon = row
        distance = calculate_distance(user_lat, user_lon, lat, lon)
        if distance <= radius:
            nearby_trucks.append({'name': name, 'latitude': lat, 'longitude': lon, 'distance': distance})

    nearby_trucks = sorted(nearby_trucks, key=lambda x: x['distance'])

    return jsonify(nearby_trucks)

if __name__ == '__main__':
    app.run(debug=True)
