from tkinter import Tk
from tkinter.filedialog import askopenfilename
import getpass
import csv
import mysql.connector


def main():
    usr = 'username'
    psswd = 'password'
    hostnm = 'hostname'
    db = 'database'
    # Connect to MySQL database.
    conn = mysql.connector.connect(user=usr,password=psswd, host=hostnm, database=db)

    try:
        cursor = conn.cursor()
        # Drop table.
        cursor.execute("DROP TABLE table")
        # Create new table.
        cursor.execute("CREATE TABLE table(col1 VARCHAR(20) NOT NULL, col2 VARCHAR(20) NOT NULL, col3 VARCHAR(20) NOT NULL)")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        exit(0)

    with open(openFile()) as f:
            # Read file.
            reader = csv.reader(f, delimiter=',')
            # Skip first line (header).
            next(reader)
            for row in reader:
                # Clean each row.
                row = str(row).replace("[","").replace("\'","").replace("\'","").replace("]","").split(",")
                # Define SQL query.
                sql = "INSERT INTO table VALUES('" + str(row[0]) + "','" + str(row[1]) + "','" + str(row[2]) + "')"
                # Execute SQL query.
                cursor.execute(sql)

    # Commit transaction.
    conn.commit()
    # Close connection.
    cursor.close()
    conn.close()


def openFile():
    # Create Tk object.
    root = Tk()
    # Hide blank window.
    root.withdraw()
    # Get user name.
    user = getpass.getuser()
    path = 'C:/Users/%s/Downloads/' % user
    ftypes = (("CSV File", "*.csv"), ("All Files", "*.*"))
    # Get file name.
    root.fileName = askopenfilename(filetypes=ftypes, initialdir=path)
    return root.fileName

main()
