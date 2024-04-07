import mysql.connector
class login:
    def __init__(self,arr,name,password):
        self.arr = arr
        self.name = name
        self.password = password

    def submit(self,arr,name,password):
            sql2 = 'select * from users where name = %s and password = %s'
            values2 = (name,password)
            cs.execute(sql2,values2)
            ans = cs.fetchall()
            rans = ans[0]
            if name == rans[1] and password == rans[2]:
                print("****Success****")
                return rans[0]
    def book(self,id):
        print("---- Enter Details ----")
        pname = input("Enter Passenger Name : ")
        page = input("Enter Passenger Age : ")
        print(" \nPress 'L' for Lower berth, 'M' for Middle Berth, 'U' for upper berth \n ")
        berth = input("Enter Berth : ")

        cs.execute('select count(*) from tickets where berth = "L"')
        berthL = cs.fetchall()[0][0]
        cs.execute('select count(*) from tickets where berth = "M"')
        berthM = cs.fetchall()[0][0]
        cs.execute('select count(*) from tickets where berth = "U"')
        berthU = cs.fetchall()[0][0]
        cs.execute('select count(*) from tickets where berth = "R"')
        berthRAC = cs.fetchall()[0][0]

        if berth == "L":
            if berthL < 10:
                berth = "L"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
            elif berthM < 10:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "M"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            elif berthU < 10:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "U"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            elif berthRAC < 7:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "R"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            else:
                print("Your Ticket in Waiting list")
                berth = "W"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()

        elif berth == "M":
            if berthM < 10:
                berth = "M"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
            elif berthL < 10:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "L"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            elif berthU < 10:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "U"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            elif berthRAC < 7:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "R"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            else:
                print("Your Ticket in Waiting list")
                berth = "W"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()

        elif berth == "U":
            if berthU < 10:
                berth = "U"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
            elif berthL < 10:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "L"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            elif berthM < 10:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "M"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            elif berthRAC < 7:
                print(f"SORRY!! No Tickets available on Berth '{berth}'.")
                berth = "R"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()
                print(f"So your berth changed to Berth '{berth}'")
            else:
                print("Your Ticket in Waiting list")
                berth = "W"
                sql4 = 'INSERT INTO tickets VALUES(%s,%s,%s,%s)'
                vals4 = (id, pname, page, berth)
                cs.execute(sql4, vals4)
                udb.commit()

        print("---- Successfully Booked ----")
    def canceltkts(self):
        while True:
            print("---- Ticket Cancelation ----")
            pname = input("Enter Passenger name : ")
            page = int(input("Enter Passenger age : "))
            sql7 = 'SELECT * from tickets where pname = %s and age = %s'
            vals7 = (pname, page)
            cs.execute(sql7, vals7)
            pInfo = cs.fetchall()
            if len(pInfo) >0:
                print("Press '1' for Confirm Cancellation")
                user_choice3 = int(input("Enter : "))
                if user_choice3 == 1:
                    sql6 = 'DELETE FROM tickets where pname = %s and age = %s'
                    vals6 = (pname,page)
                    cs.execute(sql6,vals6)
                    udb.commit()
                    print(f"--- Passenger {pname}'s Ticket Cancelled Successfully ----")
                    cs.execute('SELECT * FROM tickets WHERE berth = "R"')
                    rac = cs.fetchall()
                    cs.execute('SELECT * FROM tickets WHERE berth = "W"')
                    wl = cs.fetchall()
                    if len(rac) > 0:
                        b = pInfo[0][3]
                        racPname = rac[0][1]
                        racPage = rac[0][2]
                        sql8 = 'UPDATE tickets SET berth = %s where pname = %s and age = %s'
                        vals8 = (b,racPname,racPage)
                        cs.execute(sql8,vals8)
                        udb.commit()
                    else:
                        b = pInfo[0][3]
                        wlPname = wl[0][1]
                        wlPage = wl[0][2]
                        sql8 = 'UPDATE tickets SET berth = %s where pname = %s and age = %s'
                        vals8 = (b, wlPname, wlPage)
                        cs.execute(sql8, vals8)
                        udb.commit()

                    break
                else:
                    print("Canelation failed \nTry Again")
            else:
                print("No passenger found!!")
                print(" \n 1.Try again \n 2.Main Menu")
                us = int(input("Enter : "))
                if us == 1:
                    continue
                else:
                    break
    def showtickts(self,id):
        sql5 = 'select * from tickets where id = %s'
        vals5 = (id,)
        cs.execute(sql5,vals5)
        tickets = cs.fetchall()
        return tickets
    def availtickts(self):
        cs.execute('select count(*) from tickets where berth = "L"')
        berthL = cs.fetchall()[0][0]
        cs.execute('select count(*) from tickets where berth = "M"')
        berthM = cs.fetchall()[0][0]
        cs.execute('select count(*) from tickets where berth = "U"')
        berthU = cs.fetchall()[0][0]
        cs.execute('select count(*) from tickets where berth = "R"')
        berthRAC = cs.fetchall()[0][0]
        cs.execute('select count(*) from tickets where berth = "W"')
        berthWL = cs.fetchall()[0][0]
        print(f"---- Available Tickets ---- "
              f"\n1) {10 - berthL} Lower Berth Tickets. "
              f"\n2) {10 - berthM} Middle Berth Tickets. "
              f"\n3) {10 - berthU} Upper Berth Tickets. "
              f"\n4) {7 - berthRAC} RAC Tickets ")

