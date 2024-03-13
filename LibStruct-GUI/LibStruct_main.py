#LibStruct-GUI

print("Connecting Server...")
import mysql.connector
import sys
import pygame
from pygame.locals import *
mydb = mysql.connector.connect(
     host ="localhost", 
     user ="########", 
     password ="########", 
     database = "Library")
print("Connection Succeeded")
mycursor = mydb.cursor()
pygame.init()

# Display Values:
FPS = 60
WIDTH, HEIGHT = 800,600 #Base resolution, you need not edit this, use SCALER values below

#-----SCALE VALUES-----#
## You can experiment as needed, tested values are given below ##
SCALE = 1.0 #Set to 1 for 800 x 600, 1.7 for 1920 x1080
SCALEW,SCALEH = 1,1 #Set to 1,1 for 800 x 600, 2.4,1.7 for 1920 x 1080
##----------------------------------------------------------------------##

screen = pygame.display.set_mode((WIDTH*SCALEW, HEIGHT*SCALEH), pygame.SCALED)
pygame.display.set_caption('LibStruct - GUI')

#Elements:
sprites ={}
Hfont = pygame.font.SysFont("Montserrat SemiBold", int(65*SCALE))
Bfont = pygame.font.SysFont("Montserrat", int(25*SCALE))
SFont = pygame.font.SysFont("Cutive Mono Regular",int(15*SCALE))
text_clr = (255, 255, 255)
bg = 'bg.jpg'

#Classes:
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		surface.blit(self.image, (self.rect.x, self.rect.y))
		return action

    
#FUNCTIONS:
global data
global ctr
global state

#PYGAME:
def dtext(text, font, text_col,x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

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
    sql = "select Sno, BookName from librarydb"
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
            amt = 1
            up = (int(j[5]) + amt)
            q2 = "update librarydb set Available= %s where SNo = %s"
            mycursor.execute(q2,(up,Code))
            mydb.commit()
            print("Successfully returned 1 copy of ", j[1])

def help():
    print("Made by _korax_ (Github: koraxial)")
    

#ButtonIMGs:
one = pygame.image.load("Buttons/1.png").convert_alpha()
two = pygame.image.load("Buttons/2.png").convert_alpha()
three = pygame.image.load("Buttons/3.png").convert_alpha()
four = pygame.image.load("Buttons/4.png").convert_alpha()
five = pygame.image.load("Buttons/5.png").convert_alpha()
six = pygame.image.load("Buttons/6.png").convert_alpha()
seven = pygame.image.load("Buttons/7.png").convert_alpha()
eight = pygame.image.load("Buttons/8.png").convert_alpha()
nine = pygame.image.load("Buttons/9.png").convert_alpha()
ten = pygame.image.load("Buttons/10.png").convert_alpha()
eleven = pygame.image.load("Buttons/11.png").convert_alpha()
twelve = pygame.image.load("Buttons/12.png").convert_alpha()

#BUTTONS:
bone = Button(110*SCALEW, 150*SCALEH, one, SCALE*0.115)
btwo = Button(110*SCALEW, 300*SCALEH, two, SCALE*0.115)
bthree = Button(110*SCALEW, 450*SCALEH, three, SCALE*0.115)
bfour = Button(260*SCALEW, 150*SCALEH, four, SCALE*0.115)
bfive = Button(260*SCALEW, 300*SCALEH, five, SCALE*0.115)
bsix = Button(260*SCALEW, 450*SCALEH, six, SCALE*0.115)
bseven = Button(410*SCALEW, 150*SCALEH, seven, SCALE*0.115)
beight = Button(410*SCALEW,300*SCALEH, eight, SCALE*0.115)
bnine = Button(410*SCALEW, 450*SCALEH, nine, SCALE*0.115)
bten = Button(560*SCALEW, 150*SCALEH, ten, SCALE*0.115)
beleven = Button(560*SCALEW, 300*SCALEH, eleven, SCALE*0.115)
btwelve = Button(560*SCALEW, 450*SCALEH, twelve, SCALE*0.115)

#Pygame Button Functions:
def pyView():
    dtext("This Feature is still under developement ;)", Bfont,text_clr, 15,125)

#PYMAIN:
run = True
while run:

    #persistent values:
    sprites['bg'] = (pygame.image.load(bg).convert())
    bgd = pygame.transform.scale_by(sprites['bg'], (SCALEW, SCALEH))
    screen.blit(bgd, (0, 0))
    dtext("LibStruct", Hfont,text_clr, 250*SCALEW,15*SCALEH)
    state = 0

    #conditional values:
    if state == 0:
        dtext("Select operation to perform:", Bfont,text_clr, 15*SCALEW,125*SCALEH)
        dtext("LibStruct-GUI v1.1.0 by _korax_", Bfont,text_clr, 250*SCALEW,570*SCALEH)
        if bone.draw(screen):
            newView()
            state = 1
        if btwo.draw(screen):
            InsertVal()
            state = 2
        if bthree.draw(screen):
            delete()
            state = 3
        if bfour.draw(screen):
            search()
            state = 4
        if bfive.draw(screen):
            update()
            state = 5
        if bsix.draw(screen):
            ctr()
            state = 6
        if bseven.draw(screen):
            top()
            state = 7
        if beight.draw(screen):
            StockSearch()
            state = 8
        if bnine.draw(screen):
            ASearch()
            state = 9
        if bten.draw(screen):
            issue()
            state = 10
        if beleven.draw(screen):
            returnb()
            state = 11
        if btwelve.draw(screen):
            help()
            state = 12

    pygame.display.update()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
