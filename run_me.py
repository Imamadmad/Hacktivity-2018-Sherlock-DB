"""
======================================================================
README  README  README  README  README  README  README  README  README

                        The Game's Afoot!

  Sherlock Holmes needs your help to solve a murder mystery! Become a
    database wizz as you help him sieve through the information to 
                       discover who dunnit.


To begin your adventure, please run this file. All the information and
         materials you need will be spawned by this program.


END_README  END_README  END_README  END_README  END_README  END_README
======================================================================
"""

import time, os, random
import sqlite3 as sql

def main() :
    # Who are you and who am I
    for i in range(3) :
        print("Connecting.  ", end='\r')
        time.sleep(0.3)
        print("Connecting.. ", end='\r')
        time.sleep(0.3)
        print("Connecting...", end='\r')
        time.sleep(0.3)

    print("Connected to Sherlock Holmes")

    sherlock("Ah, so you're the new apprentice Watson sent me.")
    sherlock("You're shorter than I imagined.")
    sherlock("Ah well, what's your name then?")

    name = you("I need your name to continue.").strip()
    name = ' '.join([n[0].upper() + n[1:].lower() for n in name.split(' ')])
    sherlock("Right then {}, I've got a mystery for you to solve.".format(name))

    sherlock("Oh, I should probably introduce myself as well. I'm Sherlock Holmes, the world's best consulting detective.")
    sherlock("...")
    sherlock("Insert proper good dialog stuff here")

    # Basic mystery setup
    sherlock("rewrite this but with better words")
    sherlock("An old gentleman, Mr Samuel Thompson, has been stabbed in the back in his house. A boot print was found at the crime scene in blood, along with a strand of hair.")


    # Trying out the DB: Seeing what tables exist
    try :
        os.remove("pleasantville.db")

    except FileNotFoundError:
        do = "nothing"
    
    create_initial_db()
    create_db_access_script()
    sherlock("I have created a database for you with information about the town. I've also created a program through which you can access that database.")

    sherlock("We can open this program in IDLE for you to edit. Search IDLE (Python 3.5) on your computer, go to File -> Open, and then find the program.")
    sherlock("Have you done that?")
    wait_for_yes()

    sherlock("Good! Now run the file by hitting the F5 key on your keyboard.")
    
    # Looking at our info: SELECT FROM WHERE
    sherlock("You should see a list of available tables in the database listed. They are People and Buisnesses.")
    sherlock("A table is a place where we keep information.")
    sherlock("Look in the program file we have open in IDLE and see the line which says 'SELECT type, tbl_name FROM sqlite_master'. Can you see it?")
    wait_for_yes()

    sherlock("A table has a name and is made up of columns and rows. Let's give you an example.")
    sherlock("Replace the line I mentioned earlier with 'SELECT first_name, last_name, age FROM People' and then run the program.")
    sherlock("Have you done this?")
    wait_for_yes()

    sherlock("The output of this program is part of the database table. The table columns contain different kinds of information, such as name and age")
    sherlock("and the rows are the different things we are holding information on, in this case individual people.")
    sherlock("Does this make sense?")
    wait_for_yes()

    sherlock("The line we added is what's known as a SELECT statement. We use it to select information from a table.")
    sherlock("Its form is as follows: SELECT <column names> FROM <table name>")
    sherlock("Can you modify the line we just added to just give us the age column from the people table?")
    sherlock("Paste your answer in here once you think you have it right.")

    check_query("""
        SELECT age FROM People
    """)

    sherlock("Brilliant!")
    sherlock("Now, instead of stating specific columns, we can instead use a * to mean 'all columns'.")
    sherlock("Can you select all columns from the people table?")


    check_query("""
        SELECT * FROM People
    """)

    sherlock("Good work!")
    sherlock("Now, like how we can select only certain columns, we can also select only certain rows.")
    sherlock("We do this using a WHERE clause. So we can say: \"SELECT * from People WHERE hair_colour = 'brown'\"")
    sherlock("Try that in the database access program. Have you done it yet?")
    wait_for_yes()

    sherlock("Very good. Now, write me a query to see everybody whose job is as a Mechanic.")

    check_query("""
        SELECT * FROM People WHERE job = 'Mechanic'
    """)

    sherlock("Very good. Now I think you're ready to start solving crime!")

    # Need to SELECT a group of people to contact next
    interviewees = ["mary", "susan", "dan"]
    sherlock("Let's start with speaking to everybody who lives on Main St. Who should we speak to first?")

    while len(interviewees) > 0 :
        interviewee = you("You need to give me somebody's name.").lower()

        if "mary" in interviewee or "johnson" in interviewee :
            print("TODO: Mary's story. Learning about NULL and updating rows.")
            interviewees.remove("mary")

        elif "susan" in interviewee or "knowles" in interviewee :
            print("TODO: Susan's story. Dead end here.")
            interviewees.remove("susan")

        elif "dan" in interviewee or "miles" in interviewee :
            sherlock("Hello Dan. Mind if we speak with you?")
            dan("Sure thing. What do you need to know.")
            sherlock("We're investigating the murder of Mr Samuel Thompson.")
            sherlock("We've a list of people in the town. Is there anything you can say about any of them?")
            dan("Unfortunately, your information is out of date. Mike left the town in January to go back to Uni, and Colin moved on a year ago.")
            sherlock("Hmm, that is unfortunate.")
            sherlock("Have there been any newcommers in the town of late?")
            dan("Hmm, well Michelle Curtin came in to replace Colin at the bakery a few months back, and Justin's brother Henry got back from his gap year a few weeks back.")
            sherlock("We'll have to update our information. Thank you Dan.")
            dan("No problem.")

            sherlock("{}, I need you to update our people table to match this new information.")
            sherlock("We'll need to use an INSERT query to add the new people and DELETE to remove those who've left.")
            sherlock("Let's start with DELETE. Are you ready?")
            wait_for_yes()

            sherlock("Good, then let's get started.")
            sherlock("To remove a person, we need to use a DELETE query. This is similar to a SELECT FROM WHERE query, except without the SELECT part.")
            sherlock("We write: 'DELETE FROM table WHERE condition")
            sherlock("Try using the program to delete from person where the person's name is Mike.")
            sherlock("Can I check yet?")
            wait_for_yes()

            while not check_change("select * from people where first_name = 'Mike'", 0) :
                sherlock("It doesn't quite seem to have worked. Try again.")
                sherlock("Can I check yet?")
                wait_for_yes()

            sherlock("Very good! Now, do the same for Colin.")
            sherlock("Are you ready?")
            wait_for_yes()

            while not check_change("select * from people where first_name = 'Colin'", 0) :
                sherlock("It doesn't quite seem to have worked. Try again.")
                sherlock("Can I check yet?")
                wait_for_yes()

            sherlock("You're getting to be good at this!")

            print ("~~~ END OF DEMO ~~~")

        else :
            sherlock("{} doesn't live on Main St. Try again.".format(interviewee))


        # Colin the Baker: modifying a table - Intermediate only

        # Mary the Cafe Owner: updating rows

        # Dan the Reporter: Insert and delete rows

        # Susan the Fishmonger: Dead end

    # Pulling our info together: left join

    # Killer identification: SELECT FROM JOIN WHERE


