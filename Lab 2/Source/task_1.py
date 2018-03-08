dictionary_books = {"Python":80,"AngularJs":30,"C#":20,"MEAN Stack":10, "Oracle": 100}
min = int(input("Minimum price range: "))
max = int(input("Maximum price range: "))
list_books = []
for price in range(min,max+1):
    for bookname in dictionary_books:
        if dictionary_books[bookname] == price:
            list_books.append(bookname)
print("You can purchase books" , list_books)