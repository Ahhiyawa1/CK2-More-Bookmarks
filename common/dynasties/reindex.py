import re

def reindex_dynasties(input_path, output_path, start_id=23000012):
    with open(input_path, 'r', encoding='windows-1252') as f:
        content = f.read()

    # Match lines like "123 = {"
    pattern = re.compile(r'^(\d+)\s*=\s*{', re.MULTILINE)

    def replacer(match):
        nonlocal start_id
        replacement = f'{start_id} = {{'
        start_id += 1
        return replacement

    updated_content = pattern.sub(replacer, content)

    with open(output_path, 'w', encoding='windows-1252') as f:
        f.write(updated_content)

    print(f"Reindexed dynasties written to: {output_path}")

# Example usage:
input_file = '09_dynasties.txt'  # Update with the correct path if needed
output_file = '09_dynasties_reindexed.txt'
reindex_dynasties(input_file, output_file)
