class God:
    pow = 12
    # @classmethod #A classmethod is a method that works with the class (cls) and not with individual objects, and it cannot be used with __init__.
    @property #@property allows controlled access to instance variables while using attribute-style syntax.
    def Power(self):
        print(self.pow)

Hanuman = God()
Hanuman.pow = -12
Hanuman.Power