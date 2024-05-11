import sqlite3

def selectOperations():

    connection = sqlite3.connect("chinook.db")

    #cursor = connection.execute("""select city,count(*) from customers 
    #                           group by city having count(*) > 1 
    #                           order by city""") 

    #for row in cursor:
    #   print("City = "+row[0])
    #   print("Count = "+str(row[1]))
    #   print("*********")


    #cursor = connection.execute("""select FirstName,LastName 
    #                            from customers 
    #                           where city = 'Prague' or city = 'Berlin' 
    #                           order by FirstName,LastName desc""")  # asc artana göre sıralar desc azalana göre sıralar

    #for row in cursor:
    #   print("First Name = "+row[0])
    #   print("Last Name = "+row[1])
    #   print("*********")


    cursor = connection.execute("""select FirstName,LastName 
                                from customers 
                                where FirstName like '%a' """)

    for row in cursor:
        print("First Name = "+row[0])
        print("Last Name = "+row[1])
        print("*********")

    connection.close


#selectOperations()

def InsertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers 
                       (firstName,lastName,city,email) 
                       values('Murat','Asik','Ankara',
                       'muratasik7@gmail.com')""")

    connection.commit()
    connection.close()

#InsertCustomer()

def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city = 'İstanbul' 
                       where city = 'Ankara' """)


    connection.commit()
    connection.close()

#updateCustomer()

def deletecustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers 
                          where city = 'İstanbul'""")

    connection.commit()
    connection.close()

#deletecustomer()



def joinOperations():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select albums.Title, artists.Name from artists 
                                inner join albums
                                on artists.ArtistId = albums.ArtistId """)

    for row in cursor:
        print("Title = "+row[0]+" Name = "+row[1])

    connection.close

#joinOperations()