# Name: Irving F Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Define the Movie class to represent movie data.


''' /*---+---+---+--Start of Movie Class Block---+---+---+--*/ '''

class MovingPicture:
    
    ''' Here this class will represent a movie with title, year, genere and rating '''
    
    def __init__(self, title, year, genre, rating):
        
        '''Here I'd like to specify the attributes of the movie'''
        
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating
        
    def __str__(self):
        
        '''Here i'd like to format a string representing the movie'''
        
        return f"{self.title} ({self.year}) - {self.genre} - Rating: {self.rating}"
    
''' /*---+---+---+--End of Movie Class Block---+---+---+--*/ '''
