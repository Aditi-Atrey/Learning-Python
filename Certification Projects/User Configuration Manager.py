#User Configuration Manager

test_settings = {
    'theme': 'light',
    'notifications':'enabled',
    'volume':'high'
}

def add_setting(dictionary, key_value_pair):
    key, value = key_value_pair
    key = key.lower()
    value = value.lower()

    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, key_value_pair):
    key, value = key_value_pair
    key = key.lower()
    value = value.lower()

    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, keys):
    keys = keys.lower()

    if keys in dictionary:
        dictionary.pop(keys)
        return f"Setting '{keys}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dictionary):

    if dictionary == {}:
        return "No settings available."
    else:
        output = "Current User Settings:\n"
        for key, value in dictionary.items():
             output += f"{key.capitalize()}: {value}\n"
        return output
