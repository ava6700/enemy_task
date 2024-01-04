
None selected 


Skip to content
Using Gmail with screen readers

9 of 14,524
(no subject)
Inbox

Adit Ishraq
Attachments
Jan 4, 2024, 11:33 PM (4 hours ago)
to me


Regards,

Adit Ishraq

Stockholms universitet

Portfolio : Adit Ishraq
Google Scholar: Adit Ishraq
Linkedin: Adit Ishraq

ResearchGate: Adit Ishraq

 One attachment
  •  Scanned by Gmail
import os
import re
from collections import defaultdict

def index_files(directory):
    index = defaultdict(list)
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read().lower()  
                words = re.findall(r'\b\w+\b', content)  
                index[filename] = set(words)
    return index

def calculate_rank(search_words, file_words):
    if not search_words:
        return 0
    common_words = set(search_words) & file_words
    rank = (len(common_words) / len(search_words)) * 100
    return round(rank, 2)

def search_files(index, search_words):
    results = []
    for filename, file_words in index.items():
        rank = calculate_rank(search_words, file_words)
        if rank > 0:  
            results.append((filename, rank))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:10]

def main(directory):
    index = index_files(directory)
    print(f"{len(index)} files read in directory {directory}")

    while True:
        search_input = input("search> ")
        if search_input == ":quit":
            break

        search_words = re.findall(r'\b\w+\b', search_input.lower())
        results = search_files(index, search_words)

        if results:
            for filename, rank in results:
                print(f"{filename} : {rank}%")
        else:
            print("no matches found")

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception('No directory given to index')

    indexable_directory = args[0]
    main(indexable_directory)
main.py
Displaying main.py.
