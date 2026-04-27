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
## Running the API server
The CLI client expects the backend API to be available at `http://localhost:5000`.
Start the server ny running:
```
python3 app.py
```
## Testing endpoints
Based on the current CLI, the endpoints include:
- `GET /workouts` - list available workouts
- `POST /workouts` - add workout
- `GET /workouts/<id>` - get workout by id
- `DELETE /workout/<id>` - delete workout by id
- `GET /exercicses` - list available exercises
- `POST /exercises` - add exercise
- `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` - add exercise to workout

## Author
- Anzigale George

## Contributions
Contributions are welcome. Open an issue with  a clear description of the proposed improvements.

## License
The code is open for use.
