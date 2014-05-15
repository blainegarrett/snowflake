class Line(object):
    def __init__(self, *args, **kwargs):
        """
        Simple Representation of a Line
        """

        # TODO: This could be refactored, but it is probably fine for now for clarity
        # TODO: Validate call args for type
        # TODO: Catch infinite slope case i.e. div by 0
        if args:
            # At least one point given
            if len(args) == 2 and isinstance(args[0], tuple) and isinstance(args[1], tuple):
                # Given 2 points
                p1 = args[0]
                p2 = args[1]
                kwargs['slope'] = (p2[1] - p1[1])/(p2[0] - p1[0])
                kwargs['intercept'] = p2[1] - kwargs['slope'] * p2[0]

            elif len(args) == 1 and isinstance(args[0], tuple) and 'slope' in kwargs:
                # Given a point and a slope
                p1 = args[0]
                kwargs['intercept'] = p1[1] - kwargs['slope'] * p1[0]

            elif len(args) == 1 and isinstance(args[0], tuple) and 'intercept' in kwargs:
                # given a point and an y intercept (basically a point)
                p1 = args[0]
                p2 = (0, kwargs['intercept'])
                kwargs['slope'] = (p2[1] - p1[1])/(p2[0] - p1[0])

        # else: Given slope and intercept
        self.slope = kwargs['slope']
        self.intercept = kwargs['intercept']

    def __call__(self, x):
        # Evaluate the equation
        y = self.slope * x + self.intercept
        return y


f1 = Line((1,1), (2,2)) # eg. Given 2 points
f2 = Line(slope=1, intercept=0) # eg. given slope and intercept
f3 = Line((1,1), intercept=0) # eg. given slope and intercept
f4 = Line((1,1), slope=1) # eg. given slope and intercept
#f5 = Line((0,1), (0,2)) # eg. Given 2 points both with xi = 0 -> infinite slope

print f1(3) 
print f2(3)
print f3(3)
print f4(3)