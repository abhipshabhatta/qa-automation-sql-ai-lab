
# Test Summary - OrderSprout

## What I tested

I used Python, Playwright and Pytest to check whether
the OrderSprout homepage opens successfully.

## Why I tested it

Before testing features such as adding or editing orders,
I wanted to make sure the application was running and
that Playwright could access it.

## Test details

Test ID: AUTO-001
Test name: test_ordersprout_homepage
Test type: Smoke test
Browser: Chromium
Test date: 27 November 2026

## What I expected

- The homepage should open.
- The server should return HTTP status 200.
- The page body should be visible.

## What happened

The homepage opened successfully.
The server returned HTTP 200.
The page body was visible.

Result: PASS

## Execution results

Total tests: 1
Passed: 1
Failed: 0

## What I learned

I learned how Playwright opens a browser and visits a
website. I also learned how to use assertions to check
whether the actual result matches the expected result.

Pytest generated an HTML report showing the test result.

## Limitations

This test only checks whether the homepage loads.
It does not verify order creation, payments, editing
or database information.



## AUTO-002 - Create an order

### What I wanted to check

I wanted to check whether a user could create
an order and see the correct information on
the homepage.

### Test data

Customer: A unique QA test customer
Item: Birthday cake
Delivery date: 15 December 2026
Status: New
Total: €50.00
Paid: €10.00
Expected remaining amount: €40.00

### How I tested it

I used Playwright to open the New Order form,
enter the order details, and save the order.

Then I checked that the correct order appeared
on the homepage with the expected amounts.

### Expected result

The order should be saved successfully.
The customer, item, total, paid amount and
remaining balance should be displayed correctly.

### Issue found during testing

The test initially passed, but failed when I
ran it again.

Playwright found two orders with the same
customer name, while my test expected only one.

I realized that the test was using the same
customer name on every execution.

### What I changed

I updated the test to generate a unique customer
name every time it runs.

This helps prevent the test from matching orders
created during previous executions.


### Actual result

The test initially failed when I ran it again
because it found two orders with the same customer name.

I updated the test to generate a unique customer name
for every execution.

After making this change, I ran the full test suite
three times. Both automated tests passed each time.

### Result

PASS - Verified on 27 November 2026.

### Test execution summary

Total automated tests: 2
Passed: 2
Failed: 0

Repeated full suite runs: 3
Successful runs: 3

### What I learned

I learned that an automated test can fail because
of the way the test is written, even when the
application is working correctly.

I also learned how to read an assertion error,
investigate the cause, and improve the test
so it can run repeatedly.


## AUTO-003 - Verify saved order using SQL

### What I wanted to check

I wanted to make sure that information entered through the OrderSprout website was correctly saved in the database.

### How I tested it

I used Playwright to create a new order for a chocolate cake.

Then I connected to the temporary SQLite test database using Python and ran an SQL query to find that order.

I checked the saved customer name, item, total amount, paid amount and order status.

### Test data

- Customer: Unique SQL test customer
- Item: Chocolate cake
- Total: €80.00
- Paid: €20.00
- Status: New

### Expected result

The database should contain the new order with the correct information.

### Actual result

The order was found in the test database, and all the checked values matched the expected results.

### Result

**PASS — 28 November 2026**

The SQL test passed individually, and the complete three-test suite also passed.

### Issue encountered

During the first complete test run, the homepage test failed because it tried to access port 5001 instead of the test server on port 5002.

I corrected the port number and ran the complete suite again. All three tests passed.

### What I learned

I learned how to use SQL to read information from a database and how to use Python assertions to check saved data.

I also learned how to investigate a connection error and correct the test configuration.

### Limitation

The tests currently require a locally running OrderSprout server and a matching test database path. Automatic setup and cleanup are planned.