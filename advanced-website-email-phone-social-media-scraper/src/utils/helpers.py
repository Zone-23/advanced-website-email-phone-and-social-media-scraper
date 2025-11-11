thonimport json

def save_data(data):
    with open('data/output.json', 'w') as f:
        json.dump(data, f, indent=4)