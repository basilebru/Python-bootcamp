from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
    if len(list_of_inputs) == 0:
        return(0)
    if len(list_of_inputs) == 1:
        return(list_of_inputs[0])
    r = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for i in list_of_inputs[2:]:
        r = function_to_apply(r, i)
    return(r)

def big(x, y):
    if len(x) > len(y):
        return(x)
    else:
        return(y)

l = ["basile"]
print(ft_reduce(big, l))