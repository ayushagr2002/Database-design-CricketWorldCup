DROP DATABASE IF EXISTS dna;
CREATE DATABASE dna;
USE dna;

CREATE TABLE Team (
    Team_ID INT PRIMARY KEY CHECK (Team_ID >=1 AND Team_ID<=10),
    Team_Captain VARCHAR(50) NOT NULL,
    Team_Coach VARCHAR(50) NOT NULL,
    Country_Name VARCHAR(50) NOT NULL,
    Ranking INT UNIQUE NOT NULL
);
CREATE TABLE Batting_Statistics (
    Player_ID INT NOT NULL,
    Highest_Score INT NOT NULL CHECK (Highest_Score>=0 AND Highest_Score<=999),
    Batting_Average DECIMAL(5,2) NOT NULL ,
    Batting_Strike_Rate DECIMAL(5,2) NOT NULL ,
    Number_of_4s INT NOT NULL CHECK (Number_of_4s>=0 AND Number_of_4s<=1000),
    Number_of_6s INT NOT NULL CHECK (Number_of_6s>=0 AND Number_of_6s<=1000), 
    Batting_Style VARCHAR(50) NOT NULL
);
CREATE TABLE Bowling_Statistics (
     Player_ID INT NOT NULL ,
     Bowling_Average DECIMAL(5,2) NOT NULL ,
     Max_Wickets_Taken INT CHECK (Max_Wickets_Taken>=0 AND Max_Wickets_Taken<=10),
     5_Wickets INT NOT NULL CHECK (5_Wickets>=0 AND 5_Wickets<=100),
     Bowling_Style VARCHAR(50) NOT NULL
);
CREATE TABLE Phone (
    Player_ID INT ,
    Phone_Number VARCHAR(50),
    CONSTRAINT Ph_number PRIMARY KEY (Player_ID,Phone_Number)
);
CREATE TABLE Sponsor (
    Match_ID INT ,
    Sponsor VARCHAR(50),
    CONSTRAINT Sponsor_number PRIMARY KEY (Match_ID,Sponsor)
);
CREATE TABLE contract (
    Match_ID int NOT NULL,
    Venue_ID int NOT NULL,
    Player_ID int NOT NULL,
    Team_ID int NOT NULL,
    Match_Fees int 
);
CREATE TABLE Match_Schedule (
    Match_ID    int NOT NULL,
    Venue_ID    int NOT NULL,
    Team1_ID    int NOT NULL,
    Team2_ID    int NOT NULL
);
CREATE TABLE All_Rounder (
    Player_ID   int,
    Total_runs_scored     int NOT NULL,
    Total_Wickets_Taken     int NOT NULL,
    Highest_Runs   int NOT NULL,
    Highest_Wicket   int NOT NULL,
    Batting_Average     int NOT NULL,
    Bowling_Average      int NOT NULL,
    Economy        int NOT NULL,
    CONSTRAINT check_totalrunscored CHECK (Total_runs_scored BETWEEN 0 AND 20000),
    CONSTRAINT check_totalwicketstaken CHECK (Total_Wickets_Taken BETWEEN 0 AND 1000),
    CONSTRAINT check_highestruns CHECK (Highest_Runs BETWEEN 0 AND 500),
    CONSTRAINT check_highestwicket CHECK (Highest_Wicket BETWEEN 0 AND 10)
);

