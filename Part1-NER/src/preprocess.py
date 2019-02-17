import nltk
import re


def convert_integer_file_number_to_string(file_number):
    if(file_number <= 9):
        return "00" + str(file_number)
    elif(file_number <= 99):
        return "0" + str(file_number)
    return str(file_number)


def fetch_annotated_tokens(file_number):
    # Read all lines from the given file
    filename = "../dataset/" + convert_integer_file_number_to_string(file_number) + ".txt"
    with open(filename, 'r') as f:
        document_lines = f.readlines()

    # Now, read line by line
    annotated_tokens = []
    for line in document_lines:
        # Find the positions of <loc> and </loc>
        start_positions = list(re.finditer('<loc>', line))
        end_positions = list(re.finditer('</loc>', line))
        for i in range(0, len(start_positions)):
            # Extract out the part between <loc> and </loc>
            annotated_tokens.append(line[start_positions[i].end():end_positions[i].start()])
    print(annotated_tokens) # TODO: Remove this once stabilized
    return annotated_tokens

def main():
    # Test API
    fetch_annotated_tokens(113)

if __name__ == "__main__":
    main()