''' A decorator which handles the openning and closing of
    database connections, so each function doesn't have to
    do so itself.

    Each wrapped function needs its first parameter to be
    c (cursor) when declared, but this parameter is not then
    used when calling he function.
'''
def connect(some_function) :
    def wrapper(*args, **kwargs) :
        conn = sql.connect("pleasantville.db")
        conn.row_factory = sql.Row
        c = conn.cursor()

        result = some_function(c, *args, **kwargs)

        conn.commit()
        conn.close()
        return result
    return wrapper

# Helper functions
def sherlock(msg) :
    print()
    print("Sherlock: {}".format(msg))
    time.sleep(0.05 * len(msg))

def dan(msg) :
    print()
    print("Dan: {}".format(msg))
    time.sleep(0.05 * len(msg))

def you(err) :
    response = input(">>> ").strip()

    if len(response) > 0 :
        return response
    else :
        sherlock(err)
        return you(err)

def wait_for_yes() :
    response = input(">>> ").strip().lower()

    if "yes" not in response :
        sherlock("Ask a tutor for help if you need it. Write 'yes' when you're ready to move on.")
        wait_for_yes()

def check_query(expected_query) :
    success = True

    test_query = query(expected_query)

    try :
        their_query = query(input("Query:  "))

        if len(their_query) == len(test_query) :
            for x in range(len(their_query)) :
                if their_query[x] != test_query[x] :
                    success = False
                    break
        else :
            success = False
    except :
        success = False

    if not success :
        sherlock(random.choice(["That's not quite right. Try again.", "Nearly there. Have another go.", "Not quite. Give it another try."]))
        check_query(expected_query)

