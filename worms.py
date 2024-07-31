import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # 选择一个浏览器引擎，这里使用 Chromium
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # 导航到目标网站
        await page.goto('https://select.pdgzf.com/login')

        # 等待页面加载完成
        await page.wait_for_load_state('networkidle')
        #输入账号
        await page.locator('//*[@id="loginhEAD"]/div[1]/div[2]/form/div[1]/div/div/input').fill('shuaibangguo')
        await page.locator('//*[@id="loginhEAD"]/div[1]/div[2]/form/div[2]/div/div/input').fill('shuai183493')
        await page.locator('//*[@id="loginhEAD"]/div[1]/div[2]/form/div[3]/div/img').screenshot(path='test.png')


        # 关闭浏览器
        await browser.close()

asyncio.run(main())

'''
if __name__ == 'main':
    pass
'''