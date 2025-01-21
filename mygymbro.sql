BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	last_name VARCHAR(100) NOT NULL, 
	dni VARCHAR(20) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	password TEXT NOT NULL,
	role VARCHAR(7) NOT NULL, 
	birth_date DATE, 
	gender VARCHAR(10), 
	height FLOAT, 
	initial_weight FLOAT, 
	training_goal VARCHAR(11), 
	subscription_status BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (dni), 
	UNIQUE (email), 
	CONSTRAINT user_roles CHECK (role IN ('admin', 'trainer', 'user')), 
	CONSTRAINT training_goals CHECK (training_goal IN ('weight_loss', 'muscle_gain', 'toning')), 
	CHECK (subscription_status IN (TRUE, FALSE))
);
INSERT INTO users VALUES(1,'raul','raul','awefgasgr','raul','scrypt:32768:8:1$GjxYqMNZz07bHZzo$cc41d2f5f703cc2101892a19d0763eae2465d86bb255cbd190504f06fd48be120b607b8a53fbbca1a54cfaa56a50b592040d73d83c4b4dc62b6b4aecf99d202d','admin',NULL,NULL,NULL,NULL,NULL,TRUE);
INSERT INTO users VALUES(2,'pablo','pablo','asdfwf','pablo','scrypt:32768:8:1$zJCJBoXjDqN1RMKn$b3f45dc4660b71749432a9c24154667de54699ce2f1cfd9ef5c73249848969018b02e79de77e33a76fe8e1d5b9476db3832359cbe3bf4dad4e9df3d09eae3221','user',NULL,NULL,NULL,NULL,NULL,TRUE);
INSERT INTO users VALUES(3,'carlos','carlos','13574687E','carlos','scrypt:32768:8:1$RW326AkDv7dJSPA1$eb3ecb13e3f0a307e8e495351a2f6ea5372d7ffe6ea0dca1216f166c40040bafc72893404386617c67e906a2188dbfc7f5e2a1137499002000baa5f5802b5394','user',NULL,NULL,NULL,NULL,NULL,TRUE);
INSERT INTO users VALUES(4,'admin','admin','admin','admin','scrypt:32768:8:1$MJ1meou84wfuLw0q$325a61a38b28a6a0022fa603182ce17425748b9b5fe23b1e38dbaaa550d2a3fb917c4c3d1561042cff61f4ef06aa3337e5bcb8a9864c76a2dbec08d9060f0a4f','user',NULL,NULL,NULL,NULL,NULL,TRUE);
CREATE TABLE IF NOT EXISTS exercises (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	description TEXT, 
	category VARCHAR(11), 
	count_type VARCHAR(11) NOT NULL, 
	count_value INTEGER, 
	equipment_required BOOLEAN, 
	equipment_optional BOOLEAN, 
	equipment_list VARCHAR(200), 
	recommended_series INTEGER, 
	suggested_weight FLOAT, 
	rest_time INTEGER, 
	visual_demo VARCHAR(200), 
	execution_tips TEXT, 
	PRIMARY KEY (id), 
	CONSTRAINT exercise_type CHECK (category IN ('strength', 'cardio', 'mobility', 'flexibility')), 
	CONSTRAINT count_types CHECK (count_type IN ('repetitions', 'time')), 
	CHECK (equipment_required IN (TRUE, FALSE)),
    CHECK (equipment_optional IN (TRUE, FALSE))
);
INSERT INTO exercises VALUES(1,'Bench Press','The bench press is a strength exercise that primarily targets the chest, triceps, and shoulders. It is performed lying on a flat bench while lifting a barbell with weights.','strength','repetitions',8,TRUE,FALSE,'barbell, weight plates, flat bench',4,0.0,90,NULL,'Keep your feet firmly on the ground, lower the bar slowly to your chest, and push up without locking your elbows.');
INSERT INTO exercises VALUES(2,'Jump Rope','High-intensity exercise to improve cardiovascular endurance.','cardio','time',300,FALSE,FALSE,'None',3,0.0,60,NULL,'Keep your core engaged and land softly on your toes.');
INSERT INTO exercises VALUES(3,'Pull-Ups','Builds overall back strength and muscle definition.','strength','repetitions',10,TRUE,TRUE,'Pull-up Bar',3,0.0,120,NULL,'Focus on pulling with your back, not your arms.');
INSERT INTO exercises VALUES(4,'Standing Forward Bend','Stretches the hamstrings and improves flexibility.','mobility','time',60,FALSE,FALSE,'None',2,0.0,30,NULL,'Bend at the hips and keep your legs straight.');
INSERT INTO exercises VALUES(5,'Bodyweight Squats','Targets the quadriceps and glutes for lower body strength.','strength','repetitions',15,FALSE,FALSE,'None',4,0.0,60,NULL,'Keep your knees aligned with your toes.');
INSERT INTO exercises VALUES(6,'Dumbbell Shoulder Press','Engages the shoulders and core.','strength','repetitions',8,TRUE,FALSE,'Dumbbells',4,0.0,90,NULL,'Maintain a straight back while lifting.');
INSERT INTO exercises VALUES(7,'Running','Increases heart rate and burns calories.','cardio','time',600,TRUE,FALSE,'None',1,0.0,0,NULL,'Maintain a steady pace and focus on breathing.');
INSERT INTO exercises VALUES(8,'Bicep Curls','Strengthens the biceps and forearms.','strength','repetitions',12,TRUE,FALSE,'Dumbbells',3,0.0,60,NULL,'Keep your elbows close to your sides.');
INSERT INTO exercises VALUES(9,'Crunches','Targets the core muscles.','strength','repetitions',15,FALSE,FALSE,'None',3,0.0,30,NULL,'Keep your core tight and do not strain your neck.');
INSERT INTO exercises VALUES(10,'Lunging Hip Flexor Stretch','Stretches the hip flexors and lower back.','flexibility','time',45,FALSE,FALSE,'None',2,0.0,20,NULL,'Hold the stretch and breathe deeply.');
INSERT INTO exercises VALUES(11,'Kettlebell Swings','Strengthens the core and lower back.','strength','repetitions',10,TRUE,FALSE,'Kettlebell',4,0.0,90,NULL,'Swing the kettlebell with your hips, not your arms.');
INSERT INTO exercises VALUES(12,'Shoulder Dislocates','Improves shoulder and upper back mobility.','mobility','time',60,FALSE,FALSE,'None',3,0.0,30,NULL,'Focus on controlled movements.');
INSERT INTO exercises VALUES(13,'Deadlift','Builds leg strength and stability.','strength','repetitions',12,TRUE,FALSE,'Barbell',4,0.0,120,NULL,'Keep your back straight while lifting.');
INSERT INTO exercises VALUES(14,'Burpees','Burns calories and strengthens the legs.','cardio','time',300,FALSE,FALSE,'None',3,0.0,60,NULL,'Maintain a quick pace and steady rhythm.');
INSERT INTO exercises VALUES(15,'Dips','Targets triceps and shoulders.','strength','repetitions',12,TRUE,FALSE,'Parallel Bars',3,0.0,90,NULL,'Lower yourself slowly to avoid injury.');
INSERT INTO exercises VALUES(16,'Chest Stretch','Stretches the chest and shoulders.','flexibility','time',60,FALSE,FALSE,'None',2,0.0,20,NULL,'Hold the stretch without bouncing.');
CREATE TABLE IF NOT EXISTS training_plans (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	description TEXT, 
	objective VARCHAR(11), 
	duration INTEGER NOT NULL, 
	weekly_frequency INTEGER NOT NULL, 
	difficulty_level VARCHAR(12), 
	sequence JSON, 
	additional_guidelines TEXT, 
	assigned_to INTEGER NOT NULL, 
	created_by INTEGER NOT NULL, 
	start_date DATE, 
	estimated_end_date DATE, 
	status VARCHAR(20) NOT NULL, 
	trainer_notes TEXT, 
	PRIMARY KEY (id), 
	CONSTRAINT training_goals CHECK (objective IN ('weight_loss', 'muscle_gain', 'toning')), 
	CONSTRAINT difficulty_levels CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')),
	FOREIGN KEY(assigned_to) REFERENCES users (id),
	FOREIGN KEY(created_by) REFERENCES users (id)
);
INSERT INTO training_plans VALUES(1,'Gorilla Chest','This training plan is to get the 100 kg on chest press','muscle_gain',3,2,'intermediate',NULL,NULL,1,1,NULL,NULL,'active',NULL);
INSERT INTO training_plans VALUES(2,'Muscle Gain Program','A 12-week plan focused on building muscle.','muscle_gain',12,5,'advanced',NULL,NULL,2,1,'2024-11-20','2025-02-20','active','Focus on compound exercises for maximum results.');
CREATE TABLE IF NOT EXISTS routines (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	description TEXT, 
	objective VARCHAR(11), 
	routine_type VARCHAR(10), 
	training_plan_id INTEGER, 
	series INTEGER, 
	repetitions INTEGER, 
	recommended_weight FLOAT, 
	weekly_frequency INTEGER, 
	difficulty_level VARCHAR(12), 
	created_by INTEGER, 
	assigned_to INTEGER, 
	current_progress VARCHAR(12), 
	created_at TIMESTAMP,
	start_date DATE, 
	end_date DATE, 
	notes TEXT, 
	PRIMARY KEY (id), 
	CONSTRAINT training_goals CHECK (objective IN ('weight_loss', 'muscle_gain', 'toning')), 
	CONSTRAINT routine_types CHECK (routine_type IN ('predefined', 'custom')), 
	FOREIGN KEY(training_plan_id) REFERENCES training_plans (id), 
	CONSTRAINT difficulty_levels CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')), 
	FOREIGN KEY(created_by) REFERENCES users (id), 
	FOREIGN KEY(assigned_to) REFERENCES users (id), 
	CONSTRAINT difficulty_levels CHECK (current_progress IN ('beginner', 'intermediate', 'advanced'))
);
INSERT INTO routines VALUES(1,'Full Body Strength - Beginner','Full body routine focusing on building strength for beginners.','muscle_gain','predefined',1,NULL,NULL,NULL,3,'beginner',1,NULL,NULL,'2024-11-18 19:11:33.335603','2024-11-20',NULL,NULL);
CREATE TABLE IF NOT EXISTS routine_exercises (
	routine_id INTEGER NOT NULL, 
	exercise_id INTEGER NOT NULL, 
	series INTEGER, 
	repetitions INTEGER, 
	time FLOAT, 
	weight FLOAT, 
	PRIMARY KEY (routine_id, exercise_id), 
	FOREIGN KEY(routine_id) REFERENCES routines (id), 
	FOREIGN KEY(exercise_id) REFERENCES exercises (id)
);
INSERT INTO routine_exercises VALUES(1,1,4,12,NULL,40.0);
INSERT INTO routine_exercises VALUES(1,2,3,10,NULL,50.0);
INSERT INTO routine_exercises VALUES(1,3,3,8,NULL,0.0);
INSERT INTO routine_exercises VALUES(1,4,2,NULL,300.0,NULL);
INSERT INTO routine_exercises VALUES(1,5,4,15,NULL,0.0);
CREATE TABLE IF NOT EXISTS progress_records (
	id INTEGER NOT NULL, 
	record_date DATE, 
	exercise_id INTEGER NOT NULL, 
	routine_id INTEGER NOT NULL, 
	training_plan_id INTEGER, 
	series_completed INTEGER, 
	repetitions_per_series INTEGER, 
	time_per_series FLOAT, 
	weight_used FLOAT, 
	user_notes TEXT, 
	trainer_notes TEXT, 
	exercise_status VARCHAR(20) NOT NULL, 
	perceived_effort INTEGER, user_id INTEGER NOT NULL DEFAULT 1, 
	PRIMARY KEY (id), 
	FOREIGN KEY(exercise_id) REFERENCES exercises (id), 
	FOREIGN KEY(routine_id) REFERENCES routines (id), 
	FOREIGN KEY(training_plan_id) REFERENCES training_plans (id)
);
INSERT INTO progress_records VALUES(1,'2024-11-04',1,1,1,3,9,90.0,65.0,'I should use less weight','so much effort','completed',98,1);
INSERT INTO progress_records VALUES(2,'2024-11-23',1,2,1,4,12,NULL,50.0,'Felt strong during the session.','Increase weight by 5kg next session.','complete',7,1);
CREATE TABLE IF NOT EXISTS alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE IF NOT EXISTS _alembic_tmp_progress_records (
	id INTEGER NOT NULL, 
	record_date DATE, 
	exercise_id INTEGER NOT NULL,
	routine_id INTEGER NOT NULL, 
	training_plan_id INTEGER, 
	series_completed INTEGER, 
	repetitions_per_series INTEGER, 
	time_per_series FLOAT, 
	weight_used FLOAT, 
	user_notes TEXT, 
	trainer_notes TEXT, 
	exercise_status VARCHAR(20) NOT NULL, 
	perceived_effort INTEGER, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT fk_progress_user_id FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(training_plan_id) REFERENCES training_plans (id), 
	FOREIGN KEY(routine_id) REFERENCES routines (id), 
	FOREIGN KEY(exercise_id) REFERENCES exercises (id)
);
COMMIT;
