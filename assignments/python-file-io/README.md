# 📘 Assignment: Python File I/O and Data Persistence

## 🎯 Objective

Learn how to read from files, write data back to files, and keep structured CSV data using Python file I/O.

## 📝 Tasks

### 🛠️ Read from a text file

#### Description
Write a function called `read_file_contents()` that opens a text file, reads its contents, and returns the text.

#### Requirements
Completed program should:

- Open the file path provided as an argument.
- Read the full text from the file.
- Return the file contents as a single string.
- Handle the file using a `with` statement.

### 🛠️ Write a log file

#### Description
Write a function called `write_log_entries()` that saves a list of log messages to a text file.

#### Requirements
Completed program should:

- Accept a file path and a list of strings.
- Write each string to the file on its own line.
- Overwrite the file if it already exists.
- Use a `with` statement and `write()`.

### 🛠️ Work with CSV data

#### Description
Write functions called `save_scores_to_csv()` and `load_scores_from_csv()` to store and read numeric scores using the `csv` module.

#### Requirements
Completed program should:

- Save a list of student score records to a CSV file with headers.
- Read the saved CSV file and return a list of dictionaries.
- Use the `csv` module and file I/O best practices.
- Preserve the column names in the output records.
