from sqlalchemy import Enum

# Enum for user roles
UserRoleEnum = Enum("admin", "trainer", "user", name="user_roles")

# Enum for training goals (e.g., user's goals or routine objectives)
TrainingGoalEnum = Enum("weight_loss", "muscle_gain", "toning", name="training_goals")

# Enum for routine types (whether predefined by the system or customized by a trainer)
RoutineTypeEnum = Enum("predefined", "custom", name="routine_types")

# Enum for difficulty levels of routines or plans
DifficultyLevelEnum = Enum(
    "beginner", "intermediate", "advanced", name="difficulty_levels"
)

# Enum for routine statuses (to track if a routine is active, completed, or paused)
RoutineStatusEnum = Enum("active", "completed", "paused", name="routine_statuses")

# Enum for exercises types (to get a classification of the exercises)
ExerciseTypeEnum = Enum(
    "strength", "cardio", "mobility", "flexibility", name="exercise_type"
)

# Enum for the type of count an exercise
CountTypeEnum = Enum("repetitions", "time", name="count_types")
