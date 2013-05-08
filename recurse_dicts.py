"""
@author: Jonathan Mickle
@summary: Traverses a through multi level dictionaries to diff them and return the changes -- Thanks to Yi Fan for correcting logic
@param original: takes in the original unmodified JSON
@param modified: Takes in the modified json file for comparison
@return: a json dictionary of changes key-> value 
"""
def diffDict(original, modified):
    if isinstance(original, dict) and isinstance(modified, dict):
        changes = {}
        for key, value in modified.iteritems():
            if isinstance(value, dict):
                innerDict = diffDict(original[key], modified[key])
                if innerDict != {}:
                    changes[key] = {}
                    changes[key].update(innerDict)
            else:
                if original.has_key(key):
                    if value != original[key]:
                        changes[key] = value
                else:
                    changes[key] = value
                
                    
        return changes        
    else:
        raise Exception('parameters must be a dictionary')
