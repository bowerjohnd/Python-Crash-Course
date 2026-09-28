from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print("\033[33m" + f"Sorry, the file {path} does not exist." + "\033[0m")
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print("\033[32m" + f"The file {path} has about {num_words} words." + "\033[0m")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
             'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)