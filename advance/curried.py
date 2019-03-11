def curried_f(x, y=None, z=None):
    def f(x, y, z):
        return x**3 + y**2 + z

    if y is not None and z is not None:
        return f(x, y, z)

    if y is not None:
        return lambda z: f(x, y, z)

    return lambda y, z=None: (
        f(x, y, z) if (y is not None and z is not None)
        else (lambda z: f(x, y, z))
    )


call_x = curried_f(2)
call_z = call_x(3)
print(call_z(4))
