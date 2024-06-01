from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False, slow_mo=500)
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.basketball-reference.com/leagues/NBA_2023.html")

    cookie_button = page.get_by_text("AGREE", exact=True)
    cookie_button.click()

    page.locator("#advanced-team_sh").get_by_text("Share & Export").click()
    page.locator("#advanced-team_sh").get_by_role("button", name="Get table as CSV (for Excel)").click()

    csv_stuff = page.locator("#csv_advanced-team").text_content()

    substring = "--- When using SR data, please cite us and provide a link and/or a mention."

    result = csv_stuff.replace(substring, "")

    with open("src/assets/stats.txt", "w") as my_file:
        my_file.write(result)
    print("Bien executé!")
    browser.close()