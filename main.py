# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.

# BOOK CLASS (PARENT)
class Book():
    def __init__(self, title, author, year, numpages):
        self.title = title
        self.author = author
        self.year = year
        self.numpages = numpages

    # Methods
    def displaydetails(self):
        print(f'Title:{title}')
        print(f'Author:{author}')
        print(f'Year of Publication:{year}')
        print(f'Number of Pages:{numpages}')


    def ratebook(self):
        rate = input('What will you rate this book? ★★★★★ (Enter 1-5 for rating)')
        if rate == 1:
            print(f'You have rated {title} 1 star! What a shame...')
        if rate == 2:
            print(f'You have rated {title} 2 stars! Not your cup of tea?')
        if rate == 3:
            print(f'You have rated {title} 3 stars! Cool beans.')
        if rate == 4:
            print(f'You have rated {title} 4 stars! Sounds like a good read!')
        if rate == 5:
            print(f'You have rated {title} 5 stars! Amazing!!')
        else:
            print("Sorry, that rating isn't valid. Please resubmit your rating")
            ratebook(self)

# NOVEL CLASS
class Novel(Book):
    def __init__(self, title, author, year, numpages, genre, numchapters):
            super().__init__(title, author, year, numpages)
            self.genre = genre
            self.numchapters = numchapters

    # Methods
    def calcreadtime(self):
        wpm = ('How many words per average can you read?')
        readtime = 275 / wpm * numpages

americanpsycho = Novel('American Psycho', 'Bret Easton Ellis', '1991', '400', 'Psychological Horror / Dark Comedy', '60')
nt84 = Novel('1894', 'George Orwell', '1949', '336', 'Science Fiction / Dystopian', '23')

# MAGAZINE CLASS
class Magazine(Book):
    def __init__(self, title, author, year, numpages, issuenum, numarticles):
        super().__init__(title, author, year, numpages)
        self.issurenum = issuenum
        self.numarticles = numarticles

    # Methods
#get article by title

# PROGRAM
def novellist():
    print('NOVELS:')
    print('  American Psycho')
    print('  1894')

def magazinelist():
    print('MAGAZINES:')
    print('eugh')

def main():  
    print('Welcome to the most underwhelming library to exist.')
    typereq = input('What type of books were you after? (Novel / Magazine) ').lower()

    if typereq == 'novel':
        print('What novel would you like to inquire about? ')
        novellist()
        novchoice = input('Enter: ')

        if novchoice == 'american psycho':
            print('What would you like to know about American Psycho?')
            print(' 1. Details')
            print(' 2. Reading Time')

            actionnov = input('Enter: ').lower()

            if actionnov == '1' or 'details':
                print(displaydetails.(americanpsycho))

main()

    