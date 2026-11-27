
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

## Next steps

- Test creating an order.
- Use an isolated test database.
- Check saved orders using SQL.
```

<text color="secondary" size="sm">I've used 27 November 2026 as the summary date. If your latest execution happened on a different date, change that line to the actual execution date.</text>

This sounds like a beginner describing real work. It also doesn't exaggerate your skills.

## 4. Decide what to do with the HTML report

For this first milestone, let's keep the generated HTML report locally and publish your human-written summary to GitHub.

Why? Pytest's HTML report includes environment information, which can contain local paths and other details you might not want to publish without reviewing them.

Later, GitHub Actions will generate downloadable reports automatically, and we'll add links to those runs.

Open `.gitignore` and add this line at the bottom:

<CodeBlock language="gitignore"># Generated HTML reports
reports/