# Simplified Airline Booking System

# Models
from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number} ({self.origin} -> {self.destination})"

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='passengers')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

# Serializers
from rest_framework import serializers

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    flight_details = FlightSerializer(source='flight', read_only=True)

    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'flight', 'flight_details']

# Views/ViewSets
from rest_framework.viewsets import ModelViewSet

class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

# URLs
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'passengers', PassengerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

# README.md content
# Simplified Airline Booking System

## Project Overview
This Django REST framework-based API allows for managing flights and passengers in a simplified airline booking system. The application supports CRUD operations for flights and passengers.

## Models
1. **Flight**:
   - `flight_number`: Unique identifier for the flight.
   - `departure`: Date and time of departure.
   - `arrival`: Date and time of arrival.
   - `origin`: Origin airport.
   - `destination`: Destination airport.
   - `capacity`: Total number of seats available.

2. **Passenger**:
   - `first_name`, `last_name`, `email`, `phone_number`: Passenger details.
   - `flight`: Foreign key relating a passenger to a specific flight.

## Endpoints
- `/api/flights/`: List all flights, create a new flight.
- `/api/flights/{id}/`: Retrieve, update, or delete a specific flight.
- `/api/passengers/`: List all passengers, create a new passenger.
- `/api/passengers/{id}/`: Retrieve, update, or delete a specific passenger.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd simplified-airline-booking
   ```
2. Set up the virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install django djangorestframework
   ```
3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
5. Test the API endpoints using Postman or any API client.

## Optional Enhancements
- Filtering passengers by flight using query parameters.
- Pagination for list endpoints.

## Submission
Ensure the project is pushed to a GitHub repository named with your student ID. Include this README file in the root of the repository.
