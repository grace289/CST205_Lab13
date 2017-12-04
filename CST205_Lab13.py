#!/usr/bin/python

# CST205 Lab 13
# November 29, 2017
#
# Team 5, Hopper
# Grace Alvarez
# Christian Guerrero

#Mad Lib program    


"""

Add Strings

At the beginning of your game, ask the user to enter their name (or to name their character). Use the user's name at least one other place in your program (maybe when they win or lose!).

Add Lists

Now that we've explored lists, you can probably think of multiple ways to use them in your adventure game.  In particular, lists should really help you cut down on the number of global variables you need since you can have a single list for inventory or to hold other important information.  Go back through your adventure game and think about whether there is an opportunity to use lists to simplify your code.  
"""
                                                                                          
story = """    
Archaeologists recently unearthed a curious %(item)s in %(place)s ." 
A %(place)s %(item)s. 
Unlike the Great %(item)s of %(city)s, which was made of %(material)s, this %(item)s was made from plastic.  
And it wasn't carved by the ancient %(place)s, but molded by designers on the set of %(movie)s.  
The film featured thousands of actors and actresses, and the director commissioned famed art
by designer %(name)s to construct an ancient %(place)s palace for the film's backdrop. %(name)ss final product  
was the largest set design of its time and included more than 20 %(item)ss.  
After filming was complete, the 12 story set was too expensive to dismantle and too valuable to leave
for rival film studios to pilfer. In a move just as ambitious as his filmmaking, %(name)s, who created a  
second version of the film in 1956, ordered the set buried at a location unknown to the public. 

"""                                                 

def madLib():                                     
    userInput = dict()
    addInput('item', userInput)
    addInput('place', userInput)
    addInput('city', userInput)
    addInput('material', userInput)      
    addInput('movie', userInput)           
    addInput('name', userInput)           
    printNow(story % userInput)                         
                                                    
def addInput(key, dictionary):
    promptString = "Enter one word for %s: " % key     
    dictionary[key] = requestString(promptString)   
                                                                                                                         

showInformation("Welcome to MadLib. Madlibs is a word game that prompts you, the player, for a list of words to substitute blank spaces in a story. In this game we're using a news article from NPR.")
userName = requestString("What is your name")
madLib()
printNow(userName + " you've created a new story!")                                         
requestString("To end the program please press enter.")   
