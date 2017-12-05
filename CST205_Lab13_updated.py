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

Good job %(player)s!.  Here is the story you created...

Archaeologists recently unearthed a curious %(object)s in %(place)s
Unlike the Great %(object)s of %(city)s, which was made of %(material)s, this %(object)s was made from plastic.  And it wasn't carved by the ancient %(place)s, but molded by designers on the set of %(movie)s.  The film featured thousands of actors and actresses, and the director commissioned famed artby designer %(name)s to construct an ancient %(place)s palace for the film's backdrop. %(name)ss final product was the largest set design of its time and included more than 20 %(object)s.  After filming was complete, the 12 story set was too expensive to dismantle and too valuable to leave for rival film studios to pilfer. In a move just as ambitious as his filmmaking, %(name)s, who created a  second version of the film in 1956, ordered the set buried at a location unknown to the public.

Press Stop to finish game.
"""

showInformation("Welcome to MadLibs.\nMadlibs is a word game that prompts you, the player, for a list of words to substitute blank spaces in a story. In this game we're using a news article from NPR.")

def madLib():                                 
    userInput = dict()
    addInput('player', userInput)
    addInput('object', userInput)
    addInput('place', userInput)
    addInput('city', userInput)
    addInput('material', userInput)      
    addInput('movie', userInput)           
    addInput('name', userInput)
               
    showInformation(story % userInput)                         
                                                    
def addInput(key, dictionary):
    if key == 'player':
      promptString = "To start, please enter your name."
    else:
      promptString = "Enter one word for %s: " % key     
    dictionary[key] = requestString(promptString)   
                                                                                                                         
madLib()                                     

