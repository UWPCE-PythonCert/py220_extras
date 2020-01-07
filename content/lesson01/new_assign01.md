# Lesson 01 Assignment

You may use this as an alternative to the assignment on Canvas, or in addition
to that assignment. Completing only one of these assignments will not adversely impact
your grade!

## Overview

The purpose of this assignment is to make sure you can setup a new project,
write some code and then run some automated tests. The material we covered in
class is very relevant to this.

## What you need to do
1. Create a new Python project
1. The project will use a list of tuples of product transactions as input.
1. The project will display a list of tuples of products and stock quantities as output.
1. The input tuple will contain a product name, a transaction type code of A,
   or S (add, sell), and a quantity.
1. There should be several transactions for each product, so quantities can be
   added and sold.
1. The output list of tuples will show the final stock quantities for every product as a
   result of processing all the transactions. 
1. There will be exactly one record in output for each input product, showing
   the product name and quantity.

So, If the input is:

`

   [
      ('Chair', 'A', 10),
      ('Bed', 'A', 12),
      ('Chair', 'S', 6)
   ]

`

The output will be:

`

   [
      ('Chair', 4),
      ('Bed', 12)
   ]

`

## Notes
1. Order does not matter in the output tuple.
1. You should have at least 20 input records, with a mix of As and Ss.
1. You should include tests to make sure that the program behaves correctly.
   Pay special attention to potential errors in input data, and any functions
   you will write.
1. Be sure to lint your code and resolve at least 80% of the issues

## Submission
1. use a zip tool to submit a .zip file to Canvas that contains the contents of
your src and tests directories.
1. email Andy and Luis when done.

NOTE THAT THIS SUBMISSION PROCESS APPLIES TO THIS ASSIGNMENT, AND THE ONE IN
git TOO. Ignore any instructions in github about cloning and pushing.
