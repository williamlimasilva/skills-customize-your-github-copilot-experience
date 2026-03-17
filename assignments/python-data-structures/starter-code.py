"""
Python Data Structures Starter Code

This template provides a foundation for working with lists, dictionaries, sets, and tuples.
Complete the tasks outlined in the assignment to implement the required functionality.
"""

# TODO: Task 1 - Work with Lists and Tuples
# Implement the following functions:


def create_student_list():
    """
    Create and return a list of student dictionaries.
    Each student should have: id, name, grade
    """
    pass


def sort_students(student_list, key):
    """
    Sort students by a given key (name or grade).
    
    Args:
        student_list (list): List of student dictionaries
        key (str): Sort key - either 'name' or 'grade'
        
    Returns:
        list: Sorted list of students
    """
    pass


def find_student(student_list, student_id):
    """
    Find a student by ID.
    
    Args:
        student_list (list): List of student dictionaries
        student_id (int): Student ID to search for
        
    Returns:
        dict or None: Student dictionary if found, None otherwise
    """
    pass


def get_top_grades(student_list, n):
    """
    Get the top n students by grade as a tuple.
    
    Args:
        student_list (list): List of student dictionaries
        n (int): Number of top students to return
        
    Returns:
        tuple: Top n students sorted by grade (highest first)
    """
    pass


# TODO: Task 2 - Use Dictionaries and Sets for Data Management
# Implement the following functions:


def word_frequency(text):
    """
    Count word frequency in text.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary with words as keys and counts as values
    """
    pass


def find_unique_words(text):
    """
    Find unique words in text (lowercase, no punctuation).
    
    Args:
        text (str): Input text
        
    Returns:
        set: Set of unique words
    """
    pass


def find_common_words(texts):
    """
    Find words common to all texts.
    
    Args:
        texts (list): List of text strings
        
    Returns:
        set: Set of words common to all texts
    """
    pass


def student_performance_report(student_list):
    """
    Create a report grouping students by grade range.
    
    Args:
        student_list (list): List of student dictionaries
        
    Returns:
        dict: Dictionary with grade ranges as keys and lists of names as values
    """
    pass


# TODO: Main program
# Test your functions with sample data


if __name__ == "__main__":
    # Add your test code here
    pass
