# Your task is to write your own function, which behaves almost exactly like the original split() method, that is:
#
# must accept exactly one argument - a string;
# must return a list of words created from the string, divided into places where the string contains whitespace;
# if the string is empty, the function must return an empty list;
# its name should be mysplit()

def my_split(string):
    my_list = []
    if len(string) == 0:
        return my_list

    str_aux = None
    for i, char in enumerate(string):
        if contains_alnum(string):
            if not char.isspace():
                if str_aux is None:
                    str_aux = char
                else:
                    str_aux += char
            else:
                if str_aux is not None:
                    my_list.append(str_aux)
                    str_aux = None

        if i == len(string) - 1 and str_aux is not None:
            my_list.append(str_aux)

    return my_list


def contains_alnum(string):
    for char in string:
        if char.isalnum():
            return True
    return False


print(my_split("To be or not to be, that is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))
