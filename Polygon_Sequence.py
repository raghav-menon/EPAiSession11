from Polygon import Polygon


class Polygons:
    """Implementaion Of Custom Sequence of Polygons which takes largest \
        polygon num of edges and circumradius as input"""

    def __init__(self, m, R):
        """ Function initialising the number of edges and circumradius"""
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]

    def __len__(self):
        """Function returning the length of sequence"""
        return self._m - 2

    def __repr__(self):
        """Repr Function to print regarding the initialized variables"""
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        """Function to retrieve a particular element in the sequence or a \
            list of elements"""
        return self._polygons[s]

    def __iter__(self):
        """Iterator Function--> This function converts this class to an \
            Iterator returning an Iterator object"""
        return self.PolygonIter(self)

    @property
    def max_efficiency_polygon(self):
        """Function to calculate the maximum efficiency of the Polygon"""
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area/p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]

    class PolygonIter:
        """This is an Iterator class which converts the main class into an \
            Iterator"""

        def __init__(self, polyobj):
            """Function initializing the polygon sequence object and \
                index. Index is used to return the next element in the polygon\
                    sequence when used as a iterator"""
            self._polyobj = polyobj
            self._index = 0

        def __iter__(self):
            """Iterator function which makes it an iterator object"""
            return self

        def __next__(self):
            """Next function to return the next element from an polygon \
                sequence iterator object"""
            if self._index >= len(self._polyobj):
                raise StopIteration
            else:
                item = self._polyobj._polygons[self._index]
                self._index += 1
                return item
