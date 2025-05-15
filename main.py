# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.

class Book():
    def __init__(self, title, author, year, numpages)
        self.title = title
        self.author = author
        self.year = year
        self.numpages = numpages

    def displaydetails(self):
        print(f'Title:{title}')
        print(f'Author:{author}')
        print(f'Year of Publication:{year}')
        print(f'Number of Pages:{numpages}')


    def ratebook(self):

    def reviewbook(self):

    book1 = Book('American Psycho', ''):

class Novel(Book):
    def __init__(self, title, author, year, numpages, genre, numchapters):
            super().__init__(title, author, year, numpages)
            self.genre = genre
            self.numchapters = numchapters

    def calcreadtime(self):

class Magazine(Book):
    def __init__(self, title, author, year, numpages, issuenum, numarticles)
        super().__init__(title, author, year, numpages)
        self.issurenum = issuenum
        self.numarticles = numarticles

    def getarticlebytitle(self):