def func():
	print("r")

func()	


class Vector:
        def __init__(self, values):
                self._values = values

        def __eq__(self, other):
                return tuple(self) == tuple(other)
        
