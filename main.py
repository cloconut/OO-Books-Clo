# BOOK CLASS (PARENT)
class Book():
    def __init__(self, title, author, year, numpages):
        self.title = title
        self.author = author
        self.year = year
        self.numpages = numpages

  # Methods
    def displaydetails(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Year of Publication: {self.year}')
        print(f'Number of Pages: {self.numpages}')

    def ratebook(self):
        rate = input('What will you rate this book? ★★★★★ (Enter 1-5 for rating) ')
        if rate == '1':
            print(f'You have rated {self.title} 1 star! What a shame...')
        if rate == '2':
            print(f'You have rated {self.title} 2 stars! Not your cup of tea?')
        if rate == '3':
            print(f'You have rated {self.title} 3 stars! Cool beans.')
        if rate == '4':
            print(f'You have rated {self.title} 4 stars! Sounds like a good read!')
        if rate == '5':
            print(f'You have rated {self.title} 5 stars! Amazing!!')
        else:
            print("Sorry, that rating isn't valid. Please resubmit your rating")
            Book.ratebook(self)

# - - - - - - - - - - - - - - #

# NOVEL CLASS
class Novel(Book):
    def __init__(self, title, author, year, numpages, genre, numchapters):
            super().__init__(title, author, year, numpages)
            self.genre = genre
            self.numchapters = numchapters

  # Methods
    def calcreadtime(self):
        wpm = int(input('How many words per minute can you read? '))
        averagewords = int(self.numpages) * 275  # Assuming 275 words per page
        readtime = averagewords / wpm
        print(f"Estimated reading time: {readtime:.2f} minutes")

americanpsycho = Novel('American Psycho', 'Bret Easton Ellis', '1991', '400', 'Psychological Horror / Dark Comedy', '60')
nt84 = Novel('1894', 'George Orwell', '1949', '336', 'Science Fiction / Dystopian', '23')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# MAGAZINE CLASS
class Magazine(Book):
    def __init__(self, title, author, year, numpages, issuenum, numarticles):
        super().__init__(title, author, year, numpages)
        self.issurenum = issuenum
        self.numarticles = numarticles

  # Methods
#get article by title

# - - - - - - - - - - - #

# PROGRAM
def novellist():
    print('NOVELS:')
    print(' - American Psycho')
    print(' - 1984')

def magazinelist():
    print('MAGAZINES:')
    print('eugh')

print('Welcome to the most underwhelming library to exist.')

def main():  
    typereq = input('What type of books were you after? (Novel / Magazine) ').lower()

# Novels
    if typereq == 'novel':
        print('What novel would you like to inquire about? ')
        novellist()
        novchoice = input('Enter: ')

  # American Psycho
    if novchoice == 'american psycho':
        print('What would you like to know about American Psycho?')
        print(' 1. Details')
        print(' 2. Reading Time')
        actionnov = input('Enter: ').lower()

        if actionnov == '1' or actionnov == 'details':
            americanpsycho.displaydetails()
        if actionnov == '2' or actionnov == 'reading time':
            americanpsycho.calcreadtime()
        
        willrate = input('Would you like to rate this novel? (yes/no) ').lower()
        if willrate == 'yes':
            americanspycho.ratebook()
        if willrate == 'no':
            print('Okay!')
            main()       

  # 1984
    if novchoice == '1984':
        print('What would you like to know about 1984?')
        print(' 1. Details')
        print(' 2. Reading Time')
        actionnov = input('Enter: ').lower()

        if actionnov == '1' or actionnov == 'details':
            nt84.displaydetails()
        if actionnov == '2' or actionnov == 'reading time':
            nt84.calcreadtime()

        willrate = input('Would you like to rate this novel? (yes/no) ').lower()
        
        if willrate == 'yes':
            nt84.ratebook()
        if willrate == 'no':
            print('Okay!')
            main()

main()

    