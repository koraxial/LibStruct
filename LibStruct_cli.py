
#Libstruct-CLI

print("Connecting Server...")
import mysql.connector
mydb = mysql.connector.connect(
     host ="########", 
     user ="########", 
     password ="########", 
     database = "Library")
print("Connection Succeeded")
mycursor = mydb.cursor()

#FUNCTIONS:
global data
global ctr

#SEARCH FUNCTIONS:
def BookCodeSearch():
    BookN = int(input("Enter Book Code to find record: ")) 
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        if i[0]== BookN:
            print(i)

def BookNameSearch():
    BookN = input("Enter Book Name to find record: ") 
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        if i[1]== BookN:
            print(i)

def AuthorSearch():
    BookN = input("Enter Author Name to find record: ") 
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        if i[2]== BookN:
            print(i)

def PriceSearch():
    BookN = int(input("Enter Book Price to find record: ")) 
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        if i[3] == BookN:
            print(i)

def StockSearch():
    
    sql = "select Sno, BookName, TotalQty from librarydb"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    widths = []
    columns = []
    t = '|'
    separator = '+' 

    for cd in mycursor.description:
        tup = 20
        widths.append(max((tup), len(cd[0])))
        columns.append(cd[0])
        

    for w in widths:
        t += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(t % tuple(columns))
    print(separator)
    for row in results:
        print(t % row)
    print(separator)


def ASearch():
    sql = "select Sno, BookName, Available from librarydb"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    widths = []
    columns = []
    t = '|'
    separator = '+' 

    for cd in mycursor.description:
        tup = 20
        widths.append(max((tup), len(cd[0])))
        columns.append(cd[0])
        

    for w in widths:
        t += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(t % tuple(columns))
    print(separator)
    for row in results:
        print(t % row)
    print(separator)

#PRIMARY FUNCTIONS
def ViewAll ():
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    for i in data:
        print(i)

def newView():
    sql = "select * from librarydb"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    widths = []
    columns = []
    t = '|'
    separator = '+' 

    for cd in mycursor.description:
        tup = 20
        widths.append(max((tup), len((cd[0]))))
        columns.append(cd[0])

    for w in widths:
        t += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(t % tuple(columns))
    print(separator)
    for row in results:
        print(t % row)
    print(separator)
        
def InsertVal():
    SNo = int(input("Enter BookCode: "))
    BookName = str(input("Enter Book Name: "))
    AuthorName = str(input("Enter Author Name: "))
    Price = int(input("Enter price of book: "))
    TotalQty = int(input("Enter total stock of book: "))
    Available = 0 + TotalQty

    q2 = "insert into librarydb (Sno, BookName, AuthorName, Price, TotalQty, Available) values(%s, %s, %s, %s,%s,%s)"
    val = (SNo, BookName, AuthorName, Price, TotalQty, Available)
    mycursor.execute(q2,val)
    mydb.commit()
    print("\nRecord added successfully")

def delete():
    sql = "SELECT Sno, BookName FROM librarydb"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    widths = []
    columns = []
    t = '|'
    separator = '+' 

    for cd in mycursor.description:
        tup = 20
        widths.append(max((tup), len((cd[0]))))
        columns.append(cd[0])

    for w in widths:
        t += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(t % tuple(columns))
    print(separator)
    for row in results:
        print(t % row)
    print(separator)

    Snow = int(input("\nEnter Book Code of record to be deleted: "))
    q3 = "delete from librarydb where SNo = %s"
    mycursor.execute(q3,(Snow,))
    mydb.commit()
    print("Record deleted")

def search ():
    print("1. Book Code Search")
    print("2. Book Name Search")
    print("3. Author Name Search")
    print("4. Price Search")
    print("5. Total Stock Search")
    print("6. Availability Search\n")
    
    What = input("Select Category Number to search: ")
    
    if What == "1":
        BookCodeSearch()
    elif What == "2":
        BookNameSearch()
    elif What == "3":
        AuthorSearch()
    elif What == "4":
        PriceSearch()
    elif What == "5":
        StockSearch()
    elif What == "6":
        ASearch()
    else:
        print("invalid input")

