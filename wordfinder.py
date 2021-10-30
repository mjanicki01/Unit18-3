"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    """
    A class used to iterate through words of a file
    
    Attributes
    --------------------
    a: path
        path of file to iterate through
    word_count: list
        list of each word in the file; each element is an individual word
    count: int
        number of words read through in the file
    """

    def __init__(self, a):
        self.a = a
        self.word_count = []
        for line in (open(self.a, "r")):
            line = line[:len(line)-1]
            self.word_count.append(line)
        self.count = len(self.word_count)       
        self.print_count()

    def print_count(self):
        """Upon instantiation, prints the number of words in file"""
        print(f"{self.count} words read")

    def random(self):
        """Prints a randomly selected word from the list of the file"""
        random_num = randint(0, self.count)
        print(self.word_count[random_num])




class SpecialWordFinder(WordFinder):
    """
    A subclass of WordFinder used to remove empty lines and lines that begin
    with chaaracter '#' from a file during instantiation

    Attributes
    --------------------
    a: path
        path of file to iterate through
    word_count: list
        list of each word in the file; each element is an individual word
        if a given line within the file is blank, do not append
        if a given line within the file begins with '#', do not append
    count: int
        number of valid words read through in the file
    
    """

    def __init__(self, a):
        super().__init__(a)
        self.word_count = []
        for line in (open(self.a, "r")):
            if '#' not in line and len(line) > 1:
                line = line[:len(line)-1]
                self.word_count.append(line)
        self.count = len(self.word_count)       
        self.print_count()
    

    # Further study: How to prevent self.print_count() in init of super() in subclass?
    