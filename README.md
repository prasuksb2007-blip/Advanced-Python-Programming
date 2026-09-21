
# Advanced Python — Course Syllabus

## Overview
This course covers advanced Python concepts with a focus on practical skills and real-world applications. Topics include object-oriented design, dynamic programming, scripting, data analysis with NumPy and Pandas, concurrency, and performance optimization.

## Table of Contents
- [Course Objectives](#course-objectives)
- [Learning Outcomes](#learning-outcomes)
- [Course Structure](#course-structure)
- [Assignments & Labs](#assignments--labs)
- [Repository Structure](#Repository-Structure)

## About Python Language
Python is a high-level, interpreted, general-purpose programming language known for its clear syntax, readability, and strong standard library. It supports multiple programming paradigms (procedural, object-oriented, and functional) and has a large ecosystem of third-party packages available via PyPI. Python is widely used in web development, data science, machine learning, automation, scripting, and scientific computing.

## Getting Started
Follow these steps to prepare your environment and run the example scripts.

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install optional dependencies if present:

```bash
pip install -r requirements.txt
```

3. Run the Library Management example:

```powershell
python libary_managment.py
```

4. Running assignment starters or tests:

- Place starter scripts in `examples/` or `labs/` and run them with `python examples/<script>.py`.
- For data analysis, open notebooks in `notebooks/` with Jupyter Lab or Notebook.

Notes
- This repository assumes Python 3.8+. If you are using a different Python version, update the virtual environment command accordingly.
- Add a `requirements.txt` file listing any external packages used for assignments or labs.

## Course Objectives
By the end of this course, students will be able to:
- Apply object‑oriented programming concepts to design maintainable Python applications.
- Solve complex problems using dynamic programming (memoization and tabulation).
- Manipulate and analyze data efficiently using NumPy and Pandas.
- Write robust Python scripts for file processing, regular expressions, and CLI tools using `argparse`.
- Optimize Python code for performance and memory efficiency.

## Learning Outcomes
Graduates of this course will be able to:
1. Design and implement Python applications following OOP principles and design patterns.
2. Apply dynamic programming techniques to solve optimization and sequence problems.
3. Develop scripts for file I/O, regex-based text processing, and command-line automation.
4. Perform data cleaning, transformation, and exploratory analysis with Pandas and NumPy.
5. Profile and optimize Python code for better runtime and memory characteristics.

### Unit I — Object Oriented Programming (9 hours)
- Core concepts: classes, objects, constructors, variable scopes.
- Methods: instance, class, static; magic methods (`__init__`, `__str__`, `__repr__`).
- OOP pillars: inheritance, encapsulation, abstraction, polymorphism, composition.
- Advanced topics: decorators, iterators, generators, closures.
- Design: common patterns (Singleton, Factory, Observer, Strategy) and SOLID principles.
Case Study: Library Management System (OOP implementation)

### Unit II — Dynamic Programming (12 hours)
- Concepts: memoization, tabulation, overlapping subproblems.
- Techniques: bottom-up and top-down approaches.
- Problems: Fibonacci (efficient), Longest Common Subsequence, 0/1 Knapsack.

### Unit III — Scripting & Text Processing (12 hours)
- File I/O: text, CSV, JSON, XML; context managers.
- Regular expressions for pattern matching and extraction.
- Command-line tools using `argparse`.
Case Study: Extract IPs, timestamps, and URLs from server logs.

### Unit IV — NumPy & Pandas (12 hours)
- NumPy: arrays, indexing, broadcasting, vectorized operations.
- Pandas: Series, DataFrame, cleaning, merge/aggregate operations.
- EDA: descriptive statistics, visualization, handling missing data.
Case Study: eCommerce sales analysis.

### Unit V — Advanced Topics (12 hours)
- Concurrency: `threading`, `multiprocessing`, and `async` patterns; GIL impacts.
- Logging best practices and structured logging.
- Memory management: profiling, `gc`, and visualization tools (`memory_profiler`, `objgraph`).

## Assignments & Labs
Representative assignments by unit:
- Unit I: Library Management System (OOP); dynamic report generator; strategy pattern payment processor.
- Unit II: Efficient Fibonacci; LCS; 0/1 Knapsack (top-down and bottom-up).
- Unit III: File extraction script; CSV→JSON converter; regex email extractor.
- Unit IV: NumPy array (1–10); Pandas Series with random values; EDA on a dataset.
- Unit V: Multi-threading demo; multiprocessing example; logging exercises; memory profiling and `gc` experiments.

### Repository Structure
The repository contains the following core implementation files:
* **`basic_oop_program.py`**: Basic object-oriented programming examples
* **`libary_managment.py`**: Case study: simplified Library Management System (OOP)
* **`dynamic_report_generator.py`**: Case study: simplified Dynamic Report Generator (OOP)
* **`strategy_pattern_payment_processor.py`**: Case study: simplified Strategy Pattern Payment Processor.py (OOP)
* **`advanced_python_concept.py`**: Advanced Python concepts and implementations
* **`design_pattern.py`**: Design pattern implementations
* **`fibonacci_sequence.py`**: Case study: Efficient Fibonacci implementation (dynamic programming)
* **`lcs.py`**: Case study: Longest Common Subsequence implementation
* **`0_1_knapsack.py`**: Case study: 0/1 Knapsack implementation (dynamic programming)
* **`regex_email_extractor.py`**: Case study: Regex Email Extractor implementation
* **`file_extraction_script.py`**: Case study: File Extraction Script implementation
* **`csv_json_converter.py`**: Case study: CSV to JSON converter implementation