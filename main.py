import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

#create table
cursor.execute("CREATE TABLE users(username, email, password)")

#add 7 usernames and passwords
cursor.execute("INSERT INTO users VALUES (?,?,?)", ("Maria Iqbal", "mariaiqbal@gmail.com", "hello123"))
cursor.execute("INSERT INTO users VALUES (?,?,?)", ("Travis Scott", "utopia@gmail.com", "ilovemusic"))
cursor.execute("INSERT INTO users VALUES (?,?,?)", ("Kylie Jenner", "kj@gmail.com", "stormibaby"))
cursor.execute("INSERT INTO users VALUES (?,?,?)", ("Aubrey Drake", "torontotingz@gmail.com", "lightskingod"))
cursor.execute("INSERT INTO users VALUES (?,?,?)", ("Playboi Carti", "wholelottared@gmail.com", "atldraco"))
cursor.execute("INSERT INTO users VALUES (?,?,?)", ("Abel Tesfaye", "65spencerave@gmail.com", "starboy"))
cursor.execute("INSERT INTO users VALUES (?,?,?)", ("Advait Patil", "advaitpatil@gmail.com", "rutgers2004"))
cursor.execute("INSERT INTO users VALUES (?,?,?)", ("Shanika Paul", "shanikapaul@gmail.com", "forallthedogs"))
conn.commit()
conn.close()
