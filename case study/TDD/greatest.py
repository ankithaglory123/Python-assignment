def findbigger(x,y,z):
    if(check_int_float(x) and check_int_float(y) and check_int_float(z)):
        if (x>=y and x>=z):
            return x
        elif (y>=x and y>=z):
            return y
        elif ( z>= x and z >= y):
            return z
    else:
        return "error"

def check_int_float(x):
    if(type(x)== int or type(x) == float):
        return True
    else:
        return False