
# QA Automation, SQL & AI Lab

A practical software quality assurance portfolio project
developed while studying Computer Science at EPITA.

## Project Objectives

- Automate web application testing with Python and Playwright
- Learn SQL database validation using SQLite
- Explore AI-assisted test design and review
- Practice Git, GitHub, and CI/CD workflows

## Application Under Test

OrderSprout, a personal Flask order-management web application.

The application and QA testing project are maintained
in separate repositories.

## Technologies

- Python
- Playwright
- Pytest
- SQLite (planned)
- Git and GitHub

## Automated Tests

### Homepage Smoke Test

File: tests/test_orders_ui.py

Checks:
- The homepage returns HTTP status 200.
- The webpage body is visible.

Test result: PASSED locally using Chromium on 25 November 2026.

## Running Tests Locally

Start the OrderSprout application separately
on http://127.0.0.1:5001.

Install the QA project's dependencies:

    python -m pip install -r requirements.txt
    python -m playwright install chromium

Execute:

    python -m pytest tests/ -v --headed

## Current Status

Work in progress.

Next milestone: automate creating an order using
an isolated SQLite test database.

## Notes

Automated tests currently require OrderSprout
to be running locally.

SQL validation and AI-assisted testing will be
implemented in future feature branches.
