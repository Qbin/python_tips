def dynamically_get_result_of_expressions(expressions, fields, *args):
    for i in range(len(fields)):
        locals()[fields[i]] = args[i]
    return eval(expressions)

print(dynamically_get_result_of_expressions("((a+b)*c)**c",["a","b","c"],2,3,4))