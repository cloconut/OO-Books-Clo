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

    def displaydetails

    def ratebook

    def reviewbook

class Novel(Book):
    def __init__(self, genre, numchapters):

    def calcreadtime

class Magazine(Book):
    def __init__(self, issuenum, numarticles)
        self.issurenum = issuenum
        self.numarticles = numarticles

    def getarticlebytitle