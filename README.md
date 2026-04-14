# Workout Tracking API

A Flask backend API for personal trainers to manage workouts and exercises.

## Setup Instructions
1. Run `pipenv install` to install dependencies.
2. Enter the shell: `pipenv shell`.
3. Initialize Database:
   ```bash
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade 