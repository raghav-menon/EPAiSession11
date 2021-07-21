# Polygon.py
import math

class Polygon :   
    """Implementation of a regular Polygon which takes num_eges and \
        circumradius as input. It can give num_eges, num_vertices,interior \
            angle,edge length,apothem,area,perimeter \
            """
    def __init__(self, num_edges : int = 3, circumradius : float = 1.0) -> None:
        """ Function to initialize the num of edges and circumradius"""
        
        if num_edges < 3:
            raise ValueError("Polygon must have atleast 3 edges")
        self.num_edges = num_edges
        self.circumradius = circumradius

    @property
    def count_edges(self):
        """ Function to return the number of edges"""
        return self.num_edges

    @property
    def count_vertices(self):
        """ Function to return the number of vertices. Number of vertices \
            equals number of edges in a regular polygon"""

        return self.num_edges

    @property
    def circumradius(self):
        """ Function to return Circumradius"""

        return self._circumradius

    @circumradius.setter
    def circumradius(self, value):
        """ Setter for Circumradius"""
        if(value < 0):
            raise ValueError(" Radius should be greater than 0")
        self._circumradius = value

    @property
    def interior_angle(self):
        """Function to calculate the interior angle"""
        return (self.num_edges - 2) * 180 / self.num_edges

    @property
    def side_length(self):
        """Function to calculate the edge length"""
        return 2 * self.circumradius * math.sin(math.pi / self.num_edges)

    @property
    def apothem(self):
        """Function to calculate the apothem"""
        return self.circumradius * math.cos(math.pi / self.num_edges)

    @property
    def area(self):
        """Function to calculate the area"""
        return 1/2 * self.num_edges * self.side_length * self.apothem

    @property
    def perimeter(self):
        """Function to calculate the perimeter"""
        return self.num_edges * self.side_length

    def __repr__(self):
        """Repr Function to return the no of edges and Circumradius"""
        return f"Polygon(n={self.count_vertices}, R={self.circumradius})"

    def __eq__(self, other):
        """Equality function to compare whether 2 polygons are equal by \
            comparing the number of edges and circumradius"""
        
        if isinstance(other, self.__class__):
            return self.num_edges == other.num_edges and self.circumradius == other.circumradius
        else:
            return NotImplemented

    def __gt__(self, other):
        """Greater than function to compare whether which of the 2 polygons \
            is bigger by comparing the number of vertices"""
            
        if isinstance(other, self.__class__):
            return self.num_edges > other.num_edges
        else:
            return NotImplemented
