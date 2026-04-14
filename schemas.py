from marshmallow import Schema, fields, validate
from models import db

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    # Schema Validation 1: Length
    name = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    # Schema Validation 2: Specific choices
    category = fields.Str(required=True, validate=validate.OneOf(["Strength", "Cardio", "Flexibility", "Yoga"]))
    equipment_needed = fields.Bool()

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    # Schema Validation 3: Range
    reps = fields.Int(validate=validate.Range(min=1, max=100))
    sets = fields.Int(validate=validate.Range(min=1, max=20))
    duration_seconds = fields.Int(validate=validate.Range(min=1))
    exercise = fields.Nested(ExerciseSchema, only=("name", "category"))

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()
    # Nested Serialization (Excelled)
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema))

# Pre-init instances
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()