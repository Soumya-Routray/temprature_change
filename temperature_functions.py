#temperaure conversion module
def Celsius_Fahrenheit(c):
    f= c*(9/5 )+ 32
    return f

def Celsius_Kelvin(c):
    k = c+273.15
    return k
    

def Fahrenheit_Celsius(f):
    c = (f-32) * 5/9
    return c


def Fahrenheit_Kelvin(f):
    k= (f-32)*5/9+273.15
    return k


def Kelvin_Celsius(k):
    c= k-273.15
    return c


def Kelvin_Fahrenheit(k):
    f = (k-273.15)*9/5+32
    return f

#step 1 - def function name (parameter)
#step 2 - store the formula to new variable
#step 3 - print or return the new variable