book = {}
while True:

    book_listing = "1"
    book_add= "2"
    book_delete = "3"
    exit = "X"        


    def book_information():
        for book_key in book.keys():
            name = book[book_key]["book_name"]
            yayınevi = book[book_key]["book_yayınevi"]
            yazar = book[book_key]["book_yazar"]
            print(book_key, "= kitabın ismi: ", name, " yayınevi: ", yayınevi, " : ", yazar)
            

    def add_book():
        name = input("kitabın ismini  girin\n")
        yayınevi = input("kitabın yayınevini  girin\n")
        yazar = input("kitabın yazarını girin\n")
        key = len(book.items()) + 1
        book[key] = {"book_name": name, "book_yayınevi": yayınevi, "book_year": yazar}


    def delete_book():
        book_key = input("Kaçıncı sıradaki kitabı silmek istiyorsunuz\nListelemeden sırayı görebilirsiniz .")
        book.pop(book_key)


    if book_listing == "1":
        book_information()
    elif book_add == "2":
        add_book()
    elif book_delete == "3":
        delete_book()
    elif exit == "x":
        print("çıkış yapılıyor")
        break