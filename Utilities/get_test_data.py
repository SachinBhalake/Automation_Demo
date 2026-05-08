import yaml

def get_test_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)