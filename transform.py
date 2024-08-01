from collections import defaultdict
import json

data = [
    {"parent": "shay", "dog": "looly", "food": "coocki"},
    {"parent": "shay", "dog": "looly", "food": "salad"},
    {"parent": "shay", "dog": "looly", "food": "pizza"},
    {"parent": "shay", "dog": "maple", "food": "pizza"},
    {"parent": "rou", "dog": "maple", "food": "pizza"},
    {"parent": "roy", "dog": "maple", "food": "hamborger"}
]

# Define the hierarchy
hierarchy = ['parent', 'dog', 'food']

def build_hierarchy(data, hierarchy):
    def nested_defaultdict():
        return defaultdict(nested_defaultdict)
    
    output = nested_defaultdict()
    
    for entry in data:
        current_level = output
        for key in hierarchy[:-1]:
            current_level = current_level[entry[key]]
        # Ensure the last level is an int to allow += operation
        if isinstance(current_level[entry[hierarchy[-1]]], defaultdict):
            current_level[entry[hierarchy[-1]]] = 0
        current_level[entry[hierarchy[-1]]] += 1
    
    return output

# Convert defaultdict to a regular dict
def convert_to_dict(d):
    if isinstance(d, defaultdict):
        return {k: convert_to_dict(v) for k, v in d.items()}
    return d

# Build and print the hierarchy
output = build_hierarchy(data, hierarchy)
output_dict = convert_to_dict(output)
print(json.dumps(output_dict, indent=4))
