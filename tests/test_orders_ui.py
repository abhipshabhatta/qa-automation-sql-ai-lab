
from playwright.sync_api import Page, expect


def test_ordersprout_homepage(page: Page):
    # Open our local OrderSprout application
    response = page.goto("http://127.0.0.1:5002/")

    # Check that the server responded successfully
    assert response is not None
    assert response.status == 200

    # Check that the page contains visible content
    expect(page.locator("body")).to_be_visible()

