'''
This is a play field for classes and decorators
'''
#define a class called "Door"
class Door(object):
    #define a class variable
    name = "DOOR"
    #make the 'constructor' of instances
    def __init__(self):
        self.status = 'opened'
        self.colour = 'woody yellow'
        
    #define methods for opening, closing and painting the door
    def door_open(self):
        if self.status != 'opened':
            self.status = 'opened'

    def door_close(self):
        if self.status != 'closed':
            self.status = 'closed'

    def door_paint(self,colour):
        self.colour = colour

#define a decorator function to "door_paint" but for metallic doors
def paint_limited(func,self,colour):
    def wrapper_paint_limited(self,colour):
        print "Painted for " + str(self.no_paints) + " times"
        #print func
        if self.no_paints < 3:
            self.no_paints += 1
            func(colour)
        else:
            print "WARNING: Door can't be painted again"
    return wrapper_paint_limited

#define a class called "MetallicDoor" that inherits from "Door"
class MetallicDoor(Door):
    #define a class variable
    name = "Metallic Door" #overrides the original
    #make the 'constrictor' of instances
    def __init__(self):
        Door.__init__(self) #explicit initialization from another class "aka. composition or external delegation"
        self.lock = 'locked'
        self.no_paints = 0
    #define methods to lock and unlock the door
    def door_lock(self):
        if self.lock != 'locked':
            self.lock = 'locked'

    def door_unlock(self):
        if self.lock != 'unlocked':
            self.lock = 'unlocked'

    def door_paint(self,colour):
        hey_paint = paint_limited(Door.__dict__['door_paint'].__get__(self,colour),self,colour)
        return hey_paint(self,colour) #simply execute the decorated function
    '''
Before proceeding, we shall mention the following conclusions:-
Purpose of the previous decorator: to expand a method using a parent's one
1- The main decorator function [here in this example is "paint_limited"] shall accept three main arguments
{the method object, the instance object, rest of related arguments}
2- The method object is fetched with a somehow cryptic way, first of all you get the the method from its class
[Door.__dict__['door_paint'] => classname.__dict__[methodname_str]],
Python will see the result as "unbound method" and will throw an error if you try to execute it that way,
so you then need to apply the method-wrapper "__get__"on it
[__get__(self,colour) => __get__(self,[args])], this leads to the final wholistic syntax of the method object
[classname.__dict__[methodname_str].__get__(self,[args])]
3- when the object is supplied to a function, you can use its attributes and methods inside the body of that function.
    '''

#End of class definition. let's start defining our simple 'main' function
def main():
    ord_door = Door()
    met_door = MetallicDoor()
    print "Let's see the attributes of every instance"
    print "____________________"
    print "ord_door name is " + ord_door.name
    print "met_door name is " + met_door.name
    print "____________________"
    print "Are these doors opened?"
    print "ord_door is " + ord_door.status
    print "met_door is " + met_door.status
    print "*******"
    print "Close them all"
    print "*******"
    ord_door.door_close()
    met_door.door_close()
    print "ord_door is " + ord_door.status
    print "met_door is " + met_door.status
    print "____________________"
    print "Let's paint the metallic door with brown"
    met_door.door_paint('brown')
    print "met_door's colour is " + met_door.colour
    print "Let's paint it again with silver"
    met_door.door_paint('silver')
    print "met_door's colour is " + met_door.colour
    print "Let's paint it with dark chocolate"
    met_door.door_paint('dark chocolate')
    print "met_door's colour is " + met_door.colour
    print "Can we paint it again with black?"
    met_door.door_paint('black')
    if met_door.colour == 'black':
        print "met_door's colour is black"

#Run the code
if __name__ == '__main__': main()