def check_change(test_query, num_lines_expected) :
    result = query(test_query)

    return len(result) == num_lines_expected

@connect
def create_initial_db(c) :
    c.execute("""
        CREATE TABLE People (
            first_name  TEXT    NOT NULL,
            last_name   TEXT    NOT NULL,
            age         INT     NOT NULL,
            address     TEXT,
            hair_colour TEXT,
            shoe_size   INT,
            job         TEXT,
            employer    TEXT
        )
    """)

    c.execute("""
        CREATE TABLE Businesses (
            name            TEXT    NOT NULL,
            staff           INT,
            annual_profit   INT
        )
    """)


    c.execute("""INSERT INTO People (first_name, last_name, age, address, hair_colour, shoe_size, job, employer)
        VALUES ('Mary', 'Johnson', 34, 'Main St', 'red', 8, 'Owner', 'Seaworth Cafe')""")

    c.execute("""INSERT INTO People (first_name, last_name, age, address, hair_colour, shoe_size, job, employer)
        VALUES ('Anne', 'Straus', 52, 'Green Ln', 'brown', 9, 'Editor/Owner', 'The Pleasantville Times')""")

    c.execute("""INSERT INTO People (first_name, last_name, age, address, hair_colour, shoe_size, job, employer)
        VALUES ('Colin', 'O''Brien', 53, 'Wave Ave', 'brown', 11, 'Baker', 'Baker''s Treat')""")

    c.execute("""INSERT INTO People (first_name, last_name, age, address, hair_colour, shoe_size, job, employer)
        VALUES ('Mike', 'O''Brien', 23, 'Abbey Rd', 'blond', 9, 'Student/Fishmonger', 'Catch''o the Day')""")

    c.execute("""INSERT INTO People (first_name, last_name, age, address, hair_colour, shoe_size, job, employer)
        VALUES ('Susan', 'Knowles', 47, 'Main St', 'blond', 7, 'Fishmonger', 'Catch o'' the Day')""")

    c.execute("""INSERT INTO People (first_name, last_name, age, address, hair_colour, shoe_size, job, employer)
        VALUES ('Dan', 'Miles', 24, 'Main St', 'brown', 10, 'Reporter', 'The Pleasantville Times')""")

    c.execute("""INSERT INTO People (first_name, last_name, age, address, hair_colour, shoe_size, job, employer)
        VALUES ('Kate', 'Brown', 23, 'Wave Ave', 'brown', 8, 'Mechanic', 'Service-Stop')""")

    c.execute("""INSERT INTO People (first_name, last_name, age, address, hair_colour, shoe_size, job, employer)
        VALUES ('Justin', 'Straus', 19, 'Green Ln', 'brown', 13, 'Mechanic', 'Service-Stop')""")

@connect
def query(c, query) :
    c.execute(query)
    return c.fetchall()


def create_db_access_script() :
    with open("access_database.py", 'w') as accessor :
        accessor.write("""
query = \"\"\"

-- edit query below this line


SELECT type, tbl_name FROM sqlite_master







-- edit query above this line

\"\"\"







# ===== DO NOT TOUCH ANYTHING BELOW THIS LINE =====

import sqlite3 as sql


def connect(some_function) :
    def wrapper(*args, **kwargs) :
        conn = sql.connect("pleasantville.db")
        conn.row_factory = sql.Row
        c = conn.cursor()

        result = some_function(c, *args, **kwargs)

        conn.commit()
        conn.close()
        return result
    return wrapper

@connect
def run_query(c, query) :
    c.execute(query)

    result = c.fetchall()

    if len(result) < 1 :
        print("No output")
        return

    print("\t".join(result[0].keys()))

    for row in result :
        print("\t".join([str(x) for x in tuple(row)]))

if __name__ == "__main__" :
    run_query(query)
            """.strip())

if __name__ == "__main__" :
    main()