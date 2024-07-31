import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # 选择一个浏览器引擎，这里使用 Chromium
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # 导航到目标网站
        await page.goto('https://example.com')

        # 等待页面加载完成
        await page.wait_for_load_state('networkidle')

        # 提取页面上的所有标题
        titles = await page.query_selector_all('h1')
        for title in titles:
            print(await page.evaluate('(element) => element.textContent', title))

        # 关闭浏览器
        await browser.close()

asyncio.run(main())

'''
if __name__ == 'main':
    pass
'''