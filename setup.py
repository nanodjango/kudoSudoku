from setuptools import setup,find_packages

long_description = ""
with open ('README.rst', encoding='utf-8') as f:
	long_description = f.read()

setup(
    name = "kudosudoku",
    version = "1.0.0",
    description = "Sudoku solver,that solves sudoku puzzles using constraint programming",
    url = "https://github.com/VarshneyaB/kudoSudoku.git",
    author = "Varshneyabhushan",
    author_email = "varshneyacoder@gmail.com",
    license = "MIT License",
    packages = find_packages(),
    long_description = long_description,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    keywords = "sudoku solving solve puzzle kudos constraint"
)