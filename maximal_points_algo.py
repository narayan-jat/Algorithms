"""
This script implements maximal points algorithm in two ways one from left to right
and other from right to left.

Author: Narayan jat
Date: 27 January 2024
"""


class MaximalPoints(object):
    """This class implements the methods which identify the maximal points from given points."""
    class _Point:
        """This is lightweight private class which holds the point and it's operations."""
        __slots__ = '_x', '_y'

        def __init__(self, x, y):
            self._x = x
            self._y = y

        @property
        def x(self):
            """This is x coordinate of point."""
            return self._x

        @property
        def y(self):
            """This is y coordinate of point."""
            return self._y

    __slots__ = '_n', '_points'

    def __init__(self, n):
        self._n = n
        self._points = []

    def __str__(self):
        """Prints the points."""
        s = ""
        for i in range(self._n):
            s += f"{(self._points[i].x, self._points[i].y)}, "
        return s

    def add_point(self, x, y):
        """This adds new point to the points list."""
        self._points.append(self._Point(x, y))

    def sort_points(self):
        """Sorts the points in place based on the x-coordinate."""
        self._points.sort(key=lambda point: point.x)

    def left_to_right(self):
        """This finds maximal points by left to right method."""
        comparison = 0
        self.sort_points()      # Sorting the points based on x coordinate.
        maximal_points = [(self._points[0].x, self._points[0].y)]  # Considering first point as maximal.
        c_point = maximal_points[-1]
        for i in range(1, self._n):
            n_point = self._points[i]
            comparison += 1
            if c_point[1] < n_point.y:
                comparison = comparison + MaximalPoints._update_maximal_points(n_point, maximal_points)
            maximal_points.append((n_point.x, n_point.y))
            c_point = maximal_points[-1]
        print("Maximal points:\t", maximal_points)
        print("Number of comparisons:\t", comparison)

    def right_to_left(self):
        """This finds maximal points by right to left method."""
        self.sort_points()      # Sorting the points first.
        c_point = self._points[-1]
        comparison = 0
        print("Maximal points:\t", end='')
        for i in range(self._n - 2, -1, -1):
            n_point = self._points[i]
            # Adding points to maximal points if point is maximal
            comparison += 1
            if n_point.y >= c_point.y:
                print((c_point.x, c_point.y), end=', ')
                c_point = n_point       # Updating next point to current point.
        print((c_point.x, c_point.y))       # Adding for the first point.
        print("Number of comparisons:\t", comparison)

    # Helper class methods.
    @staticmethod
    def _update_maximal_points(n, pl):
        pl.pop()
        comparison = 0
        while len(pl) > 0:
            c = pl[-1]
            comparison += 1
            if c[1] < n.y:
                pl.pop()
            else:
                return comparison
        return comparison


def user_input():
    try:
        n = int(input("Enter the number of points: "))
    except ValueError:
        raise ValueError("Please enter a valid integer value only")
    points = MaximalPoints(n)
    i = 1
    while i <= n:
        try:
            x, y = map(float, input(f"Enter x{i} and y{i} respectively separated by single space: ").split(' '))
            points.add_point(x, y)
            i += 1
        except (ValueError, TypeError):
            print("Please provide numerical values in proper format. Try again for same point")
    return points


def main():
    points = user_input()
    print("Your points entered are: \n", points, "\n\n")
    print("Output and number of comparisons from RIGHT TO LEFT technique: ")
    points.right_to_left()
    print("\n\nOutput and number of comparisons from LEFT TO RIGHT technique: ")
    points.left_to_right()


# Calling main function
main()
