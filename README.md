# AirlineBookingSystem_138464

## Project Overview

This project is an Airline Booking System designed to manage flight bookings for customers and airlines. The system allows users to search for flights, book tickets, view flight details, and manage reservations. It also provides functionalities for airlines to manage flight schedules, pricing, and customer bookings.

## Features

- **Customer Features:**
  - **Flight Search**: Search for flights by origin, destination, date, and other filters.
  - **Booking Management**: Make flight reservations, view booking details, and cancel bookings.
  - **User Authentication**: Secure login and account creation for users.
  - **Flight Information**: View flight schedules, status, and availability.

- **Airline Admin Features:**
  - **Flight Schedule Management**: Add, update, and delete flight schedules.
  - **Pricing Management**: Set and update pricing for flights.
  - **Booking Overview**: View customer bookings, including booking details and payment status.

- **Payment Integration**: Integration with payment gateways to handle booking payments.

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript
  - React.js (for dynamic and interactive user interface)
  - Bootstrap (for responsive design)

- **Backend**:
  - Node.js with Express.js (for handling API requests)
  - MongoDB (for storing flight and booking data)

- **Payment Gateway**: Stripe (for processing payments)

- **Authentication**: JWT (JSON Web Tokens) for secure user authentication.

## System Architecture

The system is designed as a client-server model with the following architecture:

1. **Frontend (Client)**: The web interface where users (both customers and airline admins) interact with the system to search for flights, make bookings, and manage accounts.
2. **Backend (Server)**: A Node.js server that handles user requests, interacts with the database, processes bookings, and manages authentication.
3. **Database**: MongoDB is used to store data such as flight schedules, user information, bookings, and payment records.

## Installation

### Prerequisites

1. **Node.js**: Install Node.js from [here](https://nodejs.org/).
2. **MongoDB**: Install MongoDB from [here](https://www.mongodb.com/try/download/community).
3. **Stripe Account**: Sign up for a Stripe account for payment integration.

### Steps to Set Up

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/airline-booking-system.git
   cd airline-booking-system
