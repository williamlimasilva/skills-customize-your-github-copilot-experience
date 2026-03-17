# 📘 Assignment: Python Text Processing

## 🎯 Objective

Master Python string manipulation, file input/output operations, and text processing techniques. You will practice reading files, processing text data, and writing transformed results back to files.

## 📝 Tasks

### 🛠️ String Manipulation and Text Analysis

#### Description
Write a program that reads a text file and performs various string operations to analyze and transform the text content.

#### Requirements
Completed program should:

- Read text from a file using file I/O operations.
- Convert all text to lowercase and uppercase, and display character statistics (total characters, words, lines, unique words).
- Find and replace specific words in the text with alternative words.
- Count the frequency of each word and display the top 5 most common words.
- Example output:
  ```
  File: sample.txt
  Total characters: 1250
  Total words: 245
  Total lines: 12
  Unique words: 89
  Top 5 words: ["the", "and", "is", "to", "a"]
  ```

### 🛠️ File Processing and Text Transformation

#### Description
Create a program that processes multiple lines of text, applies transformations, and writes the results to a new file.

#### Requirements
Completed program should:

- Read a text file line by line.
- Strip leading/trailing whitespace from each line.
- Filter out empty lines and lines starting with a comment character (e.g., `#`).
- Convert filtered lines to a consistent format (e.g., title case, capitalized).
- Write the transformed text to a new output file.
- Include error handling for file not found and permission errors.
- Example usage:
  ```
  Input:  "  hello world  "
  Output: "Hello World"
  ```
