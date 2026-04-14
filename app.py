from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from models import db, Workout, Exercise, WorkoutExercise
from schemas import (workout_schema, workouts_schema, 
                     exercise_schema, exercises_schema, 
                     workout_exercise_schema)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# WORKOUT ENDPOINTS
@app.route('/workouts', methods=['GET', 'POST'])
def workouts():
    if request.method == 'GET':
        return make_response(workouts_schema.dump(Workout.query.all()), 200)
    
    if request.method == 'POST':
        try:
            data = workout_schema.load(request.get_json())
            new_workout = Workout(**data)
            db.session.add(new_workout)
            db.session.commit()
            return make_response(workout_schema.dump(new_workout), 201)
        except Exception as e:
            return make_response({"errors": str(e)}, 400)

@app.route('/workouts/<int:id>', methods=['GET', 'DELETE'])
def workout_by_id(id):
    workout = Workout.query.get_or_404(id)
    if request.method == 'GET':
        return make_response(workout_schema.dump(workout), 200)
    
    if request.method == 'DELETE':
        db.session.delete(workout)
        db.session.commit()
        return make_response({}, 204)

# EXERCISE ENDPOINTS
@app.route('/exercises', methods=['GET', 'POST'])
def exercises():
    if request.method == 'GET':
        return make_response(exercises_schema.dump(Exercise.query.all()), 200)
    
    if request.method == 'POST':
        try:
            data = exercise_schema.load(request.get_json())
            new_ex = Exercise(**data)
            db.session.add(new_ex)
            db.session.commit()
            return make_response(exercise_schema.dump(new_ex), 201)
        except Exception as e:
            return make_response({"errors": str(e)}, 400)

# JOIN TABLE ENDPOINT
@app.route('/workouts/<int:w_id>/exercises/<int:e_id>/workout_exercises', methods=['POST'])
def add_ex_to_workout(w_id, e_id):
    Workout.query.get_or_404(w_id)
    Exercise.query.get_or_404(e_id)
    try:
        data = workout_exercise_schema.load(request.get_json())
        new_we = WorkoutExercise(workout_id=w_id, exercise_id=e_id, **data)
        db.session.add(new_we)
        db.session.commit()
        return make_response(workout_exercise_schema.dump(new_we), 201)
    except Exception as e:
        return make_response({"errors": str(e)}, 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)