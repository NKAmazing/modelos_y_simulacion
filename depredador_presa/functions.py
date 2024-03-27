from constants import RANGE_LIMITS

def set_range_limit(variable_option):
    '''
    Set the range limit of the axis
    '''
    results = {}
    if variable_option in [1, 2, 3]:
        for key, value in RANGE_LIMITS[variable_option].items():
            results[key] = value
    else:
        for key, value in RANGE_LIMITS[1].items():
            results[key] = value
    return results
