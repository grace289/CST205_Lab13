#!/usr/bin/python

# CST205 Lab 13
# November 29, 2017
#
# Team 5, Hopper
# Grace Alvarez
# Christian Guerrero

#Mad Lib program    
                                                                                          
story = """    
Archaeologists recently unearthed a curious %(item)s in %(place)s ." 
A %(place)s %(item)s. 
Unlike the Great %(item)s of %(place2)s, which was made of %(material)s, this %(item)s was made from plastic.  
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
    addInput('place2', userInput)
    addInput('material', userInput)      
    addInput('movie', userInput)           
    addInput('name', userInput)           
    printNow(story % userInput)                         
                                                    
def addInput(key, dictionary):
    prompt = "Enter one word for %s: " % key     
    dictionary[key] = raw_input(prompt)                                                             

madLib()                                         
raw_input("To end the program please press enter.")   
