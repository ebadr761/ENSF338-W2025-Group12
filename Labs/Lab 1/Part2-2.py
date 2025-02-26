def count_vowels(word):
    vowels = "aeiouyAEIOUY"
    return sum(1 for char in word if char in vowels)

def process_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the starting point after "CHAPTER 1. Loomings."
    start_line = next((i for i, line in enumerate(lines) if "CHAPTER 1. Loomings." in line), None)
    
    if start_line is None:
        print("Start line not found.")
        return

    # Process the lines starting from the next line
    lines_to_process = lines[start_line + 1:]

    total_vowels = 0
    total_words = 0

    for line in lines_to_process:
        words = line.split()
        for word in words:
            total_vowels += count_vowels(word)
            total_words += 1

    if total_words > 0:
        avg_vowels = total_vowels / total_words
        print(f"Average number of vowels per word: {avg_vowels:.2f}")
    else:
        print("No words found to process.")

# Run the function with the file path
process_text("pg2701.txt")
