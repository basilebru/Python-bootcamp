def ft_map(function_to_apply, list_of_inputs):
        return(function_to_apply(i) for i in list_of_inputs)

def double(i):
    return(i * 2)

l = [2, 4, 6]

l2 = ft_map(lambda x: x * 4, l)
print(next(l2))
print(next(l2))
print(next(l2))