import mysql.connector
import mysql.connector.pooling
import os


my_db = mysql.connector.connect(
    pool_name="mypool",
    pool_size=3,
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database="camping-trip-planner"
)


def sign_up_db(first_name, last_name, email, password):
    cursor = my_db.cursor()
    cmd = "INSERT INTO Tbl_Users (Users_Email, Users_Verified, Users_Password, " \
          "Users_First_Name, Users_Last_Name, Users_Username) VALUES " \
          "(%s,%s,%s,%s,%s,%s)"

    vls = (email, True, password, first_name, last_name, email)
    cursor.execute(cmd, vls)
    my_db.commit()
    cursor.close()


def check_if_user_exists_by_email(email):
    cursor = my_db.cursor()
    sql = "SELECT COUNT(1) FROM Tbl_Users WHERE Users_Email = %s"
    cursor.execute(sql, (email,))

    res = cursor.fetchall()

    if res[0][0] == 0:
        print("Email does not exist")
        return False
    else:
        print("Email exists")
        return True


def check_if_username_exists(username):
    cursor = my_db.cursor()
    sql = "SELECT COUNT(1) FROM Tbl_Users WHERE Users_Username = %s"
    cursor.execute(sql, (username,))

    res = cursor.fetchall()

    if res[0][0] == 0:
        print("Username does not exist")
        return False
    else:
        print("Username exists")
        return True


def get_password(email):
    cursor = my_db.cursor()
    sql = "SELECT Users_Password FROM Tbl_Users WHERE Users_Email = %s"
    cursor.execute(sql, (email,))

    res = cursor.fetchall()

    if len(res) == 0:
        return {"found": False, "pass": ""}
    else:
        return {"found": True, "pass": res[0][0]}


def add_element(element):
    cursor = my_db.cursor()
    cmd = "INSERT INTO Tbl_Elements (Elements_Name) VALUES " \
          "(%s)"

    vls = (element,)
    cursor.execute(cmd, vls)
    my_db.commit()
    cursor.close()


def delete_element(element):
    cursor = my_db.cursor()
    cmd = "DELETE FROM Tbl_Elements WHERE " \
          "Elements_Name= (%s)"

    vls = (element,)
    cursor.execute(cmd, vls)
    my_db.commit()
    cursor.close()


def edit_element(new, element):
    cursor = my_db.cursor()
    cmd = "UPDATE Tbl_Elements SET Elements_Name= (%s) WHERE " \
          "Elements_Name= (%s)"

    vls = (new, element)
    cursor.execute(cmd, vls)
    my_db.commit()
    cursor.close()


if __name__ == '__main__':
    thing = "trail mix"
    thing2 = "gum"
    edit_element(thing, thing2)
