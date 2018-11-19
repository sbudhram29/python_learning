def addWorld(func):
    """
    returns a callable function that adds world to the end of a string
    """
    def world():
        """
        adds world to end of string
        """
        return func() + ' world'

    return world


@addWorld
def hello():
    return 'Hello'


print(hello())
