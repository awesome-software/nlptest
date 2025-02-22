from .utils import (
    asian_names, black_names, country_economic_dict, hispanic_names, inter_racial_names, male_pronouns,
    native_american_names, neutral_pronouns, religion_wise_names, white_names, female_pronouns
)

def add_custom_data(data, name, append):
    """
    Adds custom data to the corresponding bias dictionaries based on the specified name.

    Args:
        data (dict or list): The data to be added.
        name (str): The type of bias dictionary to update. It should be one of the following:
            - "Country-Economic-Bias"
            - "Religion-Bias"
            - "Ethnicity-Name-Bias"
            - "Gender-Pronoun-Bias"
        append (bool): Specifies whether to append the values or overwrite them.

    Raises:
        ValueError: If the specified `name` is invalid or if the provided data has an invalid format or contains invalid keys.
    """
    if name == "Country-Economic-Bias":
        valid_names = country_economic_dict.keys()

        # Validate the schema
        if not set(data.keys()).issubset(valid_names):
            raise ValueError(f"Invalid schema. It should be one of: {', '.join(valid_names)}.")

        if append:
            # Append unique values to existing keys
            for key, values in data.items():
                unique_values = set(values)
                country_economic_dict[key] = list(set(country_economic_dict[key]) | unique_values)
        else:
            # Overwrite the keys' values
            for key, values in data.items():
                country_economic_dict[key] = values

    elif name == "Religion-Bias":
        valid_names = religion_wise_names.keys()

        # Validate the schema
        if not set(data.keys()).issubset(valid_names):
            raise ValueError(f"Invalid schema. It should be one of: {', '.join(valid_names)}.")

        if append:
            # Append unique values to existing keys
            for key, values in data.items():
                unique_values = set(values)
                religion_wise_names[key] = list(set(religion_wise_names[key]) | unique_values)
        else:
            # Overwrite the keys' values
            for key, values in data.items():
                religion_wise_names[key] = values

    elif name == "Ethnicity-Name-Bias":
        valid_names = (
            'white_names',
            'black_names',
            'hispanic_names',
            'asian_names',
            'native_american_names',
            'inter_racial_names'
        )

        # Validate the schema
        for data_dict in data:
            if 'name' not in data_dict:
                raise ValueError("Invalid JSON format. 'name' key is missing.")

            name = data_dict['name']
            first_names = data_dict.get('first_names', [])
            last_names = data_dict.get('last_names', [])

            if not isinstance(name, str):
                raise ValueError("Invalid 'name' format in the JSON file.")

            if name not in valid_names:
                raise ValueError(f"Invalid 'name' value '{name}'. It should be one of: {', '.join(valid_names)}.")

            if not first_names and not last_names:
                raise ValueError(f"At least one of 'first_names' or 'last_names' must be specified for '{name}'.")

            if set(data_dict.keys()) - {'name', 'first_names', 'last_names'}:
                raise ValueError(f"Invalid keys in the JSON for '{name}'. "
                                f"Only the following keys are allowed: 'name', 'first_names', 'last_names'.")

            bias_dict = {
                'white_names': white_names,
                'black_names': black_names,
                'hispanic_names': hispanic_names,
                'asian_names': asian_names,
                'native_american_names': native_american_names,
                'inter_racial_names': inter_racial_names
            }

            if name in bias_dict:
                bias = bias_dict[name]
                if append:
                    bias['first_names'].extend(set(first_names) - set(bias['first_names']))
                    bias['last_names'].extend(set(last_names) - set(bias['last_names']))
                else:
                    bias['first_names'] = list(set(first_names))
                    bias['last_names'] = list(set(last_names))
    elif name == "Gender-Pronoun-Bias":
        valid_names = ('female_pronouns', 'male_pronouns', 'neutral_pronouns')

        # Validate the schema
        for data_dict in data:
            if 'name' not in data_dict:
                raise ValueError("Invalid JSON format. 'name' key is missing.")

            name = data_dict['name']

            if name not in valid_names:
                raise ValueError(f"Invalid 'name' value '{name}'. It should be one of: {', '.join(valid_names)}.")

            pronouns = {
                'subjective_pronouns': data_dict.get('subjective_pronouns', []),
                'objective_pronouns': data_dict.get('objective_pronouns', []),
                'reflexive_pronouns': data_dict.get('reflexive_pronouns', []),
                'possessive_pronouns': data_dict.get('possessive_pronouns', [])
            }

            if all(key not in pronouns for key in
                   ['subjective_pronouns', 'objective_pronouns', 'reflexive_pronouns', 'possessive_pronouns']):
                raise ValueError(
                    f"Missing pronoun keys in the JSON for '{name}'. Please include at least one of: "
                    "'subjective_pronouns', 'objective_pronouns', 'reflexive_pronouns', 'possessive_pronouns'.")

            invalid_keys = set(data_dict.keys()) - {'name', 'subjective_pronouns', 'objective_pronouns',
                                                     'reflexive_pronouns', 'possessive_pronouns'}
            if invalid_keys:
                raise ValueError(
                    f"Invalid keys in the JSON for '{name}': {', '.join(invalid_keys)}. "
                    f"Only the following keys are allowed: "
                    "'name', 'subjective_pronouns', 'objective_pronouns', 'reflexive_pronouns', 'possessive_pronouns'.")

            bias_dict = {
                'female_pronouns': female_pronouns,
                'male_pronouns': male_pronouns,
                'neutral_pronouns': neutral_pronouns
            }

            if name in bias_dict:
                bias = bias_dict[name]
                if append:
                    bias['subjective_pronouns'].extend(set(pronouns['subjective_pronouns']) - set(bias['subjective_pronouns']))
                    bias['objective_pronouns'].extend(set(pronouns['objective_pronouns']) - set(bias['objective_pronouns']))
                    bias['reflexive_pronouns'].extend(set(pronouns['reflexive_pronouns']) - set(bias['reflexive_pronouns']))
                    bias['possessive_pronouns'].extend(set(pronouns['possessive_pronouns']) - set(bias['possessive_pronouns']))
                else:
                    bias['subjective_pronouns'] = pronouns['subjective_pronouns']
                    bias['objective_pronouns'] = pronouns['objective_pronouns']
                    bias['reflexive_pronouns'] = pronouns['reflexive_pronouns']
                    bias['possessive_pronouns'] = pronouns['possessive_pronouns']
    else:
        raise ValueError(f"Invalid 'test_name' value '{name}'. It should be one of: Country-Economic-Bias, Religion-Bias, Ethnicity-Name-Bias, Gender-Pronoun-Bias.")