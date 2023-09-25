import pickle

# Define a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Pickle the dictionary
with open('my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)

# Unpickle the dictionary
with open('my_dict.pickle', 'rb') as f:
    loaded_dict = pickle.load(f)

# Print the unpickled dictionary
print(loaded_dict)
