# 📘 Assignment: Data Structures in Python

## 🎯 Objective

Learn to effectively use Python's built-in data structures—lists, dictionaries, sets, and tuples—to organize and manipulate data. You will practice choosing the right data structure for different problems and writing efficient code using their unique methods and operations.

## 📝 Tasks

### 🛠️ Work with Lists and Tuples

#### Description
Write functions that demonstrate working with lists and tuples, including sorting, searching, and modifying list data while understanding tuple immutability.

#### Requirements
Completed program should:

- Create a function `create_student_list()` that returns a list of student dictionaries with fields: `id`, `name`, and `grade`.
- Write a function `sort_students(student_list, key)` that sorts students by name or grade.
- Implement a function `find_student(student_list, id)` that uses a linear search to find and return a student by ID.
- Create a function `get_top_grades(student_list, n)` that returns the top n students by grade as a tuple.
- Example usage:
  ```python
  students = [{"id": 1, "name": "Alice", "grade": 95}, {"id": 2, "name": "Bob", "grade": 87}]
  sorted_students = sort_students(students, "grade")
  top_3 = get_top_grades(students, 3)
  ```

### 🛠️ Use Dictionaries and Sets for Data Management

#### Description
Build functions that use dictionaries for key-value storage and sets for efficient membership testing and deduplication.

#### Requirements
Completed program should:

- Create a function `word_frequency(text)` that returns a dictionary with word counts from a given text string.
- Write a function `find_unique_words(text)` that returns a set of unique words (lowercase, no punctuation).
- Implement a function `find_common_words(texts)` that takes a list of texts and returns the set of words common to all texts.
- Create a function `student_performance_report(student_list)` that returns a dictionary with grade ranges as keys and lists of student names as values.
- Example usage:
  ```python
  text = "hello world hello python"
  freq = word_frequency(text)  # {"hello": 2, "world": 1, "python": 1}
  unique = find_unique_words(text)  # {"hello", "world", "python"}
  ```
