import re 
import pandas
from argparse import ArgumentParser
import sys


class baseFunctions: 
    """The base/parent functions for a script that would simulate a grocery store experience for a user."""
    
    def __init__(self, fileCSV, path2TextFile):
        self.itemsWithPricesDict = {} 
    
    def __del__(self):
        """Holds space for its child function that cleans up the sqlite3 database connection."""
        pass
    
    def groceryItemsDict(self, path2TextFile):
        """  Takes a a path to a file containing one item and its price per line, opens the file, adds each line to a dictionary as
        a key,value pair. In its child function, it uses re.split instead of just the split function. 
            
        Args:
            path2TextFile (str): the path to a file (containing one address per line)

        Returns:
            dict: creates a dictionary of items in available for the user to buy with their corresponding prices 
        """
        with open(path2TextFile) as my_text_file:
            print(my_text_file.read())
        for line in my_text_file:
            myList= line.split()
            self.itemsWithPricesDict[myList[0]]= myList[1]
            
        return self.itemsWithPricesDict
    
        
    def makeTablefromCSV(self, fileCSV):
        """The simplest part of a function that would make a table of items and prices from a CSV with those as column headers. 
        Here, it uses pandas to read the file and prints the file as a string. In its child function, I override this function and
        use f = open(fileCSV, "r") to read the function and make a table. 
        
        Args:
        fileCSV (str): the path to the csv file (of items for sale at the grocery store) to be read in   
        """
        df = pandas.read_csv(fileCSV)
        print(df.read())
        
    
    def printItemsAndPrices(self):
        """Prints the name of each item and its corresponding price as a tuple. In the child function that overrides this function, it
        prints a fstring it prints the name and price as of each item as f"{key}: ${value}") (a response which is easier for the
        user to interpret).
        """
        for key, value in self.itemsWithPricesDict.items(): 
            print(tuple(key,value))  
            
    def TodaysCheapestItem(self):
        """Holds space for its child function that prints the cheapest item for sale at the grocery store today for the user."""
        pass
    
    def TodaysMostExpensiveItem(self):
        """Holds space for its child function that prints the most expensive item for sale at the grocery store today for the user.
        """
        pass
    
    def printItemsSortedCheapestDesc(self):
        """Holds space for its child function that creates and prints a dictionary sorted in descending order, with the
        cheapest value (and corresponding item) first and the most expensive item (with its price) last.
        """
        pass
    
    def checkoutDesk(self):
        """The simplest part of a function that would simulates the process you go through at checkout desk of a typical store.
        Here, it appends all items for sale to a list so that the list of items that the user would select (input) can be compared
        to it. This way, we would make sure the items the user selected are in the list of items for sale and can add their prices
        to the total price which the user would pay. 
        """
        groceryStoreItemsList = []
        for key, value in self.itemsWithPricesDict.items():
            groceryStoreItemsList.append(key)
            
    def __repr__(self):
        """Returns a string that can be used to recreate the current instance of the Book class (the Book class can be seen above).
        
        Returns:
        str: a string that can be used to recreate the current instance of the Book class. The information about the specific book is
        formatted in the following order: the call number of the book, the title of the book, and lastly the author of the book. 
        
        """
        return f"baseFunctions({repr(self.itemsWithPricesDict.key(), self.ritemsWithPricesDict.values())})"
            
            
def main(fileCSV, path2TextFile):
    """ Calls and runs my baseFunctions class.
    
    Args: 
    fileCSV (str): path to a CSV file containing two columns:
            itemName & Year
    path2TextFile (str): path to a text file with one item for sale at the grocery store and price per line
    
    """
    
    g = baseFunctions(fileCSV, path2TextFile)
    
    
    
def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("CSVfile")
    parser.add_argument("textFile")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.CSVfile, args.textFile)
