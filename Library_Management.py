class Library:

    instances = []
    lend_book = {}
    def __init__(self, listbooks, lib_name):
        self.list_of_books = listbooks
        self.library_name = lib_name
        self.__class__.instances.append(self)

    @classmethod
    def printInstances(cls):
        for instance in cls.instances:
            print(instance.library_name)

    @classmethod
    def display(cls, str):
        for instance in cls.instances:
            if str.title() == instance.library_name.title():
                print(f"List of books available {instance.list_of_books}")
                library_name = "Valid"
                return library_name
            else:
                library_name = "Invalid"
        return  library_name

    @classmethod
    def add(cls, lst, str):
        for instance in cls.instances:
            if str.title() == instance.library_name.title():
                for i in range(n):
                    ele = input("Enter the name of the book")
                    instance.list_of_books.append(ele)
                library_name = "Valid"
                return library_name
            else:
                library_name = "Invalid"
        return library_name


    @classmethod
    def lend(cls, library_name):
        inp = input("Enter the book which you want to lend")
        inp = inp.title()
        for instance in cls.instances:
            if library_name.title() == instance.library_name.title():
                if inp in instance.list_of_books:
                    lender_name = input("Enter you name")
                    lender_name = lender_name.title()
                    
                    if lender_name in cls.lend_book.keys():
                        lst = cls.lend_book[lender_name]
                        dic = {instance.library_name:inp}
                        lst.append(dic)
                        cls.lend_book[lender_name] = lst
                    else:
                        lst = []
                        lst1 = {instance.library_name:inp}
                        lst.append(lst1)
                        cls.lend_book[lender_name] = lst
                    instance.list_of_books.remove(inp)
                else:
                    print("Invalid Entry")

    @classmethod
    def returrn (cls, name):
        lst = cls.lend_book[name]
        library = []
        book_name = []
        for i in lst:
            for key, value in i.items():
                library.append(key)
                book_name.append(value)
                
        print("You lent following books\n", book_name)
        inp = input("Which book you want to return")
        if inp in book_name:
            index = book_name.index(inp)
            library_name = library[index]
            Library.add(list(inp), library_name)
            temp = "Valid"
        else:
            temp = "Invalid"
        return temp
        

while True:
    inp = input("Enter your input\n1.create\n2.Display\n3.Add\n4.Lend\n5.Return\n6.List of lenders")
    inp = inp.title()

    #Condition to create a Library
    if inp == "1" or inp == "Create":
        name = input("Enter the name of the library")
        name = name.title()
        # number of books
        n = int(input("Enter number of books : "))
        list_of_books = []
        for i in range(0, n):
            ele = input("Enter the Book")
            ele = ele.title()
            list_of_books.append(ele)  # adding the element

        name = Library(list_of_books, name)


    #Condition to Display a library
    elif inp == "2" or inp == "Display":
        print("\nList of Libraries Available")
        Library.printInstances()
        a = input("Do you want to look the books available in a particular library (y/n) ?")
        if a.upper() == "Y":
            a = input("Enter name of Library")
            temp = Library.display(a)
            if temp == "Invalid":
                print("Invalid Input")
#        del a, temp


    #condition ot add books to a particular library
    elif inp == "3" or inp == "Add":
        print("\nList of Libraries Available")
        Library.printInstances()
        library_name = input( "Enter the name of the library to which you want to add the book")
        n = int(input("Enter number of books you want to add: "))
        temp = Library.add(n, library_name)
        if temp == "Invalid":
            print("Invalid Input")
#        del temp


    #condition to lend a book
    elif inp == "4" or inp == "Lend":
        print("\nList of Libraries Available")
        Library.printInstances()
        library_name = input("Enter the name of the library to which you want to lend the book")
        library_name = library_name.title()
        temp = Library.display(library_name)
        if temp == "Invalid":
            print("Invalid Input")
        else:
            Library.lend(library_name)
#        del temp

    #Condition to return a book
    elif inp == "5" or inp == "Return":
        name = input("Enter Your Name")
        name = name.title()
        if name in Library.lend_book.keys():
            temp = Library.returrn(name)
            if temp == "Invalid":
                print("Invalid Entry")
        else:
            print("You havn't lent any book. You can add the book" )

    print(Library.lend_book)