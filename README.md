# Cricket World Cup
## A database design to cater to needs of organizing a cricket world cup tournament

### Team Members
- Srikar Desu (2020101003)
- Ayush Agrawal (2020101025)
- Aryan Gupta (2020101091)

### Demo Video Link
https://drive.google.com/file/d/1fNottO49lt9JdLJoSNblNKhTOIsDy-qu/view?usp=sharing

### List of Commands
- Insert Player (`INSERT`)
> Insert a new player into database.
- Insert Venue (`INSERT`)
> Insert a new venue into the database.
- Insert Match (`INSERT`)
> Insert a new match into the database.
- Update Player Records (`UPDATE`)
> Updates the details of existing players in the database.
- Delete Player (`DELETE`)
> Deletes the record of an existing player in the database.
- View Player (`READ`)
> View the details of all existing players.
- View Player by Team ID (`PROJECTION`)
> View the list of all players of a particular team
- View Result (`AGGREGATE + PROJECTION`)
> View result of any completed match between two teams
- Average Runs (`AGGREGATE`)
> View average runs scored in the tournament so far
- Search Player (`PROJECTION`)
> View details of players starting with a particular string (like `ZAH`)
- Highest Score (`ANALYSIS`)
> View highest runs scored by a player of a particular team
- Boundaries Scored (`ANALYSIS`)
> Get number of boundaries scored by each team
- Exit 
> Exit from the Application.

### Requirements
- python3
```
$ sudo apt-get update
$ sudo apt-get install python3.8
```
- MySQL
- PyMySQL
```
$ sudo apt-get install python3-pip
$ pip3 install pymysql
```
### Installation
To replicate the Initial Data in database, run the `dump.sql` file in MySQL CLI.
```
mysql> source \{pathtoyourfile}\dump.sql;
```
Change the username and password in the following lines(770-774) in WorldCup.py
```
conn = pymysql.connect(host="localhost",
                              user="username",
                              port=3306,
                              password="password",
                              database='dna',cursorclass=pymysql.cursors.DictCursor)
```
Run using
`python3 WorldCup.py`


            