def update ():

    newView()
    Code = int(input("\nEnter Book Code of record to be updated: "))
    print("1. Book Name")
    print("2. Author Name")
    #print("3. Price")
    print("3. Total Quantity")
    #print("5. Available Stock")

    What = str(input("Select Category to Update in record: "))
    
    if What == "Admin":

        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[0] = int(input("Enter New Book Code: "))
                print("Updated Entry: ", j )
                up = j[0]
                q2 = "update librarydb set Sno = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()

            
    elif What == "1":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[1] = input("Enter New Book Name: ")
                print("Updated Entry: ", j )
                up = str(j[1])
                q2 = "update librarydb set BookName = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()

    elif What == "2":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[2] = input("Enter New Author Name: ")
                print("Updated Entry: ", j )
                up = str(j[2])
                q2 = "update librarydb set AuthorName = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()

    elif What == "Admin1":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[3] = int(input("Enter New book Price: "))
                up = j[3]
                q2 = "update librarydb set Price = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()
                print("Updated Entry: ", j )

    elif What == "3":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                print("1. Add Books")
                print("2. Remove Books")
                ar = int(input("Enter operation: ")) 
                
                if ar == 1:
                    add =  int(input("Enter Number of books to add: "))
                    j[4] = j[4] + add
                    up = j[4] 
                    q2 = "update librarydb set TotalQty= %s where SNo = %s"
                    mycursor.execute(q2,(up,Code))
                    print("Updated Entry: ", j )
                    mydb.commit()
                elif ar == 2:
                    rem = int(input("Enter Number of books to remove: "))
                    j[4] = j[4] - rem
                    up = j[4] 
                    q2 = "update librarydb set TotalQty= %s where SNo = %s"
                    mycursor.execute(q2,(up,Code))
                    print("Updated Entry: ", j )
                    mydb.commit()
                else:
                    print("invalid input")
    elif What == "Admin2":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[5] = int(input("Enter Updated Availability of books: "))
                print("Updated Entry: ", j )
                up = j[5]
                q2 = "update librarydb set Available = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()
    else:
        print("invalid input")

    
    

def ctr():
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    ctr1 =0
    for i in data:
        ctr1 +=1
    print("Total number of records in database is ",ctr1)

def top():
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    print(data[-1])
    
def issue():
    ASearch()
    Code = int(input("\nEnter Book Code of book to be issued: "))
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        j = list(i)
        if j[0] == Code:
            print("Enter number of copies of ",j[1]," to be issued: ")
            amt = int(input())
            if amt <= j[5]:
                up = (int(j[5]) - amt)
                q2 = "update librarydb set Available= %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()
                print("Successfully issued ",amt," copies of ", j[1])
            else:
                print("Sorry only ", j[5], "copies of ", j[1], " are available")

def returnb():
    
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        j = list(i)
        print(j[0],j[1])
    Code = int(input("Enter Book Code of book to be returned: "))
    for i in leest:
        j = list(i)
        if j[0] == Code:
            amt0 = 1
            amt = int(amt0)
            up = (int(j[5]) + amt)
            q2 = "update librarydb set Available= %s where SNo = %s"
            mycursor.execute(q2,(up,Code))
            mydb.commit()
            print("Successfully returned", amt, "copy of ", j[1])

def help():
    print("Made by korax (GitHub: kor4x)")

#MAIN:
while 1 == 1:
    
    print("\nWelcome to LibStruct")
    print("Select operation to perform: \n")
    print(" 1.  View existing records")
    print(" 2.  Add a new book to record")
    print(" 3.  Delete an entry from record")
    print(" 4.  Filter books")
    print(" 5.  Update an existing record")
    print(" 6.  Display total number of records")
    print(" 7.  Display last entered record")
    print(" 8.  Display total stock of books")
    print(" 9.  Display availability of books")
    print(" 10. Issue a book")
    print(" 11. Return a book\n")
    print(" Enter 'Help' for help\n")

    choice = (input("Enter Option number: "))
    print("")

    if choice == "Help" or choice == "help":
        help()

    else:
        choice = int(choice)
        if choice <=11 and choice >=1 :

            if choice == 1:
                newView()
            elif choice == 2: 
                InsertVal()
                mydb.commit()
            elif choice == 3:
                delete()
            elif choice == 4:
                search()
            elif choice == 5:
                update()
            elif choice == 6:
                ctr()
            elif choice == 7:
                top()
            elif choice == 8:
                StockSearch()
            elif choice == 9:
                print("Available books are:")
                ASearch()
            elif choice == 10:
                issue()
            elif choice == 11:
                returnb()
            else:
                print("invalid input")

    input() 
   