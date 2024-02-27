import pandas as pd
import json
import re

# Script description:
# This script is used to clean the dataset and create a new dataset with a column for each attack type

# Load the dataset
df = pd.read_csv('../data_collection/attacks-on-health-care-systems-data.csv')
def split_ignore_parentheses(s):
    # Pattern to match commas that are not inside parentheses
    # This pattern looks for commas that are followed by an even number of quotes
    # assuming that the parentheses are well-balanced and not nested(IED)
    pattern = r',\s*(?![^()]*\))'
    return re.split(pattern, s)


def fixStringWitoutClosingParentheses(s):
    if (s.count('(') > s.count(')')):
        return s + ')'
    return s
        

def removeIEDEnding(s):
    if ('(IED)' in s):
        return s.replace('(IED)', '')
    return s

def remove_parentheses(s):
    # Pattern to match an opening parenthesis, any characters not being parentheses, and a closing parenthesis
    pattern = r"\([^()]*\)"
    # Replace the matched patterns with an empty string
    return re.sub(pattern, '', s)


attackTypeRows = df['Attack Type'].tolist()

uniqueAttackTypes = set(attackTypeRows)

allAttackTypes = []

for at in uniqueAttackTypes:
    s = removeIEDEnding(at)
    s = fixStringWitoutClosingParentheses(s)
    splitAttackTypes = split_ignore_parentheses(s)
    for sat in splitAttackTypes:
        allAttackTypes.append(remove_parentheses(sat).strip())
        
uniqueAllAttackTypes = list(set(allAttackTypes))


new_df = df.copy()

for attack_type in uniqueAllAttackTypes:
    new_df[attack_type] = new_df['Attack Type'].apply(lambda x: attack_type in x)
    

output_file_path = '../data_collection/attacks-on-health-care-systems-cleaned.csv'
new_df.to_csv(output_file_path, index=False)

    
    
    
