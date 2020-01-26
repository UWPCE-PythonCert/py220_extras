# Lesson 4 assignment

In this week's assignment we are going to practice using iteration to process data files.

In the first part of this assinment you will generate a data file using random data, that you will then process in the second part.

You will quickly recognize how the techniques you have learned this week can help.

## Generate file

The file you are going to generate has this layout:

product_name
customer_id
quantity_rented
unit_rental_price_monthly
rental_period_months

The file must have at least 10,000 records.

customer_id is an integer that starts at 1 and increments by 1 for each new customer. A customer can rent one or more products.

product_name is one of:
dining chair
dining table
bed
dining set
stool
couch
occasional table
recliner

quantity_rented is a random integer between 1 and 4

unit_rental_price_monthly is a random float between 1.50 and 25.00

rental_period_months is an integer between 6 and 60

You will write python code to generate that file. It should be a csv file with the first row as headings.

Hints:
- for product_name you can randomly select from a tuple.
- to generate random numbers from low to hight use random.randrange()

## Analyze file

Produce the following analyses. Show the output by using print on the collections you produce. Consider if tests may help you and include those (but not mandatory).

### Analyses for you to produce
The top 10 products by based on total monthly payments received (assume bills are always paid).

The top 5 customers based on quantity of products rented.

The top 10 customers for every product based on total monthly payments received (again assuming bills are always paid).

The 20 customers who made the lowest total monthly payments.

Be sure to use a generator in one solution. And be creative in the techniques you use.

