# Part 1: Create the virtual environment
import re
def analyze_data(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    words = re.findall(r'\b\w+\b', text.lower()) # Find all words
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    with open(output_file, 'w') as f:
        for word, count in word_counts.items():
            f.write(f"{word}: {count}\n")

parser = argparse.ArgumentParser(description='Analyze data from a file.')
parser.add_argument('input_file', help='path to the input file') 
parser.add_argument('output_file', help='path to the output file')