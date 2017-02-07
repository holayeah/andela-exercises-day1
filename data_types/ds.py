def data_type(variable):
    """
    Does stuff basing on the data type of the 
    variable
    """
    if variable == None:
        return 'no value'

    if isinstance(variable, str):
        return len(variable)
    elif isinstance(variable, bool):
        return variable
    elif isinstance(variable, int):
        if variable > 100:
            return 'more than 100'
        elif variable < 100:
            return 'less than 100'
        else: 
            return 'equal to 100'
    elif isinstance(variable, list):
        try:
            return variable[2]
        except IndexError:
            return None
