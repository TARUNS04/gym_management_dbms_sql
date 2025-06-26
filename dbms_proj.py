import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='gym_management_project')

cursor = mydb.cursor()
#USER TABLE
cursor.execute(""" insert into User(User_ID,First_Name,Last_Name,Email_Address,Phone_Number,Gender ,Date_of_Birth,Height,Weight,Medical_History,Current_Medications)
values(1,'tarun','singh','singhtarun9060@gmail.com','8595569678','male','2024-06-11',5.7,66,'none','none'),
(2,'mexi','duhan','duhan@gmail.com','8595567778','male','2004-10-06',5,80,'none','none'),
(3,'arun','singh','arunsingh@gmail.com','8592569678','male','2004-06-11',5.8,66,'none','none'),
(4,'vriti','goyal','singhtarun90@gmail.com','7355569678','female','2005-04-30',5.2,50,'none','none'),
(5,'madhav','garg','madhavfantastic@gmail.com','8595777888','male','2004-03-06',5.9,70,'none','none')
""")
#TRAINER TABLE
cursor.execute("""insert into Trainer (Trainer_ID,First_Name,Last_Name,Phone_Number,Certification,Experience)
values(1,'guddu','don',9865741235,'iso',5),
(2,'raju','bhandari',3335741235,'iso',3),
(3,'rajat','mittal',3238644235,'iso',6)
""")
#EXERCISE TABLE
cursor.execute(""" insert into Exercise(Exercise_ID,Exercise_Name,Description,Duration,Calories_Burned)
values(1,'chestex','for chest',10,100),
(2,'shoulder','for shoulder',8,80),
(3,'legs','for legs',15,100)
""")
#NUTRITION TABLE
cursor.execute(""" insert into Nutrition (Nutrition_ID,Description,Glasses_of_Water,Calories_Intake,Protein_Intake,Carbohydrate_Intake,Fat_Intake)
values(1,'for bulking,eat pulses, and rice',10,500,50,200,80),
(2,'for slim fit',15,300,30,150,50),
(3,'for body posture',10,400,80,500,50)
""")
#GOAL TABLE
cursor.execute("""insert into Goal(Goal_ID,Goal_Description,Goal_Start_Date,Goal_End_Date,Current_Progress,User_ID)
values(1,'will do legs','2024-10-24','2025-01-01',0,1)
""")
#USER_TRAINER TABLE
cursor.execute("""insert into User_Trainer(User_ID,Trainer_ID)
values(1,1),
(2,3),
(3,3),
(4,2),
(5,1)""")
#EXERCISE_USER TABLE
cursor.execute("""insert into Exercise_User (User_ID,Exercise_ID)
values(1,1),
(2,3),
(3,3),
(4,2),
(5,1)
""")
#NUTRITION_USER TABLE
cursor.execute("""insert into Nutrition_User (User_ID,Nutrition_ID)
values(1,1),
(2,3),
(3,3),
(4,2),
(5,1)
""")
#TRAINER_EXERCISE_ADVICES
cursor.execute("""insert into Trainer_Exercise_Advices (Trainer_ID,Exercise_ID)
values(1,1),
(2,2),
(3,3)
""")
#TRAINER_NUTRITION_ADVICES
cursor.execute("""insert into Trainer_Nutrition_Advices (Trainer_ID,Nutrition_ID)
values(1,1),
(2,2),
(3,3)
""")
mydb.commit()
