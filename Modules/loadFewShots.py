import json

def load_few_shot_examples(file_path: str = 'few_shots.json'):
    """
    Loads few-shot examples from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing the few-shot examples.

    Returns:
        list: A list of dictionaries, where each dictionary represents a few-shot example.
              Returns an empty list if the file is not found or if there's a JSON decoding error.
    """
    print(f"--- Loading few-shot examples from '{file_path}' ---")
    try:
        with open(file_path, 'r') as f:
            few_shot_examples = json.load(f)
        print(f"Loaded {len(few_shot_examples)} few-shot examples successfully.")
        return few_shot_examples
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found. Please create the file with your few-shot examples.")
        return [] # Return empty list on FileNotFoundError
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{file_path}': {e}")
        print("Please ensure your few_shots.json file is valid JSON.")
        return [] # Return empty list on JSON decoding error

# How you would use this function in your main script:
# few_shot_examples = load_few_shot_examples()