def my_function(x):
    y = x[::-1]
    return y


x = 'I can do it'
assert my_function(x) == "ti od nac I"

x = 'apricot'
print(my_function(x))
