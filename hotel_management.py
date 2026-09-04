import os
import platform
import sqlite3

s = 0
z = 0

mydb = sqlite3.connect("hotel.db")
mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS custdata (
    custname TEXT,
    addr TEXT,
    indate TEXT,
    outdate TEXT
)
""")
mycursor.execute("""
CREATE TABLE IF NOT EXISTS roomtype (
    sno TEXT,
    roomtype TEXT,
    rent INTEGER
)
""")
mycursor.execute("""
CREATE TABLE IF NOT EXISTS restaurent (
    sno INTEGER,
    itemname TEXT,
    rate INTEGER
)
""")
mycursor.execute("""
CREATE TABLE IF NOT EXISTS laundary (
    sno INTEGER,
    itemname TEXT,
    rate INTEGER
)
""")
mydb.commit()

# Seed lookup tables with the same reference data from the original project,
# only if they're empty (so re-running the script doesn't duplicate rows)
mycursor.execute("SELECT COUNT(*) FROM roomtype")
if mycursor.fetchone()[0] == 0:
    mycursor.executemany(
        "INSERT INTO roomtype VALUES (?,?,?)",
        [('1', 'type A', 1000), ('2', 'type B', 2000), ('3', 'type C', 3000), ('4', 'type D', 4000)]
    )

mycursor.execute("SELECT COUNT(*) FROM restaurent")
if mycursor.fetchone()[0] == 0:
    mycursor.executemany(
        "INSERT INTO restaurent VALUES (?,?,?)",
        [(1, "tea", 10), (2, "coffee", 10), (3, "colddrink", 20), (4, "samosa", 10),
         (5, "sandwich", 50), (6, "Dhokla", 30), (7, "kachori", 10), (8, "milk", 20),
         (9, "noodles", 50), (10, "pasta", 50)]
    )

mycursor.execute("SELECT COUNT(*) FROM laundary")
if mycursor.fetchone()[0] == 0:
    mycursor.executemany(
        "INSERT INTO laundary VALUES (?,?,?)",
        [(1, "pant", 10), (2, "shirt", 10), (3, "suit", 10), (4, "sari", 10)]
    )
mydb.commit()


def registercust():
    L = []
    name = input("ENTER NAME: ")
    L.append(name)
    addr = input("ENTER ADDRESS: ")
    L.append(addr)
    indate = input("ENTER CHECK IN DATE: ")
    L.append(indate)
    outdate = input("ENTER CHECK OUT DATE: ")
    L.append(outdate)
    cust = tuple(L)
    sql = "insert into custdata(custname,addr,indate,outdate) values(?,?,?,?)"
    mycursor.execute(sql, cust)
    mydb.commit()


def roomtypeview():
    print("DO YOU WANT TO SEE ROOM TYPE AVAILABLE : ENTER 1 FOR YES :")
    ch = int(input("ENTER YOUR CHOICE: "))
    if ch == 1:
        sql = "select * from roomtype"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)


def roomrent():
    global s
    print("WE HAVE THE FOLLOWING ROOMS FOR YOU:-")
    print("1. TYPE A----> RS 1000 PN/-")
    print("2. TYPE B----> RS 2000 PN/-")
    print("3. TYPE C----> RS 3000 PN/-")
    print("4. TYPE D----> RS 4000 PN/-")
    x = int(input("ENTER YOUR CHOICE PLEASE-> "))
    n = int(input("FOR HOW MANY NIGHTS DID YOU STAY: "))
    if x == 1:
        print("YOU HAVE OPTED ROOM TYPE A")
        s = 1000 * n
    elif x == 2:
        print("YOU HAVE OPTED ROOM TYPE B")
        s = 2000 * n
    elif x == 3:
        print("YOU HAVE OPTED ROOM TYPE C")
        s = 3000 * n
    elif x == 4:
        print("YOU HAVE OPTED ROOM TYPE D")
        s = 4000 * n
    else:
        print("PLEASE CHOOSE A ROOM")
        return
    print("your room rent is =", s, "\n")


def restaurentmenuview():
    print("DO YOU WANT TO SEE MENU AVAILABLE : ENTER 1 FOR YES :")
    ch = int(input("ENTER YOUR CHOICE: "))
    if ch == 1:
        sql = "select * from restaurent"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)


def orderitem():
    global s
    print("DO YOU WANT TO SEE MENU AVAILABLE : ENTER 1 FOR YES :")
    ch = int(input("ENTER YOUR CHOICE: "))
    if ch == 1:
        sql = "select * from restaurent"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)
    print("DO YOU WANT TO PURCHASE FROM ABOVE LIST: ENTER YOUR CHOICE:")
    d = int(input("ENTER YOUR CHOICE: "))
    items = {
        1: ("TEA", 10),
        2: ("COFFEE", 10),
        3: ("COLDDRINK", 20),
        4: ("SAMOSA", 10),
        5: ("SANDWICH", 50),
        6: ("DHOKLA", 30),
        7: ("KACHORI", 10),
        8: ("MILK", 20),
        9: ("NOODLES", 50),
        10: ("PASTA", 50),
    }
    if d in items:
        name, price = items[d]
        print("YOU HAVE ORDERED", name)
        a = int(input("ENTER QUANTITY: "))
        s = price * a
        print("YOUR AMOUNT FOR", name, "IS :", s, "\n")
    else:
        print("PLEASE ENTER YOUR CHOICE FROM THE MENU")


def laundarybill():
    global z
    print("DO YOU WANT TO SEE RATE FOR LAUNDARY : ENTER 1 FOR YES :")
    ch = int(input("ENTER YOUR CHOICE: "))
    if ch == 1:
        sql = "select * from laundary"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)
        y = int(input("ENTER YOUR NUMBER OF CLOTHES-> "))
        z = y * 10
        print("YOUR LAUNDARY BILL:", z, "\n")
    return z


def lb():
    print(z)


def res():
    print(s)


def viewbill():
    a = input("ENTER CUSTOMER NAME: ")
    print("CUSTOMER NAME :", a, "\n")
    print("LAUNDAREY BILL:")
    lb()
    print("RESTAURENT BILL:")
    res()


def Menuset():
    print("ENTER 1: TO ENTER CUSTOMER DATA")
    print("ENTER 2 : TO VIEW ROOMTYPE")
    print("ENTER 3 : FOR CALCULATING ROOM BILL")
    print("ENTER 4 : FOR VIEWING RESTAURENT MENU")
    print("ENTER 5 : FOR RESTAURENT BILL")
    print("ENTER 6 :FOR LAUNDARY BILL")
    print("ENTER 7 : FOR COMPLETE BILL")
    print("ENTER 8 : FOR EXIT:")
    try:
        userinput = int(input("PLEASE SELECT AN ABOVE OPTION: "))
    except ValueError:
        exit("\nHI THAT'S NOT A NUMBER")
    else:
        if userinput == 1:
            registercust()
        elif userinput == 2:
            roomtypeview()
        elif userinput == 3:
            roomrent()
        elif userinput == 4:
            restaurentmenuview()
        elif userinput == 5:
            orderitem()
        elif userinput == 6:
            laundarybill()
        elif userinput == 7:
            viewbill()
        elif userinput == 8:
            quit()
        else:
            print("ENTER CORRECT CHOICE")


def runagain():
    runagn = input("\nWANT TO RUN AGAIN y/n: ")
    while runagn.lower() == 'y':
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        Menuset()
        runagn = input("\nWANT TO RUN AGAIN y/n: ")


Menuset()
runagain()
