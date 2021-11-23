class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

class Library:
    books = []
    def addBook(self, book):
        self.books.append(book)
    
    def removeBook(self, book):
        self.books.remove(book)

    def searchByAuthor(self, author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        return books
    
    def searchByYear(self, year):
        books = []
        for book in self.books:
            if book.year == year:
                books.append(book)
        return books

    def searchByGenre(self, genre):
        books = []
        for book in self.books:
            if book.genre == genre:
                books.append(book)
        return books
library = Library()
library.addBook(Book('Ольга Громико', 'Космобіолухи', '2011', 'Роман'))
library.addBook(Book('Ольга Громико', 'Професія Відьма', '2003', 'Роман'))
library.addBook(Book('Farnar', 'Ублюдок FFF-рангу', '2018', 'Роман'))
library.addBook(Book('Марія Вересень', 'Особливо Обдарована Особа', '2007', 'Роман'))
library.addBook(Book('Маруяма Куґане', 'Overlord', '2010', 'Роман'))
library.addBook(Book('UROBBYU', 'Балада про демона техно-мага', '2022', 'Роман'))

author = 'Ольга Громико'
books = library.searchByAuthor (author)
if len(books) != 0:
    book = books[0]

    print('Кількість книг автора '+ author, len(books))
    print('Автор книги ', author)
    print('Титульна сторінка книги ' , book.title)

    library.removeBook(book)
    books = library.searchByAuthor(author)
    print('Нова кількість книг автора ' + author, len(books))