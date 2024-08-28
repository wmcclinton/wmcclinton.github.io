import os
import sys

assert len(sys.argv) == 2

# Directory containing the Markdown files
folder_path = sys.argv[1]
output_file = 'Daily_Notes.md'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate over all files in the directory
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as infile:
                data = infile.read()
                print(filename, len(data))
                if len(data) > 20:
                    outfile.write(filename.replace('.md', '') + '\n\n') 
                    # Write the contents of the file to the output file
                    outfile.write(data)
                    # Optionally add a separator between files
                    outfile.write('\n\n---\n\n')  # Add a markdown horizontal line between files

print(f"Markdown files combined into {output_file}")
