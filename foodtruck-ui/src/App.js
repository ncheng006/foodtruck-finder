import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, TextField, Button, List, ListItem, ListItemText } from '@mui/material';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon-2x.png',
  iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
});

const App = () => {
  const [location, setLocation] = useState({ lat: '', lon: '' });
  const [radius, setRadius] = useState(5);
  const [foodtrucks, setFoodtrucks] = useState([]);
  const [mapCenter, setMapCenter] = useState([37.7749, -122.4194]);
  const fetchFoodTrucks = async (lat, lon, radius) => {
    try {
      const response = await axios.get(`http://localhost:5000/api/foodtrucks`, {
        params: { lat, lon, radius }
      });
      setFoodtrucks(response.data);
      setMapCenter([lat, lon]);

    } catch (error) {
      console.error("Error fetching food trucks", error);
    }
  };

  const handleLocationChange = (e) => {
    setLocation({ ...location, [e.target.name]: e.target.value });
  };

  const handleRadiusChange = (e) => {
    setRadius(e.target.value);
  };

  const handleSubmit = () => {
    fetchFoodTrucks(location.lat, location.lon, radius);
  };

  const handleUseCurrentLocation = () => {
    navigator.geolocation.getCurrentPosition((position) => {
      const { latitude, longitude } = position.coords;
      setLocation({ lat: latitude, lon: longitude });
      fetchFoodTrucks(latitude, longitude, radius);
    });
  };

  return (
    <Container>
      <h1>Food Truck Finder</h1>
      <TextField name="lat" label="Latitude" value={location.lat} onChange={handleLocationChange} />
      <TextField name="lon" label="Longitude" value={location.lon} onChange={handleLocationChange} />
      <TextField label="Radius (km)" value={radius} onChange={handleRadiusChange} />
      <Button onClick={handleSubmit}>Find Food Trucks</Button>
      <Button onClick={handleUseCurrentLocation}>Use Current Location</Button>
      <MapContainer center={mapCenter} zoom={13} style={{ height: "400px", width: "100%" }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        {foodtrucks.map((truck, index) => (
          <Marker key={index} position={[truck.latitude, truck.longitude]}>
            <Popup>
              {truck.name} <br /> Distance: {truck.distance.toFixed(2)} km
            </Popup>
          </Marker>
        ))}
      </MapContainer>
      <List>
        {foodtrucks.map((truck, index) => (
          <ListItem key={index}>
            <ListItemText primary={truck.name} secondary={`Distance: ${truck.distance.toFixed(2)} km`} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default App;