class regis:
    def __init__(self,arr, name,passw,rpass):
        self.arr = arr
        self.name = name
        self.passw = passw
        self.rpass = rpass
    def register(self, arr, name, passw, rpass):
        sql3 = 'select * from users where name = %s and password = %s'
        values3 = (name, passw)
        cs.execute(sql3, values3)
        ans = cs.fetchall()
        if len(ans) == 0:
            if passw == rpass:
                sql1 = "insert into users(name,password) values(%s,%s)"
                values1 = (name,passw)
                cs.execute(sql1,values1)
                udb.commit()
                print("****Successfully registered")
                return 1
            else:
                print("****Check password****")
                return 2
        else:
            print("***** User already exixts ****")
            return 3

arr = {}
udb = mysql.connector.connect(host='localhost', user='root', password='aaaa')
cs = udb.cursor()
cs.execute('use user_sampledb')
wl = True
while wl:
    print("***** Train Reservation ****")
    print("---- 1. Login ----")
    print("---- 2. Register ----")
    print("---- 3. Exit")
    a = int(input("Enter  : "))
    if a == 1 :
        lg = True
        while lg:
            print("---- LOGIN ----")
            name = input("Enter Username : ")
            password = input("Enter Password : ")
            temp = login(arr,name,password)
            try:
                logWindow = True
                while logWindow:
                    id = temp.submit(arr,name,password)
                    print("Welcome "+name+"!")
                    print("----------")
                    print("1.Book Tickets \n2.Cancel Ticket \n3.Available Tickets \n4.Booked Tickets \n5.Exit")
                    user_choice = int(input("Enter : "))
                    if user_choice == 1:
                        temp.book(id)
                        print(" \n 1. Go Back \n 2. Exit")
                        user_choice2 = int(input("Enter : "))
                        if user_choice2 == 1 :
                            continue
                        else:
                            logWindow = False
                            wl = False
                            lg = False
                            print("\nThank you!! \nHave a Safe Journey!!")
                    elif user_choice == 4:
                        tkts = temp.showtickts(id)
                        for i in range(len(tkts)):
                            a = 1+i
                            print(f" \nTicket {a} :")
                            print(f"Passenger Name : {tkts[i][1]} \nPassenger age : {tkts[i][2]} \nBerth : {tkts[i][3]}")
                        print(" \n 1.Go Back \n 2.Exit")
                        print(tkts)
                        us = int(input("Enter : "))
                        if us == 1:
                            continue
                        else:
                            logWindow = False
                            wl = False
                            lg = False
                            print("\nThank you!! \nHave a Safe Journey!!")
                    elif user_choice == 3:
                        temp.availtickts()
                        print(" \n 1.Go Back \n 2.Exit")
                        us = int(input("Enter : "))
                        if us == 1:
                            continue
                        else:
                            logWindow = False
                            wl = False
                            lg = False
                            print("\nThank you!! \nHave a Safe Journey!!")
                    elif user_choice == 2:
                        temp.canceltkts()
                        print(" \n 1.Go Back \n 2.Exit")
                        us = int(input("Enter : "))
                        if us == 1:
                            continue
                        else:
                            logWindow = False
                            wl = False
                            lg = False
                            print("\nThank you!! \nHave a Safe Journey!!")
                    elif user_choice == 5:
                        logWindow = False
                        wl = False
                        lg = False
                        print("\nThank you!! \nHave a Safe Journey!!")
                    break
            except:
                print("****Invalid Credentials****")
                print("Press 1 to try again")
                print("Press 2 to main screen")
                lg1 = int(input("Enter : "))
                if lg1 == 1:
                    continue
                elif lg1 == 2:
                    break
    elif a==2:
        while True:
            print("---- Register ----")
            name = input("Enter Username : ")
            passw = input("Enter Password : ")
            rpass = input("Re-Enter Password : ")
            temp = regis(arr,name,passw,rpass)
            a1 = temp.register(arr,name,passw,rpass)
            if a1 == 1:
                break
            elif a1 == 3:
                print("")
                print("**** Press 1 for mainmenu ****")
                print("")
                print("**** Press 2 for try again ****")
                a2 = int(input("Enter : "))
                if a2 == 1:
                    break
                elif a2 == 2:
                    continue
                else:
                    print("*** Type 1 or 2")

    else:
        break

