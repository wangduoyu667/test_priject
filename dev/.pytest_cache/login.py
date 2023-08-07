from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://10.160.152.222/")
    page.goto("http://10.160.152.222/login")
    page.get_by_role("tab", name="外部合作商").click()
    page.get_by_placeholder("请输入用户名称").click()
    page.get_by_placeholder("请输入用户名称").fill("wanghuimin")
    page.get_by_placeholder("请输入登录密码").click()
    page.get_by_placeholder("请输入登录密码").click()
    page.get_by_placeholder("请输入登录密码").fill("Ux&9=%SwutS3")
    page.get_by_role("button", name="立即登录").click()
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
