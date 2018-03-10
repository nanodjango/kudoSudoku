kudoSudoku 
**********
|p3| |p1| |p2| 



.. |p1| image:: https://img.shields.io/travis/VarshneyaB/kudoSudoku.svg
   :alt: Build status
   :target: https://travis-ci.org/VarshneyaB/kudoSudoku
   

.. |p2| image:: https://img.shields.io/github/stars/VarshneyaB/kudoSudoku.svg?style=social&logo=github&label=Stars
   :alt: GitHub stars
   :target: https://github.com/VarshneyaB/kudoSudoku


.. |p3| image:: https://img.shields.io/github/license/mashape/apistatus.svg 
   :alt: license




A sudoku solver that solves sudoku using constraint programming


Usage
=====

* import class **sudoku** from the module.
* pass puzzle to be solved as list of lists
* **sudoku** has a method called **solve( )** that returns the solved puzzle
* output will be an object with the following keys
    1. `done` : "describing status if its done or not"
    2. `iterations` : "number of times puzzle is re visited"
    3. `guesses` : "number of places where it had to guess"
    4. `timeTaken` : "Time taken to conclude"
    5. `solution` : "Final answer(will be list of list of integers)"



Example
=======

To solve this sudoku

.. image:: https://raw.githubusercontent.com/VarshneyaB/kudoSudoku/master/download.png
   :alt: a 2x2 sudoku

Input has to be:


.. code-block:: python

   [[0,2,4,0],[1,0,0,3],[4,0,0,2],[0,1,3,0]]






.. code-block:: python

    from kudoSudoku import sudoku
    puzzle = [[0,2,4,0],[1,0,0,3],[4,0,0,2],[0,1,3,0]]
    table = sudoku(puzzle)
    result = table.solve()
    print(result)


Output:

.. code-block:: python


    {'done': True, 'iterations': 2, 'guesses': 0, 'timeTaken': 0.0013199988754573474, 'solution': [[3, 2, 4, 1], [1, 4, 2, 3], [4, 3, 1, 2], [2, 1, 3, 4]]}


2X2 sudoku is taken just to demonstrate. It works for any nxn sudoku
