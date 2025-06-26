import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='gym_management_project')

cursor = mydb.cursor()
cursor.execute("""CREATE TABLE User (
    User_ID INT PRIMARY KEY,
    First_Name VARCHAR(20),
    Last_Name VARCHAR(20),
    Email_Address VARCHAR(30),
    Phone_Number VARCHAR(10),
    Gender VARCHAR(11),
    Date_of_Birth DATE,
    Height FLOAT,
    Weight FLOAT,
    BMI FLOAT GENERATED ALWAYS AS (weight / (height * height)) STORED,
    Medical_History TEXT,
    Current_Medications TEXT
)""")

cursor.execute("""CREATE TABLE Trainer (
    Trainer_ID INT PRIMARY KEY,
    First_Name VARCHAR(20),
    Last_Name VARCHAR(20),
    Phone_Number VARCHAR(10),
    Certification VARCHAR(100),
    Experience INT
)""")

cursor.execute("""CREATE TABLE Exercise (
    Exercise_ID INT PRIMARY KEY,
    Exercise_Name VARCHAR(100),
    Description TEXT,
    Duration INT,
    Calories_Burned FLOAT
)""")

cursor.execute("""CREATE TABLE Nutrition (
    Nutrition_ID INT PRIMARY KEY,
    Description TEXT,
    Glasses_of_Water INT,
    Calories_Intake FLOAT,
    Protein_Intake FLOAT,
    Carbohydrate_Intake FLOAT,
    Fat_Intake FLOAT
)""")

cursor.execute("""CREATE TABLE Goal (
    Goal_ID INT PRIMARY KEY,
    Goal_Description TEXT,
    Goal_Start_Date DATE,
    Goal_End_Date DATE,
    Current_Progress FLOAT,
    User_ID INT,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
)""")

cursor.execute("""CREATE TABLE User_Trainer (
    User_ID INT,
    Trainer_ID INT,
    PRIMARY KEY (User_ID, Trainer_ID),
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Trainer_ID) REFERENCES Trainer(Trainer_ID)
)""")

cursor.execute("""CREATE TABLE Exercise_User (
    Exercise_ID INT,
    User_ID INT,
    PRIMARY KEY (Exercise_ID, User_ID),
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
)""")

cursor.execute("""CREATE TABLE Nutrition_User (
    Nutrition_ID INT,
    User_ID INT,
    PRIMARY KEY (Nutrition_ID, User_ID),
    FOREIGN KEY (Nutrition_ID) REFERENCES Nutrition(Nutrition_ID),
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
)""")

cursor.execute("""CREATE TABLE Trainer_Exercise_Advices (
    Trainer_ID INT,
    Exercise_ID INT,
    PRIMARY KEY (Trainer_ID, Exercise_ID),
    FOREIGN KEY (Trainer_ID) REFERENCES Trainer(Trainer_ID),
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID)
)""")

cursor.execute("""CREATE TABLE Trainer_Nutrition_Advices (
    Trainer_ID INT,
    Nutrition_ID INT,
    PRIMARY KEY (Trainer_ID, Nutrition_ID),
    FOREIGN KEY (Trainer_ID) REFERENCES Trainer(Trainer_ID),
    FOREIGN KEY (Nutrition_ID) REFERENCES Nutrition(Nutrition_ID)
)""")
mydb.commit()
