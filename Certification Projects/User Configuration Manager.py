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

def update_setting(settings, pair):
    pass
