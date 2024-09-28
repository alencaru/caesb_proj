import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'args': ['--no-sandbox']}) #launch()
    page = await browser.newPage()
    await page.goto('https://hellhades.com/raid/champions/archmage-hellmut/')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())