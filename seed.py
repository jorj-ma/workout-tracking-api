from app import app
from models import db, Workout, Exercise, WorkoutExercise
from datetime import date

with app.app_context():
    print("Clearing DB...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding Exercises...")
    e1 = Exercise(name="Deadlift", category="Strength", equipment_needed=True)
    e2 = Exercise(name="Yoga Flow", category="Yoga", equipment_needed=False)
    e3 = Exercise(name="Sprints", category="Cardio", equipment_needed=False)
    db.session.add_all([e1, e2, e3])
    
    print("Seeding Workouts...")
    w1 = Workout(date=date.today(), duration_minutes=45, notes="Focus on form")
    db.session.add(w1)
    db.session.commit()

    print("Connecting them...")
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, reps=5, sets=3)
    db.session.add(we1)
    db.session.commit()
    print("Seeding complete!")