CREATE TABLE Batsman (
    Player_ID   int ,
    Total_runs_scored     int NOT NULL,
    No_of_100s     int NOT NULL,
    No_of_50s      int NOT NULL,
    Highest_Runs   int NOT NULL,
    Average        int NOT NULL,
    CONSTRAINT check_noof100s CHECK (No_of_100s BETWEEN 1 AND 100),
    CONSTRAINT check_noof50s CHECK (No_of_50s BETWEEN 1 AND 100),
    CONSTRAINT check_highest_runs CHECK (Highest_Runs BETWEEN 0 AND 500)
);
CREATE TABLE Bowler (
    Player_ID   int,
    Total_Wickets_Taken     int NOT NULL,
    No_of_3_wickets     int NOT NULL,
    No_of_5_wickets      int NOT NULL,
    Highest_Wicket   int NOT NULL,
    Economy        int NOT NULL,
    CONSTRAINT check_totalwickets_taken CHECK (Total_Wickets_Taken BETWEEN 0 AND 1000),
    CONSTRAINT check_noof3wickets CHECK (No_of_3_wickets BETWEEN 0 AND 1000),
    CONSTRAINT check_noof5wickets CHECK (No_of_5_wickets BETWEEN 0 AND 1000),
    CONSTRAINT check_highest_wicket CHECK (Highest_Wicket BETWEEN 0 AND 10)
);
CREATE TABLE Matches (
    Match_ID    int PRIMARY KEY,
    Team_1_ID   int NOT NULL,
    Team_2_ID   int NOT NULL,
    Match_Date  DATE,
    Match_Time  TIME,
    Venue_ID    int NOT NULL,
    Winner_TeamID   int NOT NULL,
    Won_By  varchar(10) NOT NULL,
    Man_of_the_match_PlayerID   int NOT NULL,
    Match_Attendance    int NOT NULL,
    Percentage_Turnover     decimal(5,2),
    Total_Runs INT NOT NULL,
    CONSTRAINT check_match_id_mat CHECK (Match_ID BETWEEN 101 AND 999),
    CONSTRAINT check_Team1id_mat CHECK (Team_1_ID BETWEEN 1 AND 10),
    CONSTRAINT check_Team2id_mat CHECK (Team_2_ID BETWEEN 1 AND 10),
    CONSTRAINT check_winnerteamid_mat CHECK (Winner_TeamID BETWEEN 1 AND 10),
    CONSTRAINT check_manofmatchplayerid_mat CHECK (Man_of_the_match_PlayerID BETWEEN 10000 AND 99999),
    CONSTRAINT check_matchattendance_mat CHECK (Match_Attendance BETWEEN 0 AND 100000)
);
CREATE TABLE Player (
    Player_ID   int PRIMARY KEY,
    Player_Name     varchar(30) NOT NULL,
    Team_ID     int NOT NULL,
    Role        varchar(10) NOT NULL,
    DOB         date NOT NULL,
    Player_Age  int NOT NULL,
    CONSTRAINT check_playerid_ply CHECK (Player_ID BETWEEN 10000 AND 99999),
    CONSTRAINT  check_playerage_ply CHECK (Player_Age BETWEEN 18 AND 45)
);
CREATE TABLE Venue (
    Venue_ID    int PRIMARY KEY,
    Venue_Name  varchar(30) NOT NULL,
    Stadium_Name    varchar(30) NOT NULL,
    CONSTRAINT check_venue_id_ven CHECK (Venue_ID BETWEEN 100 AND 999)
);

CREATE TABLE Points_Table (
    Team_ID int PRIMARY KEY,
    Team_Name   varchar(30) NOT NULL,
    Points_Scored   int NOT NULL,
    Run_rate    decimal(4,2) NOT NULL,
    Ranking     int
);

