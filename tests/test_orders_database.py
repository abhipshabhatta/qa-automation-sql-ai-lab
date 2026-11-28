
import os
import sqlite3
from uuid import uuid4

from playwright.sync_api import Page, expect


def test_order_saved_in_database(page: Page):
    # Create a unique name for this test order
    customer = f"SQL Test Customer {uuid4().hex[:8]}"

    # Find the database used by our test server
    database_path = os.environ.get("TEST_DB_PATH")
    assert database_path, "TEST_DB_PATH is missing"

    # Open OrderSprout and create a new order
    page.goto("http://127.0.0.1:5002/orders/new")

    page.locator("#customer").fill(customer)
    page.locator("#item").fill("Chocolate cake")
    page.locator("#delivery_date").fill("2026-12-20")
    page.locator("#status").select_option("New")
    page.locator("#total").fill("80.00")
    page.locator("#paid").fill("20.00")

    page.get_by_role("button", name="Save order").click()

    # Check that the application returns to the homepage
    expect(page).to_have_url("http://127.0.0.1:5002/")

    # Open the SQLite database and find our new order
    connection = sqlite3.connect(database_path)

    try:
        order = connection.execute(
            """
            SELECT customer, item, total_cents, paid_cents, status
            FROM orders
            WHERE customer = ?
            """,
            (customer,),
        ).fetchone()

    finally:
        connection.close()

    # Check that the order was saved
    assert order is not None, "Order was not found in the database"

    # Check the information stored in SQLite
    assert order[0] == customer
    assert order[1] == "Chocolate cake"
    assert order[2] == 8000
    assert order[3] == 2000
    assert order[4] == "New"
