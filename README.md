# WatchGames - Your Source for Video Game Information


**WatchGames** is a modern website and API for searching and tracking video games. You can find information about your favorite games, read reviews, learn about developers and publishers. The project uses Django REST framework (DRF) to create the API, SQLite3 for the database, and Django-Josuer for token-based authentication.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Docker Compose](#docker-compose)
- [Swagger Documentation](#swagger-documentation)
- [Additional Configuration](#additional-configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/WatchGames.git
   cd WatchGames
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Open your web browser and go to http://localhost:8000.

## Usage
Registration and Authentication
To access the API, you need to register and obtain an authentication token:

Go to the registration page: http://localhost:8000/auth/register/.

Fill out the registration form, providing a username, email address, and password.

After successful registration, you will receive an authentication token.

## API Endpoints
The API provides the following endpoints:

/api/games/: Get a list of all games and create new games.

/api/games/{game_id}/: Get, update, and delete game information by game_id.

/api/developers/: Get a list of all developers and create new developers.

/api/developers/{developer_id}/: Get, update, and delete developer information by developer_id.

/api/publishers/: Get a list of all publishers and create new publishers.

/api/publishers/{publisher_id}/: Get, update, and delete publisher information by publisher_id.

/api/reviews/: Get a list of all reviews and create new reviews.

/api/reviews/{review_id}/: Get, update, and delete review information by review_id.

## Examples
Get a list of all games:

bash
Copy code
curl -X GET http://localhost:8000/api/games/
Create a new game:

bash
Copy code
curl -X POST http://localhost:8000/api/games/ -d 'name=Game Name&release_date=2023-01-01'
Get information about a game with ID 1:

bash
Copy code
curl -X GET http://localhost:8000/api/games/2/
Update information about a game with ID 1:

bash
Copy code
curl -X PUT http://localhost:8000/api/games/2/ -d 'name=Updated Game Name'
Delete a game with ID 1:

bash
Copy code
curl -X DELETE http://localhost:8000/api/games/2/
Note: Replace http://localhost:8000 with the appropriate URL for your server.

## Docker Compose
You can also run the project using Docker Compose. Simply follow these steps:

Install Docker and Docker Compose if not already installed.

Navigate to the project directory and run:

bash
Copy code
docker-compose up
Open your web browser and go to http://localhost:8000.

## Swagger Documentation
The API includes Swagger documentation, which you can access at http://localhost:8000/swagger/. This documentation provides detailed information about the available endpoints and how to use them.

## Additional Configuration
For more detailed project configuration and feature management, please refer to the settings.py file.

## Contributing
If you would like to contribute to the project, please read our Contribution Guide before creating a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



This README provides comprehensive information about your project, including installation, usage, API endpoints, examples, Docker Compose setup, Swagger documentation, and more. Users will find it helpful to understand and utilize your project effectively.