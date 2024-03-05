"""
This script implements greedy algorithm in two ways one from left to right
and other from right to left.

Author: Narayan jat
Date: 2 March 2024
"""


class Greedyalgo(object):
    """This class implements the methods which selects the activities from given points."""
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

    __slots__ = '_n', '_activities'

    def __init__(self, n):
        self._n = n
        self._activities = []

    def __str__(self):
        """Prints the points."""
        s = ""
        for i in range(self._n):
            s += f"{(self._activities[i].x, self._activities[i].y)}, "
        return s

    def add_point(self, x, y):
        """This adds new point to the points list."""
        self._activities.append(self._Point(x, y))

    def sort_activities(self, k):
        """Sorts the points in place based on the x-coordinate."""
        if k == "y":
            self._activities.sort(key=lambda point: point.y)
        else:
            self._activities.sort(key=lambda point: -point.x)

    def left_to_right(self):
        """This selects activities left to right method."""
        comparison = 0
        self.sort_activities("y")      # Sorting the points based on end time.
        activity_selected = [(self._activities[0].x, self._activities[0].y)]
        c_point = activity_selected[-1]
        for i in range(1, self._n):
            n_point = self._activities[i]
            comparison += 1
            if c_point[1] < n_point.x:
                activity_selected.append((n_point.x, n_point.y))
            c_point = activity_selected[-1]
        print("Selected activities:\t", activity_selected)
        print("Number of comparisons:\t", comparison)

    def right_to_left(self):
        """This selects activities right to left method."""
        self.sort_activities("x")      # Sorting the activitis first.
        activity_selected = [(self._activities[0].x, self._activities[0].y)]
        c_point = activity_selected[-1]
        comparison = 0
        for i in range(1, self._n):
            n_point = self._activities[i]
            comparison += 1
            if n_point.y <= c_point[0]:
                activity_selected.append((n_point.x, n_point.y))
            c_point = activity_selected[-1]
        print("Number of comparisins:", comparison, "\n")
        return activity_selected


def user_input():
    try:
        n = int(input("Enter the number of activities: "))
    except ValueError:
        raise ValueError("Please enter a valid integer value only")
    points = Greedyalgo(n)
    i = 1
    while i <= n:
        try:
            x, y = map(float, input(f"Enter start time and end time respectively separated by single space: ").split(' '))
            points.add_point(x, y)
            i += 1
        except (ValueError, TypeError):
            print("Please provide numerical values in proper format. Try again for same point")
    return points


def main():
    points = user_input()
    print("Inputted slots are: \n", points, "\n\n")
    print("Selected activities and number of comparisons from RIGHT TO LEFT technique: ")
    print("Selected points:", points.right_to_left())
    print("\n\nSelected activities and number of comparisons from LEFT TO RIGHT technique: ")
    points.left_to_right()


# Calling main function
main()
