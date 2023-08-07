from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://10.160.152.222/home')
    # 进行更多的页面操作和断言
    print(page.title())
    page.screenshot(path=f'example-{p.firefox.name}.png')
    #page.pause()#断点
    browser.close()
