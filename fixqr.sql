
-- this is updated to work properly now, and to load new fake dat
CREATE DATABASE FREELANCE_DB_4;
USE FREELANCE_DB_4;
CREATE TABLE USER(
    user_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE, -- make sure its unique emails
    phone_number BIGINT, -- might replace for text later
    PRIMARY KEY (user_id)
);

CREATE TABLE REQUEST(
    request_id INT,
    user_id INT,
    submitted_date DATE NOT NULL,
    foundmethod VARCHAR(255),
    PRIMARY KEY (request_id),
    FOREIGN KEY (user_id) REFERENCES USER(user_id)
);

CREATE TABLE ProgrammingREQ(
    request_id INT,
    program_language VARCHAR(100),
    due_date DATE,
    project_description TEXT,
    PRIMARY KEY (request_id),
    FOREIGN KEY (request_id) REFERENCES REQUEST(request_id)
);

CREATE TABLE ConsultingREQ(
    request_id INT,
    due_date DATE,
    project_desc TEXT,
    area_of_focus VARCHAR(255),
    company_career VARCHAR(255),
    PRIMARY KEY (request_id),
    FOREIGN KEY (request_id) REFERENCES REQUEST(request_id)
);

CREATE TABLE GameREQ(
    request_id INT,
    due_date DATE,
    game_category VARCHAR(100),
    project_descript TEXT,
    PRIMARY KEY (request_id),
    FOREIGN KEY (request_id) REFERENCES REQUEST(request_id)
);

CREATE TABLE TutorREQ(
    request_id INT,
    school_year VARCHAR(100),
    due_date DATE,
    language_choice VARCHAR(100),
    description TEXT,
    PRIMARY KEY (request_id),
    FOREIGN KEY (request_id) REFERENCES REQUEST(request_id)
);
-- fix for data, new db made for testing
LOAD DATA LOCAL INFILE 'C:/Users/jonti/Xcel/users.csv'
INTO TABLE USER
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/jonti/Xcel/requests.csv'
INTO TABLE REQUEST
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/jonti/Xcel/programming_requests.csv'
INTO TABLE ProgrammingREQ
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/jonti/Xcel/consulting_requests.csv'
INTO TABLE ConsultingREQ
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/jonti/Xcel/game_dev_requests.csv'
INTO TABLE GameREQ
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/jonti/Xcel/tutoring_requests.csv'
INTO TABLE TutorREQ
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

-- check if it worked
SELECT COUNT(*) FROM USER;
SELECT COUNT(*) FROM REQUEST;
SELECT COUNT(*) FROM ProgrammingREQ;
SELECT COUNT(*) FROM ConsultingREQ;
SELECT COUNT(*) FROM GameREQ;
SELECT COUNT(*) FROM TutorREQ;

SELECT * FROM USER LIMIT 10;
SELECT * FROM REQUEST LIMIT 10;
SELECT * FROM ProgrammingREQ LIMIT 10;
SELECT * FROM ConsultingREQ LIMIT 10;
SELECT * FROM GameREQ LIMIT 10;
SELECT * FROM TutorREQ LIMIT 10;

