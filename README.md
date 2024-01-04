# Text Search Engine
| Version Info | [![Python](https://img.shields.io/badge/python-v3.10.9-green)](https://www.python.org/downloads/release/python-3900/) [![Platform](https://img.shields.io/badge/Platforms-Ubuntu%2022.04.4%20LTS%2C%20win--64-orange)](https://releases.ubuntu.com/22.04/) [![anaconda](https://img.shields.io/badge/anaconda-v22.9.0-blue)](https://anaconda.org/anaconda/plotly/files?version=22.9.0) |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

# Overview

This command-line text search engine is a versatile tool designed to swiftly analyze and retrieve information from text files within a specified directory. Constructing an in-memory representation of these files enables dynamic and interactive searches, aiming to present the top 10 most relevant filenames based on user-input search terms. Words, identified as sequences of alphanumeric characters, form the core elements of the search, and the engine treats words with case insensitivity, ensuring inclusivity in matching criteria. Utilizing an efficient data structure for in-memory storage, such as a trie or inverted index, facilitates rapid search operations.

The ranking system, initially built on word frequency within documents, evolves iteratively to enhance result accuracy. To ensure reliability, the engine undergoes thorough testing, encompassing unit tests for individual components, integration testing for seamless module interaction, and user acceptance testing for usability assessments. This tool accommodates diverse file sizes and quantities, offering scalability and efficiency in navigating and processing information for varied search queries.


# Features
### Word Identification
#### Definition:
A word is identified as a contiguous sequence of alphanumeric characters, excluding symbols and special characters.
#### Case Insensitivity: Words are treated as equal regardless of case sensitivity (e.g., "Search" and "search" are considered the same word).
### Equality of Words
#### Matching Criteria: Two words are deemed equal if their normalized forms are identical, disregarding case sensitivity and special characters.
### Data Structure Design
In-Memory Representation: Implements an efficient data structure, such as a trie or inverted index, to store and manage indexed words and corresponding file references. This enhances search efficiency and response time.
#### Hash Tables in Text Search Engines:

- The core component of inverted indexes: Enables fast lookups of terms and retrieval of associated documents.
- Store term-document relationships efficiently.
- Contribute to rapid query processing and relevant result delivery.

#### Hash Function:

Converts a term (word) into a numerical value (hash code).
Acts as a "virtual address" in the hash table.
Distributes terms evenly across the table for efficient access.
Array as Underlying Structure:
Hash table is essentially an array with buckets.
Each bucket can hold multiple key-value pairs.
Storing Terms and Documents:

Term (key) is hashed to determine its bucket.
Term-document information (value) is stored in that bucket.
Lookups:

To find documents containing a query term:
Term is hashed to its bucket.
Bucket is checked for matching term-document data.
If found, relevant documents are retrieved.
Collision Handling:

Different terms can have the same hash code (collisions).
Handling methods:
Chaining: Link multiple key-value pairs in a bucket using linked lists.
Open Addressing: Find an alternative empty bucket using probing techniques.


### Ranking Score Design
Basic Ranking: Initial ranking is based on word frequency within documents, providing a foundation for relevance assessment.
Iterative Improvement: Ongoing refinement of the ranking algorithm to enhance search result accuracy as development progresses.

### Testability
Unit Testing: Rigorous unit tests cover various components of the search engine to ensure functionality and reliability.
To run this unittest
- Save the test files in the same directory as main.py.
- Run python -m unittest from the command line.
  ```
  python -m unittest
  ```

# Usage
```
$ ./text_search_engine --directory /path/to/text/files
Enter search terms: [Input search query]
Top 10 matching filenames:
1. filename_1.txt
2. filename_2.txt
...
10. filename_10.txt

```
### Setup: 
Specify the directory containing text files to be indexed.
### Search: 
Input search terms via the command line interface.
### Output:
Obtain the top 10 filenames ranked by relevance to the search query.

## Quickstart:
Clone the repository and set up the env.
```
mkdir venv
conda create -n venv python=3.10.9
conda activate venv
python3.10.9 -m venv ./venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

```



User Acceptance Testing: Provides a user-friendly interface for testers to evaluate the search engine's usability and effectiveness.
