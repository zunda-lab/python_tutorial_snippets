class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()

x.f()
# 'hello world'

xf = x.f
while True:
    print(xf())

