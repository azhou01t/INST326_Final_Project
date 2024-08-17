import re
import sqlite3
from argparse import ArgumentParser
import sys

class groceries(baseFunctions):
    """Simulates a grocery store experience for a user."""
    
    def __init__(self, fileCSV, path2TextFile):
        super().__init__(self, fileCSV, path2TextFile)
        
        self.itemsAndPricesDict = {}
        
        self.conn = sqlite3.connect(':memory:')
        self.conn
        
        self.makeTablefromCSV(fileCSV)
        
        self.groceryItemsDict(path2TextFile)
        
        print("Welcome to the Grocery Store!")
        print("Here are the following items available today:")
        self.printItemsAndPrices(self)
        
        self.wantToKnowCheapestItem = input('Would you like to know the least expensive item today? Please enter "Yes" or "No"') 
        if self.wantToKnowCheapestItem == "yes" or "Yes" or "YES": 
            self.TodaysCheapestItem(self)
        while self.wantToKnowCheapestItem != "no" or "No" or "NO" or "Yes" or "yes" or "YES":
            print('Please enter "Yes" or "No" ')
            self.wantToKnowCheapestItem = input('Would you like to know the least expensive item today? Please enter "Yes" or "No"')
            if self.wantToKnowCheapestItem == "yes" or "Yes" or "YES": 
                self.TodaysCheapestItem(self)
        
        self.wantToKnowMostExpensiveItem = input('Would you like to know the most expensive item today? Please enter "Yes" or "No"') 
        if self.wantToKnowMostExpensiveItem == "yes" or "Yes" or "YES": 
            self.TodaysMostExpensiveItem(self)
        while self.wantToKnowMostExpensiveItem != "no" or "No" or "NO" or "Yes" or "yes" or "YES":
            print('Please enter "Yes" or "No" ')
            self.wantToKnowMostExpensiveItem = input('Would you like to know the least expensive item today? Please enter "Yes" or "No"')
            if self.wantToKnowMostExpensiveItem == "yes" or "Yes" or "YES": 
                self.TodaysMostExpensiveItem(self)    
            
        self.wantCheapestToHighest= input('Would you like to see the items sorted cheapest to most expensive? Please enter "Yes" or "No"')
        if self.wantCheapestToHighest == "Yes" or "Yes": 
            self.printItemsSortedCheapestDesc(self)
        while self.wantCheapestToHighest != "no" or "No" or "NO" or "Yes" or "yes" or "YES":
            print('Please enter "Yes" or "No" ')
            self.wantCheapestToHighest = input('Would you like to see the items sorted cheapest to most expensive? Please enter "Yes" or "No"')
            if self.wantCheapestToHighest == "yes" or "Yes" or "YES": 
                self.printItemsSortedCheapestDesc(self)
    
        self.UsersShoppingList = input("Please enter the names of the items you would like to buy today:").split()
        
        
        self.totalPrice = 0.00 #base amount the customer will pay (if they don't buy any items the price is $0.00)
        self.checkoutDesk(self)
        

    def __del__(self):
        """ Clean up the database connection. """
        super().__del__(self)
        try:
            self.conn.close()
        except:
            pass
    
    
    def groceryItemsDict(self, path2TextFile):
        """  Takes a a path to a file containing one item and its price per line, opens the file, adds each line to a dictionary as
        a key,value pair  and returns a dictionary.
            
        Args:
            path2TextFile (str): the path to a file (containing one address per line)

        Returns:
            dict: creates a dictionary of items in available for the user to buy with their corresponding prices 
        """
        super().groceryItemsDict(self, path2TextFile)
        
        with open(path2TextFile) as my_text_file:
            print(my_text_file.read())
            
        for line in my_text_file:
            myTuple= tuple(re.split("\s", line))
            for x, y in myTuple:
                    self.itemsAndPricesDict[x]= y
                    
        return self.itemsAndPricesDict
                    
                    
    def makeTablefromCSV(self, fileCSV):
        """ Reads a file from a path to the file, creates the table named "groceries", and inserts values from the csv to the table.
        Args:
        fileCSV (str): the path to the csv file (of items for sale at the grocery store) to be read in   
        """
            
        super().makeTablefromCSV(self, fileCSV)
        cursor = self.conn.cursor()
        cq = '''CREATE TABLE groceries
            (itemName text, price integer)'''
            
        cursor.execute(cq)
        
        f = open(fileCSV, "r")
        f.readline()
        for line in f:
            print(line)
            
        imq = '''INSERT INTO groceries VALUES (?,?)'''
            
        cursor.executemany(imq, f)
        
        self.conn.commit()     
                    
                    
    def printItemsAndPrices(self):
        """Prints the name of each item and price for the user.""" 
        super().printItemsAndPrices(self)
        for key, value in self.itemsAndPricesDict: 
            print(f"{key}: ${value}")  
            
    def TodaysCheapestItem(self):
        """Prints the cheapest item for sale at the grocery store today for the user."""
        super().TodaysCheapestItem(self)
        todaysCheapestPrice = min(self.itemsAndPricesDict.values())
        for key,val in self.itemsAndPricesDict.items():
            if todaysCheapestPrice == val: 
                todaysCheapestItem = f"Today's least expensive item is {key}, which costs {val}"
                print(todaysCheapestItem)

        
    def TodaysMostExpensiveItem(self):
        """Prints the most expensive item for sale at the grocery store today for the user."""
        super().TodaysMostExpensiveItem(self)
        todaysMostExpensivePrice = max(self.itemsAndPricesDict.values())
        for key,val in self.itemsAndPricesDict.items():
            if todaysMostExpensivePrice == val: 
                todaysMostExpensiveItem = f"Today's most expensive item is {key}, which costs {val}"
                print(todaysMostExpensiveItem)
            
    def printItemsSortedCheapestDesc(self):
        """Creates and prints a dictionary sorted in descending order, with the cheapest value (and corresponding item) first and the
        most expensive item (with its price) last."""
        super().printItemsSortedCheapestDesc(self)
        
        itemsandValsSortedCheapest= {k: v for k, v in sorted(self.itemsAndPricesDict.items(), key=lambda item: item[1])}
        print(itemsandValsSortedCheapest)
             
                    
    def checkoutDesk(self):
        """Simulates the process you go through at checkout desk of a typical store. If the item the user brings/sends to this is in
        the (list of) available items for sale today, this function (finds from the dictionary of items and prices) and adds the
        price of the item to the total price that the customer would have to pay. 
        """
        super().checkoutDesk(self)
        
        groceryStoreItemsList = []
        for item, price in self.itemsAndPricesDict.items():
            groceryStoreItemsList.append(item)
        
        itemsBoughtAndPrices = {}   
        for itemUsersBuying in self.UsersShoppingList:
            if itemUsersBuying in groceryStoreItemsList:
                self.totalPrice += float(self.itemsAndPricesDict[itemUsersBuying])
                itemsBoughtAndPrices[itemUsersBuying]= float(self.itemsAndPricesDict[itemUsersBuying])
            elif itemUsersBuying not in groceryStoreItemsList:
                print(f"Sorry, {itemUsersBuying} is not for sale at this grocery store today.")
                
        #Printing like a reciept        
        print("Reciept")        
        for key, value in itemsBoughtAndPrices.items():
            print(f"{key}                       ${value}")
            #I added all the tabs to match the format of a reciept in the line of code above 
        print(self.totalPrice) 
                
           

def main(fileCSV, path2TextFile):
    """ Calls and runs my baseFunctions class
    
    Args: 
    fileCSV (str): path to a CSV file containing two columns:
            itemName & Year
    path2TextFile (str): path to a text file with one item for sale at the grocery store and price per line
    """
    g = groceries(fileCSV, path2TextFile)
    


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("CSVfile", help="path to  CSV file")
    parser.add_argument("TextFile", help="path to  text file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.CSVfile, args.TextFile)
