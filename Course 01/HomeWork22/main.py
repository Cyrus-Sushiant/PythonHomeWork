from mylibrary.library import Library

lib = Library()
lib.add_book("The Lord of the Rings", "J. R. R. Tolkien")
lib.add_book("The Hobbit", "J. R. R. Tolkien")
lib.add_book("The Silmarillion", "J. R. R. Tolkien")

if __name__ == "__main__":
    print("1. Show all books")
    print("2. Search book")
    print("3. Add new book")
    print("4. Remove book")
    menu = input("Enter number of menu:")

    if menu == "1":
        print("Show books: ", lib.show_books())
    elif menu == "2":
        title = input("Enter title:")
        print("Search book: ", lib.search_book(title))
    elif menu == "3":
        title = input("Enter title:")
        author = input("Enter author:")
        lib.add_book(title, author)
        print("Show books: ", lib.show_books())
    elif menu == "4":
        title = input("Enter title:")
        lib.remove_book(title)
        print("Show books: ", lib.show_books())
