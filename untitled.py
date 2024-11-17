import os

def save_recent_files(file_list, filename='recent_files.txt', max_entries=5):
    # Ensure the directory for the file exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Truncate the list if it exceeds the maximum allowed entries
    file_list = file_list[:max_entries]
    
    # Save the list to the file
    with open(filename, 'w') as file:
        for file_path in file_list:
            file.write(file_path + '\n')

def load_recent_files(filename='recent_files.txt'):
    try:
        # Read the list from the file
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

# Example usage:
recent_files = load_recent_files()

# Add a new file to the list
new_file = 'example.txt'
recent_files.insert(0, new_file)

# Save the updated list
save_recent_files(recent_files)

# Print the recent files
print("Recent Files:", recent_files)
