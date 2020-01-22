def ft_filter(function_to_apply, list_of_inputs):
    return(i for i in list_of_inputs if function_to_apply(i))

l = list(range(-5, 5))
print(l)

l2 = ft_filter(lambda x: x < 0, l)
for i in l2:
    print(i)