ALTER TABLE Batting_Statistics ADD CONSTRAINT FK_playeridbatstat FOREIGN KEY(Player_ID) REFERENCES Player(Player_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Bowling_Statistics ADD CONSTRAINT FK_playeridbowlstat FOREIGN KEY(Player_ID) REFERENCES Player(Player_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Player ADD CONSTRAINT FK_Teamid_player FOREIGN KEY(Team_ID) REFERENCES Team(Team_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Matches ADD CONSTRAINT FK_Venueid_matches FOREIGN KEY(Venue_ID) REFERENCES Venue(Venue_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Phone ADD CONSTRAINT FK_Playerid_phone FOREIGN KEY(Player_ID) REFERENCES Player(Player_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Sponsor ADD CONSTRAINT FK_Matchid_Sponsor FOREIGN KEY(Match_ID) REFERENCES Matches(Match_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE contract ADD CONSTRAINT FK_Matchid_contract FOREIGN KEY(Match_ID) REFERENCES Matches(Match_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE contract ADD CONSTRAINT FK_Venueid_contract FOREIGN KEY(Venue_ID) REFERENCES Venue(Venue_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE contract ADD CONSTRAINT FK_Playerid_contract FOREIGN KEY(Player_ID) REFERENCES Player(Player_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE contract ADD CONSTRAINT FK_Teamid_contract FOREIGN KEY(Team_ID) REFERENCES Team(Team_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Match_Schedule ADD CONSTRAINT FK_Matchid_schedule FOREIGN KEY(Match_ID) REFERENCES Matches(Match_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Match_Schedule ADD CONSTRAINT FK_Venueid_schedule FOREIGN KEY(Venue_ID) REFERENCES Venue(Venue_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Match_Schedule ADD CONSTRAINT FK_Team1id_schedule FOREIGN KEY(Team1_ID) REFERENCES Team(Team_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Match_Schedule ADD CONSTRAINT FK_Team2id_schedule FOREIGN KEY(Team2_ID) REFERENCES Matches(Match_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Bowler ADD CONSTRAINT FK_playerid_bowler FOREIGN KEY(Player_ID) REFERENCES Player(Player_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Batsman ADD CONSTRAINT FK_playerid_batsman FOREIGN KEY(Player_ID) REFERENCES Player(Player_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE All_Rounder ADD CONSTRAINT FK_playerid_all_rounder FOREIGN KEY(Player_ID) REFERENCES Player(Player_ID) ON DELETE CASCADE ON UPDATE CASCADE;


INSERT INTO Team
VALUES ('1','Rohit Sharma','Ravi Shastri','India','1');

INSERT INTO Team
VALUES ('2','Steve Smith','Justin Langer','Australia','4');

INSERT INTO Team
VALUES ('3','Babar Azam','Matthew Hayden','Pakistan','3');

INSERT INTO Team
VALUES (4,'Kane Williamson','Gary Stead','New Zealand',2);

INSERT INTO Team
VALUES (5,'Jason Holder','Phil simmons','West indies',5);





INSERT INTO Venue 
VALUES ('101','Mumbai','Wankhede');

INSERT INTO Venue
VALUES ('102','Kolkata','Eden Gardens');

INSERT INTO Venue
VALUES('103','Chennai','M.A. Chidambaram Stadium');

INSERT INTO Venue
VALUES('104','Chennai','Jawaharlal Nehru Stadium');
 
INSERT INTO Venue
VALUES('105' , 'Delhi' , 'Arun Jaitley Stadium');





INSERT INTO Matches
VALUES('101','1','2','2021-10-23','15:30:00','101','1','20 Runs','10000','15000','95.00', '289');

INSERT INTO Matches
VALUES('102','1','3','2021-10-25','15:30:00','102','1','30 Runs','10001','20000','93.00','315');

INSERT INTO Matches
VALUES('103','3','5','2021-10-27','15:30:00','103','5','45 Runs','50002','15000','96.00','374');

INSERT INTO Matches
VALUES('104','2','3','2021-10-29','15:30:00','104','3','3 Wickets','30001','16000','90.00','256');

INSERT INTO Matches
VALUES('105','4','5','2021-10-31','15:30:00','105','4','50 Runs','40001','19000','85.00','412');




INSERT INTO Player 
VALUES ('10001','Rohit Sharma','1','Bat','1987-03-30','34');

INSERT INTO Player 
VALUES ('10003','Bhuvneshwar Kumar','1','Bowl','1990-02-05','31');

INSERT INTO Player 
VALUES ('10007','Hardik Pandya','1','AllRounder','1993-10-11','28');

INSERT INTO Player 
VALUES ('20001','Steve Smith','2','Bat','1989-06-02','32');

INSERT INTO Player 
VALUES ('20005','Mitchell Starc','2','Bowl','1990-01-30','31');

INSERT INTO Player 
VALUES ('20009','Glenn Maxwell','2','AllRounder','1988-10-14','33');

INSERT INTO Player 
VALUES ('30001','Babar Azam','3','Bat','1994-10-15','27');

INSERT INTO Player 
VALUES ('30004','Mohammad Amir','3','Bowl','1992-04-13','29');

INSERT INTO Player 
VALUES ('30008','Shoaib Malik','3','AllRounder','1982-02-01','39');

INSERT INTO Player 
VALUES ('40001','Kane Williamson','4','Bat','1991-02-12','30');

INSERT INTO Player 
VALUES ('40002','Trent Boult','4','Bowl','1989-07-22','32');

INSERT INTO Player 
VALUES ('40007','Mitchell Santner','4','AllRounder','1992-02-05','29');

INSERT INTO Player 
VALUES ('50001','Jason Holder','5','AllRounder','1991-11-05','29');

INSERT INTO Player 
VALUES ('50003','Kemar Roach','5','Bowl','1988-06-30','33');

INSERT INTO Player 
VALUES ('50009','Shimron Hetmyer','5','Bat','1996-12-26','24');





INSERT INTO Batting_Statistics
VALUES ('10001','128','038.58','140.27','12','3','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('10003','29','003.23','078.46','5','0','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('10007','63','024.79','189.49','15','2','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('20001','94','041.89','134.69','6','2','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('20005','14','006.90','034.56','2','0','Left-Handed');

INSERT INTO Batting_Statistics
VALUES ('20009','56','023.51','209.12','13','7','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('30001','82','030.40','129.41','19','11','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('30004','11','005.21','067.15','0','1','Left-Handed');

INSERT INTO Batting_Statistics
VALUES ('30008','34','023.58','126.14','16','7','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('40001','103','039.42','138.01','19','2','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('40002','25','008.45','39.16','3','0','Left-Handed');

INSERT INTO Batting_Statistics
VALUES ('40007','42','028.68','163.89','16','9','Left-Handed');

INSERT INTO Batting_Statistics
VALUES ('50001','45','025.23','195.23','11','13','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('50003','6','004.12','012.59','0','0','Right-Handed');

INSERT INTO Batting_Statistics
VALUES ('50009','78','037.21','156.34','8','1','Left-Handed');




INSERT INTO Bowling_Statistics
VALUES ('10001','068.58','1','0','Right-Arm-Medium');

INSERT INTO Bowling_Statistics
VALUES ('10003','013.12','7','2','Right-Arm-Fast');

INSERT INTO Bowling_Statistics
VALUES ('10007','027.33','6','1','Right-Arm-Medium-Fast');

INSERT INTO Bowling_Statistics
VALUES ('20001','045.21','6','1','Right-Arm-Off-Break');

INSERT INTO Bowling_Statistics
VALUES ('20005','008.20','8','1','Right-Arm-Fast');

INSERT INTO Bowling_Statistics
VALUES ('20009','054.53','3','0','Right-Arm-Slow-Orthodox');

INSERT INTO Bowling_Statistics
VALUES ('30001','093.42','1','0','Left-Arm-Medium');

INSERT INTO Bowling_Statistics
VALUES ('30004','007.41','7','1','Left-Arm-Fast');

INSERT INTO Bowling_Statistics
VALUES ('30008','036.48','6','1','Right-Arm-Slow-Orthodox');

INSERT INTO Bowling_Statistics
VALUES ('40001','099.42','1','0','Right-Arm-Off-Break');

INSERT INTO Bowling_Statistics
VALUES ('40002','007.23','9','1','Left-Arm-Fast');

INSERT INTO Bowling_Statistics
VALUES ('40007','023.11','8','1','Right-Arm-Slow-Orthodox');

INSERT INTO Bowling_Statistics
VALUES ('50001','031.32','6','1','Right-Arm-Medium-Fast');

INSERT INTO Bowling_Statistics
VALUES ('50003','009.22','6','1','Right-Arm-Fast');

INSERT INTO Bowling_Statistics
VALUES ('50009','044.41','4','0','Right-Arm-Leg-Break');





INSERT INTO Bowler
VALUES ('10003','214','23','15','9','7');

INSERT INTO Bowler 
VALUES ('20005','303','33','26','8','6');

INSERT INTO Bowler
VALUES ('30004','211','21','14','8','7');

INSERT INTO Bowler
VALUES ('40002','349','39','29','9','6');

INSERT INTO Bowler 
VALUES ('50003','114','14','6','7','8');




INSERT INTO Batsman 
VALUES ('10001','8972','7','23','132','46');

INSERT INTO Batsman 
VALUES ('20001','4523','1','13','102','38');

INSERT INTO Batsman 
VALUES ('30001','7422','4','16','111','44');

INSERT INTO Batsman 
VALUES ('40001','7237','5','21','116','41');

INSERT INTO Batsman 
VALUES ('50009','2164','1','6','103','36');




INSERT INTO All_Rounder
VALUES ('10007','2637','164','122','8','26.69','42.00','8');

INSERT INTO All_Rounder 
VALUES ('20009','4490','112','134','6','32.54','32.33','7');

INSERT INTO All_Rounder
VALUES ('30008','1369','254','110','7','21.44','23.46','7');

INSERT INTO All_Rounder
VALUES ('40007','1157','214','104','8','23.45','21.10','6');

INSERT INTO All_Rounder 
VALUES ('50001','3819','200','116','8','36.32','31.48','8');




INSERT INTO Phone
VALUES('10001','9861334567');
INSERT INTO Phone
VALUES('10001','8790675432');
INSERT INTO Phone
VALUES('10003','7894533221');
INSERT INTO Phone
VALUES('10007','9090768859');
INSERT INTO Phone
VALUES('30001','8985213052');
INSERT INTO Phone
VALUES('30001','7548969681');
INSERT INTO Phone
VALUES('30004','8584632987');
INSERT INTO Phone
VALUES('40007','9871445698');
INSERT INTO Phone
VALUES('40007','8988821414');
INSERT INTO Phone
VALUES('50003','8497225645');




INSERT INTO Sponsor
VALUES('101','Vivo');
INSERT INTO Sponsor
VALUES('101','Upstox');  
INSERT INTO Sponsor
VALUES('101','Bharat Pe'); 
INSERT INTO Sponsor
VALUES('102','Adidas'); 
INSERT INTO Sponsor
VALUES('102','Upstox');
INSERT INTO Sponsor
VALUES('102','Coca-Cola');
INSERT INTO Sponsor
VALUES('103','Hyundai');
INSERT INTO Sponsor
VALUES('103','Visa');
INSERT INTO Sponsor
VALUES('104','Adidas');
INSERT INTO Sponsor
VALUES('105','Hyundai');




INSERT INTO contract
VALUES('101','101','10001','1','500000');
INSERT INTO contract
VALUES('101','101','10003','1','400000');
INSERT INTO contract
VALUES('101','101','10007','1','425000');
INSERT INTO contract
VALUES('101','101','20001','2','450000');
INSERT INTO contract
VALUES('101','101','20005','2','475000');
INSERT INTO contract
VALUES('101','101','20009','2','480000');
INSERT INTO contract
VALUES('102','102','10001','1','550000');
INSERT INTO contract
VALUES('102','102','10003','1','450000');
INSERT INTO contract
VALUES('102','102','10007','1','370000');
INSERT INTO contract
VALUES('102','102','30001','3','300000');
INSERT INTO contract
VALUES('102','102','30004','3','350000');
INSERT INTO contract
VALUES('102','102','30008','3','375000'); 




INSERT INTO Points_Table 
VALUES('1','India','3','02.33','1');

INSERT INTO Points_Table
VALUES('2','Australia','2','01.22','2');

INSERT INTO Points_Table
VALUES('4','New Zealand','1','00.69','3');

INSERT INTO Points_Table
VALUES('5','West indies','1','-00.32','4');

INSERT INTO Points_Table
VALUES('3','Pakistan','0','-01.37','5');
