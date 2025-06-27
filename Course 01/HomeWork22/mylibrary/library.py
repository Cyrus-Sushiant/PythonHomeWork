class Library():
    books = []

    def add_book(self, title, author):
        self.books.append((title, author))

    def remove_book(self, title):
        self.books = [b for b in self.books if b[0] != title]

    def search_book(self, title):
        return [b for b in self.books if b[0].startswith(title) or b[0] == title]
    
    def show_books(self):
        return self.books