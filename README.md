# Workout Tracking API

A Flask backend API for personal trainers to manage workouts and exercises.

## Prerequisites
- Python 3.8+
- `pipenv`

## Installation
Clone the repository then run:
```
cd workout-tracking-api
```
```
pipenv install
```
```
pipenv shell
```
## Initialize Database:
   ```
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
```
## Populate the database with seed data
Run:
```
python3 seed.py
```
## Testing endpoits
Use an API client like curl or postman to test the endpoints


## Author
- Anzigale George

## Contributions
Contributions are welcome. Open an issue with  a clear description of the proposed improvements.

## License
The code is open for use.
