import json

def remove_duplicates_preserve_format(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = [json.loads(line) for line in file]

        # Use a set to remove completely duplicate records
        # Since dictionaries are not hashable, convert them to JSON strings for deduplication
        unique_data = []
        seen = set()
        
        for record in data:
            record_str = json.dumps(record, sort_keys=True)  # Convert dictionary to a sorted JSON string
            if record_str not in seen:
                seen.add(record_str)
                unique_data.append(record)

        with open(output_file, 'w') as file:
            for record in unique_data:
                file.write(json.dumps(record) + '\n')

        print(f"Cleaned data has been saved to: {output_file}")
    
    except Exception as e:
        print(f"Error occurred while processing the file: {e}")


input_path = "betting_data/wallet_bettings.json"
output_path = "betting_data/cleaned_wallet_bettings.json"

remove_duplicates_preserve_format(input_path, output_path)
