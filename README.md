## Session 11 - Iterators and Iterables

## Assignment

The starting point for this project is the Polygon class and the Polygons sequence type we created in the previous project.

The code for these classes along with the unit tests for the Polygon class are below if you want to use those as your starting point. 
But use whatever you came up with in the last project.

ONLY Goal
Refactor the Polygons (sequence) type, into an iterable. You'll need to implement both an iterable, and an iterator.

## Iterable

Iterables are objects in python that are capable of returning their elements one at a time.
Iterable is an object, which one can iterate over. Additionally, these objects have a double underscore (also called dunder) method 
called ‘__iter__()’, where the ‘__iter__()’ method returns an iterator. Thus it generates an Iterator when passed to iter() method and
hence an iterable can be looped over. Adding __iter__() method into any object's class definition makes it an iterable, which will help
to loop over it thus helping us to build our own iterables.The process of looping over something, or taking each item of it, one after 
another, is iteration.


## Iterator

Iterators are objects with states, where the state specifies the current value during iteration. Thus an iterator is an object with a state 
that remembers where it is during iteration. Iterators also have a dunder method called ‘__next__()’, which allows us to access subsequent values. 
Thus, Iterator is an object, which is used to iterate over an iterable object using __next__() method. An iterator can only go in the forward 
direction.

The notebook can be viewed at https://deepnote.com/project/Polygon-Sequence-Iterators-FVdm7XCBTziSrhOZCnx3xg/%2FPolygon_Iterator.ipynb

