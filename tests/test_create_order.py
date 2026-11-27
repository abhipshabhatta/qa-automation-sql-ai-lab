
from uuid import uuid4

from playwright.sync_api import Page, expect


def test_create_order(page: Page):
    # Give this order a unique customer name
    customer = f"QA Customer {uuid4().hex[:8]}"

    # Open the New Order form
    page.goto("http://127.0.0.1:5002/orders/new")

    # Fill in the order details
    page.locator("#customer").fill(customer)
    page.locator("#item").fill("Birthday cake")
    page.locator("#delivery_date").fill("2026-12-15")
    page.locator("#status").select_option("New")
    page.locator("#total").fill("50.00")
    page.locator("#paid").fill("10.00")

    # Save the order
    page.get_by_role("button", name="Save order").click()

    # Check that we return to the homepage
    expect(page).to_have_url("http://127.0.0.1:5002/")

    # Find the order we just created
    order_row = page.locator("tbody tr").filter(
        has_text=customer
    )

    # Check the details in that order
    expect(order_row).to_have_count(1)
    expect(order_row).to_contain_text("Birthday cake")
    expect(order_row).to_contain_text("€50.00")
    expect(order_row).to_contain_text("€10.00")
    expect(order_row).to_contain_text("€40.00")
