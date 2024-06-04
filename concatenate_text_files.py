import os

def concatenate_text_files(directory, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open(os.path.join(directory, filename), 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')


