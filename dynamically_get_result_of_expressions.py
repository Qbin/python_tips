def dynamically_get_result_of_expressions(expressions, fields, *args):
    """
    :param expressions: python's expressions
    :param fields: all variable of the expressions used
    :param args: all value of variable what you want to assignment
    :return: the result of the expressions when these variable assignment these value
    """
    for i in range(len(fields)):
        locals()[fields[i]] = args[i]
    return eval(expressions)

print(dynamically_get_result_of_expressions("((a+b)*c)**c",["a","b","c"],2,3,4))