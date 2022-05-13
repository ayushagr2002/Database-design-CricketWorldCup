from re import match
from typing import Match
import pymysql
from pymysql.connections import Connection
import pymysql.cursors
import subprocess as sp
from os import environ,path
from tabulate import PRESERVE_WHITESPACE, tabulate
from datetime import date
import math 


def get_player_age(birth_date):
    DOB = birth_date.split("-")
    year=int(DOB[0])
    month=int(DOB[1])
    day=int(DOB[2])
    cur_day=date.today()
    age = cur_day.year - year - ((cur_day.month,cur_day.day) < (month,day))
    return age

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def insertmatches():
    print("Insert Match details for entry :")
    match_id = int(input("Enter Match ID: "))
    Team1_id = int(input("Enter Team 1 ID: "))
    Team2_id = int(input("Enter Team 2 ID: "))
    Match_date = input("Enter Match Date(YYYY-MM-DD): ")
    Match_Time = input("Enter Match Time(HH:MM:SS): ")
    Venue_ID = int(input("Enter Venue ID: "))
    WinnerteamID = int(input("Enter Winner Team ID: "))
    Won_By = input("Enter win margin: ")
    momplayerid = int(input("Enter man of the match player id: "))
    match_attend = int(input("Enter Match Attendance: "))
    Total_runs= int(input("Total runs scored in the match : "))
    percent_turnover = match_attend/200.00
    percent_turnover = truncate(percent_turnover,2)

    query = """INSERT INTO Matches VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    try:
        cur.execute(query,(match_id,Team1_id,Team2_id,Match_date,Match_Time,Venue_ID,WinnerteamID,Won_By,momplayerid,match_attend,percent_turnover,Total_runs))
        conn.commit()
    except Exception as e:
        print("Could not insert into Matches.Please check input values")
        t = input("Press Any key to continue: ")
        return
    resultquery = """SELECT * FROM Matches WHERE `Match_ID` = %s; """
    cur.execute(resultquery,(match_id))
    output=cur.fetchall()
    print("The following entry has been added into Matches Table:")
    print(tabulate(output,headers="keys",tablefmt='psql'))
    t = input("Press Any key to continue: ")
    return

def insertplayer():
    print("Insert Player details for entry :")
    Player_ID=int(input("Enter Player ID : "))
    Player_Name=input("Enter Player name : ")
    Team_ID=int(input("Enter Team_ID: "))
    Role=input("Enter Player Role : ")
    DOB =input("Enter date of birth : ")
    AGE= get_player_age(DOB)
    query1 = """INSERT INTO Player VALUES(%s,%s,%s,%s,%s,%s);"""
    try:
        cur.execute(query1,(Player_ID,Player_Name,Team_ID,Role,DOB,AGE))
        conn.commit()
    except Exception as e:
        print("Could not insert data player table")
        t = input("Press Any key to continue: ")
        return
    resultquery="""SELECT * FROM Player WHERE `Player_ID`=%s;"""
    cur.execute(resultquery,(Player_ID))
    output=cur.fetchall()
    print("The following entry has been added to the Player Table : ")
    print(tabulate(output,headers="keys",tablefmt='psql'))
    t = input("Press Any key to continue: ")
    return
    

def insertvenue():
    print("Insert Venue Details for entry :")
    venue_id = int(input("Enter Venue ID: "))
    venue_name = input("Enter Venue name: ")
    stadium_name = input("Enter Stadium name: ")
    
    query = """INSERT INTO Venue VALUES (%s,%s,%s);"""
    try:
        cur.execute(query, (venue_id, venue_name, stadium_name))
        conn.commit()
    except Exception as e:
        print("Could not insert data venue table")
        t = input("Press Any key to continue: ")
        return
    query2 = """SELECT * FROM Venue WHERE `Venue_ID`=%s;"""
    cur.execute(query2,(venue_id))
    output=cur.fetchall()
    print("The following entry has been added to the Venue Table: ")
    print(tabulate(output,headers="keys", tablefmt='psql'))  
    t = input("Press Any key to continue: ")
    return 

def insertbatstat():
    print("Insert Batting Statistics :")
    player_id = int(input("Enter Player ID: "))
    highestscore = int(input("Enter Highest Runs scored by player: "))
    batting_avg = float(input("Enter Batting avg of player: "))
    strikerate = float(input("Enter strike rate of player: "))
    noof4s = int(input("Enter number of 4s scored by the player: "))
    noof6s = int(input("Enter number of 6s scored by the player: "))
    batstyle = input("Enter batting style of the player: ")
    query = """INSERT INTO Batting_Statistics VALUES(%s,%s,%s,%s,%s,%s,%s);"""
    try:
        cur.execute(query,(player_id,highestscore,batting_avg,strikerate,noof4s,noof6s,batstyle))
        conn.commit()
    except Exception as e:
        print("Could not enter values into Batting_Statistics. Please check the input")
        t = input("Press Any key to continue: ")
        return
    query2 = """SELECT * FROM Batting_Statistics WHERE `Player_ID` = %s;"""
    cur.execute(query2,(player_id))
    output=cur.fetchall()
    print("The following entry has been added to the Batting_Statistics Table: ")
    print(tabulate(output,headers="keys", tablefmt='psql'))
    t = input("Press Any key to continue: ")
    return

def insertbowlstat():
    print("Insert Bowling Statistics: ")
    Player_ID=int(input("Enter Player ID : "))
    Bowling_avg=float(input("Enter bowling average: "))
    max_wickets_taken = int(input("Enter number of wickets taken: "))
    num_5_wickets= int(input("Enter number of 5 wicket hauls: "))
    bowling_style= input("Enter Bowling Style: ")
    query1 = """INSERT INTO Bowling_Statistics VALUES(%s,%s,%s,%s,%s);"""   
    try:
        cur.execute(query1,(Player_ID,Bowling_avg,max_wickets_taken,num_5_wickets,bowling_style))
        conn.commit()
    except Exception as e:
        print("Could not insert entry into Bowling Statistics")
        t = input("Press Any key to continue: ")
        return 
    resultquery ="""SELECT * FROM Bowling_Statistics WHERE `Player_ID`=%s;"""
    cur.execute(resultquery,(Player_ID))
    output=cur.fetchall()
    print("The following entry has been added to the Bowling Statistics Table: ")
    print(tabulate(output,headers="keys", tablefmt='psql'))
    t = input("Press Any key to continue: ")
    return

def dispatchinsert():
    sp.call('clear',shell=True)
    print("Select the table u want to insert entry into")
    print("1. Matches")
    print("2. Player")
    print("3. Venue")
    print("4. Batting_Statistics")
    print("5. Bowling_Statistics")
    print()
    tablename = input()
    if(tablename == '1'):
        insertmatches()
    elif(tablename == '2'):
        insertplayer()
    elif(tablename == '3'):
        insertvenue()
    elif(tablename == '4'):
        insertbatstat()
    elif(tablename == '5'):
        insertbowlstat()
    else:
        print("Sorry u have selected an invalid option")
        t = input("Press Any key to continue")
        return
def updatematches():
    print("Update Match Details : ")
    match_id = int(input("Enter Match_ID of match to be updated: "))
    query1 = """SELECT * FROM Matches WHERE `Match_ID`=%s;"""
    cur.execute(query1, (match_id))
    output = cur.fetchall()
    if len(output)==0 :
        print("This Match_ID does not exist")
        t = input("Press Any key to continue : ")
        return
    which = input("Enter the field to be updated: ")  
    if (which == "Team_1_ID"):
        to = int(input("Enter new Team 1 ID"))
        query = """UPDATE Matches SET Team_1_ID = %s WHERE `Match_ID` = %s;"""
    elif (which == "Team_2_ID"):
        to = int(input("Enter new Team 2 ID: "))
        query = """UPDATE Matches SET Team_2_ID = %s WHERE `Match_ID` = %s;"""
    elif(which == "Match_Date"):
        to = input("Enter new Match Date(YYYY-MM-DD): ")
        query = """UPDATE Matches SET Match_Date = %s WHERE `Match_ID` = %s;"""
    elif(which == "Match_Time"):
        to = input("Enter new Match Time(HH:MM:SS): ")
        query = """UPDATE Matches SET Match_Time = %s WHERE `Match_ID` = %s;"""
    elif(which == "Venue_ID"):
        to = int(input("Enter new Venue ID: "))
        query = """UPDATE Matches SET Venue_ID = %s WHERE `Match_ID` = %s;"""
    elif(which == "Winner_TeamID"):
        to = int(input("Enter new winner team ID: "))
        query = """UPDATE Matches SET Winner_TeamID = %s WHERE `Match_ID` = %s;"""
    elif(which == "Won_By"):
        to = input("Enter new Won by: ")
        query = """UPDATE Matches SET Won_By = %s WHERE `Match_ID` = %s;"""
    elif(which == "Man_of_the_match_PlayerID"):
        to = int(input("Enter new Man of the match Player ID: "))
        query = """UPDATE Matches SET Man_of_the_match_PlayerID = %s WHERE `Match_ID` = %s;"""
    elif(which == "Match_Attendance"):
        to = int(input("Enter new Match Attendance: "))
        query = """UPDATE Matches SET Match_Attendance = %s WHERE `Match_ID` = %s;"""
    elif(which == "Total_Runs"):
        to = int(input("Enter new Total Runs : "))
        query = """UPDATE Matches SET Total_Runs = %s WHERE `Match_ID` = %s;"""
    else:
        print("Sorry no such field found, Please try again")
        t = input("Press Any key to continue : ")
        return
    if(which == "Match_Attendance"):
        percent_turnover = to/200.00
        percent_turnover = truncate(percent_turnover,2)
    if(which == "Match_Attendance"):
        query2 = "UPDATE Matches SET Percentage_Turnover = %s WHERE `Match_ID` = %s;"
    try:
        cur.execute(query,(to,match_id))
        if(which == "Match_Attendance"):
            cur.execute(query2,(percent_turnover,match_id))
        conn.commit()
    except Exception as e:
        print(e)
        print("Could not execute the update query")
        t = input("Press Any Key to continue : ")
        return
    result_query = """SELECT * FROM Matches WHERE `Match_ID` = %s;"""
    cur.execute(result_query,(match_id))
    output = cur.fetchall()
    print("The following entry has been updated into the Matches Table")
    print(tabulate(output,headers="keys",tablefmt='psql'))
    t = input("Press any key to continue: ")
    return

def updateplayers():
    print("Update Player Details: ")
    player_id = int(input("Enter Player ID of player to be updated: "))
    query1 = """SELECT * FROM Player WHERE `Player_ID`=%s;"""
    cur.execute(query1, (player_id))
    output = cur.fetchall()
    if len(output)==0 :
        print("This Match_ID does not exist")
        t = input("Press Any key to continue")
        return
    which = input("Enter the field to be updated: ")
    if(which == "Player_Name"):
        to = input("Enter the new Player Name : ")
        query = """UPDATE Player SET Player_Name = %s WHERE `Player_ID` = %s;"""
    elif(which == "TeamID"):
        to = int(input("Enter new Team ID: "))
        query = """UPDATE Player SET Team_ID = %s WHERE `Player_ID` = %s;"""
    elif(which == "Role"):
        to = input("Enter new Role: ")
        query = """UPDATE Player SET Role = %s WHERE `Player_ID` = %s;"""
    elif(which == "DOB"):
        to = input("Enter new DOB of player(YYYY-MM-DD): ")
        query = """UPDATE Player SET DOB = %s WHERE `Player_ID` = %s;"""
    else:
        print("Sorry no such field found, Please try again (aka funwa)")
        t = input("Press Any key to continue")
        return
    try:
        cur.execute(query,(to,player_id)) 
        if(which == "DOB"):
            player_age = get_player_age(to)
            query2 = "UPDATE Player SET Player_Age =%s WHERE `Player_ID` = %s;"
            cur.execute(query2,(player_age,player_id))
        conn.commit()
    except Exception as e:
        print("Could not execute the update query")
        t = input("Press any key to continue")
        return
    result_query = "SELECT * FROM Player WHERE `Player_ID` = %s;"
    cur.execute(result_query,(player_id))
    output = cur.fetchall()
    print("The following entry has been updated into the Player Table")
    print(tabulate(output,headers = "keys",tablefmt='psql'))
    t = input("Press any key to continue: ")
    return

def updatevenue():
    print("Update Venue Details :")
    venue_id = int(input("Enter Venue ID to be updated: "))
    querychk="""SELECT * FROM Venue WHERE `Venue_ID`=%s;"""
    cur.execute(querychk,(venue_id))
    output = cur.fetchall()
    if len(output)==0 :
        print("This Venue_ID does not exist")
        t = input("Press Any key to continue : ")
        return
    which = input("Enter the field to be updated: ")
    if which == "Venue_Name" :
        to = input("Enter new venue name: ")
        query = """UPDATE Venue SET Venue_Name = %s WHERE `Venue_ID` = %s;"""
    elif which == "Stadium_Name" :
        to = input("Enter new Stadium name: ")
        query = """UPDATE Venue SET Stadium_Name = %s WHERE `Venue_ID` = %s;"""
    else:
        print("Sorry no such field found, Please try again")
        t = input("Press Any key to continue : ")
        return
    try:
        cur.execute(query,(to,venue_id))
        conn.commit()
    except Exception as e:
        print(e)
        print("Could not update data venue table")
        t = input("Press Any key to continue : ")
        return
    query2 = """SELECT * FROM Venue WHERE `Venue_ID`=%s;"""
    cur.execute(query2,(venue_id))
    output=cur.fetchall()
    print("The following entry has been updated in the Venue Table: ")
    print(tabulate(output,headers="keys", tablefmt='psql')) 
    t = input("Press Any key to continue : ") 
    return


def updatebatstat():
    print("Update Batting Statistics :")
    player_id = int(input("Enter Player ID: "))
    querychk="""SELECT * FROM Player WHERE Player_ID=%s"""
    cur.execute(querychk,(player_id))
    output = cur.fetchall()
    if len(output)==0 :
        print("This Player_ID does not exist")
        t = input("Press Any key to continue")
        return
    which = input("Enter the field to be updated: ")
    if which == "Highest_Score" :
        query = """UPDATE Batting_Statistics SET Highest_Score = %s WHERE `Player_ID` = %s;"""
        to = int(input("Enter the new Highest score: "))
    elif which == "Batting_Average" :
        query = """UPDATE Batting_Statistics SET Batting_Average = %s WHERE `Player_ID` = %s;"""
        to = float(input("Enter the new Batting Average: "))
    elif which == "Batting_Strike_Rate" :
        query = """UPDATE Batting_Statistics SET Batting_Strike_Rate = %s WHERE `Player_ID` = %s;"""
        to = float(input("Enter the new Batting Strike Rate: "))
    elif which == "Number_of_4s" :
        query = """UPDATE Batting_Statistics SET Number_of_4s = %s WHERE `Player_ID` = %s;"""
        to = int(input("Enter the new number of 4s: "))
    elif which == "Number_of_6s" :
        query = """UPDATE Batting_Statistics SET Number_of_6s = %s WHERE `Player_ID` = %s;"""
        to = int(input("Enter the new number of 6s: "))
    elif which == "Batting_Style" :
        query = """UPDATE Batting_Statistics SET Batting_Style = %s WHERE `Player_ID` = %s;"""
        to = input("Enter the new Batting Style: ")
    else:
        print("Sorry no such field found, Please try again (aka funwa)")
        t = input("Press Any key to continue : ")
        return
    try:
        cur.execute(query,(to,player_id))
        conn.commit()
    except Exception as e:
        print(e)
        print("Could not enter values into Batting_Statistics. Please check the input")
        t = input("Press Any key to continue: ")
        return
    query2 = """SELECT * FROM Batting_Statistics WHERE `Player_ID` = %s;"""
    cur.execute(query2,(player_id))
    output=cur.fetchall()
    print("The following entry has been updated in the Batting_Statistics Table: ")
    print(tabulate(output,headers="keys", tablefmt='psql'))
    t = input("Press Any key to continue : ")
    return

def updatebowlstat():
    print("Update Bowling Statistics :")
    player_id = int(input("Enter Player ID: "))
    querychk="""SELECT * FROM Player WHERE Player_ID=%s;"""
    cur.execute(querychk,(player_id))
    output = cur.fetchall()
    if len(output)==0 :
        print("This Player_ID does not exist")
        t = input("Press Any key to continue : ")
        return
    which = input("Enter the field to be updated: ")
    if which == "Bowling_Average" :
        to = float(input("Enter the new Bowling Average: "))
        query = """UPDATE Bowling_Statistics SET Bowling_Average = %s WHERE `Player_ID` = %s;"""
    elif which == "Max_Wickets_Taken" :
        to = int(input("Enter the new Max Wickets taken: "))
        query = """UPDATE Bowling_Statistics SET Max_Wickets_Taken = %s WHERE `Player_ID` = %s;"""
    elif which == "5_Wickets" :
        to = int(input("Enter the new 5 Wickets Taken: "))
        query = """UPDATE Bowling_Statistics SET 5_Wickets = %s WHERE `Player_ID` = %s;"""
    elif which == "Bowling_Style" :
        to = input("Enter the new Bowling Style: ")
        query = """UPDATE Bowling_Statistics SET Bowling_Style = %s WHERE `Player_ID` = %s;"""
    else:
        print("Sorry no such field found, Please try again")
        t = input("Press Any key to continue")
        return
    try:
        cur.execute(query,(to,player_id))
        conn.commit()
    except Exception as e:
        print("Could not enter values into Bowling_Statistics. Please check the input")
        t = input("Press Any key to continue: ")
        return
    query2 = """SELECT * FROM Bowling_Statistics WHERE `Player_ID` = %s;"""
    cur.execute(query2,(player_id))
    output=cur.fetchall()
    print("The following entry has been updated in the Bowling_Statistics Table: ")
    print(tabulate(output,headers="keys", tablefmt='psql'))
    t = input("Press Any key to continue: ")
    return

def dispatchupdate():
    sp.call('clear',shell=True)
    print("Select the table u want to update entry into")
    print("1. Matches")
    print("2. Player")
    print("3. Venue")
    print("4. Batting_Statistics")
    print("5. Bowling_Statistics")
    tablename = input()
    if(tablename == '1'):
        updatematches()
    elif(tablename == '2'):
        updateplayers()
    elif(tablename == '3'):
        updatevenue()
    elif(tablename == '4'):
        updatebatstat()
    elif(tablename == '5'):
        updatebowlstat()
    else:
        print("Sorry, you have selected an invalid option")
        t = input("Press Any key to continue")
        return

def deletematches():
    Match_ID = int(
    input("Enter the match_ID of the entry you want to delete :"))
    query1 = """SELECT * FROM Matches WHERE `Match_ID`=%s;"""
    cur.execute(query1, (Match_ID))
    output = cur.fetchall()
    if len(output) :
        query2="""DELETE FROM Matches WHERE `Match_ID`=%s"""
        cur.execute(query2,(Match_ID))
        conn.commit()
        print("Entry with Match_ID ",Match_ID, " successfully deleted")
        t = input("Press Any key to continue: ")
        return

    else:
        print("Entry with Match_ID ",Match_ID ,"is non present" )
        t = input("Press Any key to continue: ")
        return

def deleteplayers():
    Player_ID = int(input("Enter the player_ID of the entry you want to delete :"))
    query1 = """SELECT * FROM Player WHERE `Player_ID`=%s;"""
    cur.execute(query1, (Player_ID))
    output = cur.fetchall()
    if len(output) :
        query2="""DELETE FROM Player WHERE `Player_ID`=%s"""
        cur.execute(query2,(Player_ID))
        conn.commit()
        print("Entry with Player_ID ",Player_ID, " successfully deleted")
        t = input("Press Any key to continue: ")
        return
    else:
        print("Entry with Player_ID ",Player_ID ,"is non present" )
        t = input("Press Any key to continue: ")
        return


def deletevenues():
    Venue_ID = int(input("Enter the Venue_ID of the entry you want to delete :"))
    query1 = """SELECT * FROM Venue WHERE `Venue_ID`=%s;"""
    cur.execute(query1, (Venue_ID))
    output = cur.fetchall()
    if len(output) :
        query2="""DELETE FROM Venue WHERE `Venue_ID`=%s"""
        cur.execute(query2,(Venue_ID))
        conn.commit()
        print("Entry with Venue_ID ",Venue_ID, " successfully deleted")
        t = input("Press Any key to continue: ")
        return
    else:
        print("Entry with Venue_ID ",Venue_ID ,"is non present" )
        t = input("Press Any key to continue: ")
        return


def deletebatstat():
    Player_ID = int(input("Enter the Player_ID of the entry you want to delete :"))
    query1 = """SELECT * FROM Batting_Statistics WHERE `Player_ID`=%s;"""
    cur.execute(query1, (Player_ID))
    output = cur.fetchall()
    if len(output) :
        query2="""DELETE FROM Batting_Statistics WHERE `Player_ID`=%s"""
        cur.execute(query2,(Player_ID))
        conn.commit()
        print("Entry with Player_ID ",Player_ID, " successfully deleted")
        t = input("Press Any key to continue: ")
        return
    else:
        print("Entry with Player_ID ",Player_ID ,"is non present" )
        t = input("Press Any key to continue: ")
        return

def deletebowlstat():
    Player_ID = int(input("Enter the Player_ID of the entry you want to delete :"))
    query1 = """SELECT * FROM Bowling_Statistics WHERE `Player_ID`=%s;"""
    cur.execute(query1, (Player_ID))
    output = cur.fetchall()
    if len(output) :
        query2="""DELETE FROM Bowling_Statistics WHERE `Player_ID`=%s"""
        cur.execute(query2,(Player_ID))
        conn.commit()
        print("Entry with Player_ID ",Player_ID, " successfully deleted")
        t = input("Press Any key to continue: ")
        return
    else:
        print("Entry with Player_ID ",Player_ID ,"is non present" )
        t = input("Press Any key to continue: ")
        return

def dispatchdelete():
    sp.call('clear',shell=True)
    print("Select the table from where u want to delete entry from: ")
    print("1. Matches")
    print("2. Player")
    print("3. Venue")
    print("4. Batting_Statistics")
    print("5. Bowling_Statistics")
    tablename = input("Enter the option: ")
    if(tablename == '1'):
        deletematches()
    elif(tablename == '2'):
        deleteplayers()
    elif(tablename == '3'):
        deletevenues()
    elif(tablename == '4'):
        deletebatstat()
    elif(tablename == '5'):
        deletebowlstat()
    else:
        print("Sorry, you have selected an invalid option")
        t = input("Press Any key to continue : ")
        return

def viewmatches():
    query = """SELECT * FROM Matches;"""
    try:
        print("Matches : ")
        print()
        cur.execute(query)
        conn.commit()
        output=cur.fetchall()
        print(tabulate(output,headers="keys", tablefmt='psql'))
        t = input("Press Any key to continue : ")
        return
    except Exception as e:
        print("Could not display table entries")
        t = input("Press Any key to continue : ")
        return

def viewplayers():
    query = """SELECT * FROM Player;"""
    try:
        cur.execute(query)
        conn.commit()
        output=cur.fetchall()
        print(tabulate(output,headers="keys", tablefmt='psql'))
        t = input("Press Any key to continue : ")
        return
    except Exception as e:
        print("Could not display Player")
        t = input("Press Any key to continue : ")
        return

def viewvenue():
    query = """SELECT * FROM Venue;"""
    try:
        cur.execute(query)
        conn.commit()
        output=cur.fetchall()
        print(tabulate(output,headers="keys", tablefmt='psql'))
        t = input("Press Any key to continue : ")
        return
        
    except Exception as e:
        print("Could not display Venue")
        t = input("Press Any key to continue : ")
        return
        
def viewbatstat():
    query = """SELECT * FROM Batting_Statistics;"""
    try:
        cur.execute(query)
        conn.commit()
        output=cur.fetchall()
        print(tabulate(output,headers="keys", tablefmt='psql'))
        t = input("Press Any key to continue : ")
        return
    except Exception as e:
        print("Could not display Batting_Statistics")
        t = input("Press Any key to continue : ")
        return

def viewbowlstat():
    query = """SELECT * FROM Bowling_Statistics;"""
    try:
        cur.execute(query)
        conn.commit()
        output=cur.fetchall()
        print(tabulate(output,headers="keys", tablefmt='psql'))
        t = input("Press Any key to continue : ")
        return
    except Exception as e:
        print("Could not display Bowling_Statistics")
        t = input("Press Any key to continue : ")
        return
    
def dispatchview():
    sp.call('clear',shell=True)
    print("Select the table to be viewed : ")
    print("1. Matches")
    print("2. Player")
    print("3. Venue")
    print("4. Batting_Statistics")
    print("5. Bowling_Statistics")
    tablename = input("Enter an option: ")
    if(tablename == '1'):
        viewmatches()
    elif(tablename == '2'):
        viewplayers()
    elif(tablename == '3'):
        viewvenue()
    elif(tablename == '4'):
        viewbatstat()
    elif(tablename == '5'):
        viewbowlstat()
    else:
        print("Sorry, you have selected an invalid option")
        t = input("Press Any key to continue : ")
        return

def userfuncsplayers():
    team_id = int(input("Enter Team ID: "))
    query = """SELECT * FROM Player WHERE `Team_ID` = %s;"""
    try:
        cur.execute(query,(team_id))
        conn.commit()
    except Exception as e:
        print("Could not execute query")
        t = input("Press any key to continue : ")
        return
    output = cur.fetchall()
    print(tabulate(output,headers="keys", tablefmt='psql'))
    t = input("Press any key to continue : ")
    return
    
def userfuncsresults():
    Team_ID = int(input("Enter Team ID : "))
    query = """SELECT Team_1_ID ,Team_2_ID , Winner_TeamID FROM Matches WHERE `Team_1_ID`=%s or `Team_2_ID`=%s;"""
    try :
        cur.execute(query,(Team_ID,Team_ID))
        conn.commit()
    except Exception as e :
        print("Could not execute query")
        t = input ("Press any key to continue: ")
        return
    result =cur.fetchall()
    print(tabulate(result,headers="keys", tablefmt='psql'))
    t = input ("Press any key to continue: ")
    return

def userfuncsavg():
    query = """SELECT avg(Total_Runs) AS Average_Runs from Matches;"""
    try:
        cur.execute(query)
        conn.commit()
    except Exception as e:
        print("Could not execute query")
        t = input("Press any key to continue: ")
        return
    result=cur.fetchall()
    print(tabulate(result,headers="keys",tablefmt='psql'))
    t = input("Press any key to continue: ")
    return
    
def userfuncszah():
    query = "SELECT * FROM Player where Player_Name LIKE 'ZAH%';"
    try:
        cur.execute(query)
        conn.commit()
    except Exception as e:
        print("Could not execute query")
        t = input("Press any key to continue: ")
        return
    output = cur.fetchall()
    print(tabulate(output,headers="keys", tablefmt='psql'))
    t = input("Press Any key to continue: ")
    return
    

def userfuncshighscore():
    team_id = int(input("Enter team id: "))
    query = """SELECT Highest_Score, Player_Name from (SELECT * from Player WHERE `Team_ID` = %s) AS temp NATURAL JOIN Batting_Statistics order by Highest_Score desc LIMIT 1;"""
    try:
        cur.execute(query,(team_id))
        conn.commit()
    except Exception as e:
        print("Could not execute query")
        t = input("Press any key to continue: ")
        return
    output = cur.fetchall()
    print(tabulate(output,headers="keys",tablefmt='psql'))
    t = input("Press any key to continue: ")
    return

def userfuncsbounds():
    query = """SELECT SUM(Number_of_4s + Number_of_6s) AS boundary , Team_ID from Player NATURAL JOIN Batting_Statistics GROUP BY Team_ID order by boundary desc LIMIT 1 ;"""
    try:
        cur.execute(query)
        conn.commit()
    except Exception as e:
        print("Could not execute query")
        t = input("Press any key to continue: ")
        return
    output = cur.fetchall()
    print(tabulate(output,headers="keys",tablefmt='psql'))
    t = input("Press any key to continue: ")
    return
    
def dispatchuserfuncs():
    sp.call('clear',shell=True)
    print("Select the query to be performed : ")
    print("1. Selection of all player details from a particular team.")
    print("2. Get results of all matches of a particular team.")
    print("3. Average runs scored in all matches at a particular venue.")
    print("4. Get all player names starting with ZAH")
    print("5. Highest score by a player for a particular team.")
    print("6. Team which scored Highest no of boundaries.")
    tablename = input("Enter any option: ")
    if(tablename == '1'):
        userfuncsplayers()
    elif(tablename == '2'):
        userfuncsresults()
    elif(tablename == '3'):
        userfuncsavg()
    elif(tablename == '4'):
        userfuncszah()
    elif(tablename == '5'):
        userfuncshighscore()
    elif(tablename == '6'):
        userfuncsbounds()
    else:
        print("Sorry, invalid option entered")
        t = input("Press Any key to continue : ")
        return
            
while(1):
    conn = pymysql.connect(host="localhost",
                              user="givegoodmarks",
                              port=3306,
                              password="givegoodmarks",
                              database='dna',cursorclass=pymysql.cursors.DictCursor)
    if(conn.open):
        print("Connected")
    else:
        print("Failed to Connect")
        
    cur = conn.cursor()
    tmp = input("Enter any key to continue : ")
    while(1):
        sp.call('clear', shell=True)
        print("1. Insert a new entry")
        print("2. Update an existing entry")
        print("3. Delete an existing entry")
        print("4. View existing entries")
        print("5. User Functionalities")
        print("6. Exit")
        ch = input()
        if(ch == '1'):
            dispatchinsert()
        elif(ch == '2'):
            dispatchupdate()
        elif(ch == '3'):
            dispatchdelete()
        elif(ch == '4'):
            dispatchview()
        elif(ch == '5'):
            dispatchuserfuncs()
        elif(ch == '6'):
            break
        else:
            print("Please Enter a valid option : ")
        
