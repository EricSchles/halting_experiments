import inspect

def contains_infinite_loop(function):
    source_code = []
    for line in inspect.getsourcelines(function)[0]:
        source_code.append(line)

    #static checks
    if any(["while True:" in line for line in source_code]):
        return True
    
    
