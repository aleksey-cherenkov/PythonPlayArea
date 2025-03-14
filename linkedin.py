def string_combiner(*args, unique=False):
    result = ''.join(str(x) for x in args if (isinstance(x, str) or isinstance(x, int)))
    return result

items = ["This", "is", 1, True, "string!"]
useUnique = False

# uncomment each of the following lines to try other test cases
# also try different values for useUnique
#items = ["This", "is", 0.1, "test", "string!"]
#items = ["This", "is", 1, True, "string!"]
#items = ["This", "is", [1, 2], "string!"]

# Don't change how the function is called
result = string_combiner(*items, unique=useUnique)