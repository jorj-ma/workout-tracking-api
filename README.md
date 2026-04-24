# Workout Tracking API

A Flask backend API for personal trainers to manage workouts and exercises.

## Setup Instructions
1. Clone the repository
2. Navigate into the repo
3. Run `pipenv install` to install dependencies.
4. Enter the shell: `pipenv shell`.
5. Initialize Database:
   ```bash
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade 