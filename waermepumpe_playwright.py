#!/usr/bin/env python3
"""
Use Playwright to open the heatpump page, enter the password in the JS prompt, and print the resulting HTML.

Usage:
  python waermepumpe_playwright.py --url http://192.168.178.120/Webserver/index.html --password 123

Install:
  pip install playwright
  python -m playwright install

This script runs headless by default. It waits for the password prompt element #password_prompt_input and #password_submit_button, fills and clicks, then waits for the Content section to be populated.
"""
import argparse
import asyncio


DEFAULT_URL = "http://192.168.178.120/Webserver/index.html"


async def run(url, password, headless=True, timeout=10000):
    from playwright.async_api import async_playwright, TimeoutError as PWTimeout

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        page = await browser.new_page()
        await page.goto(url)
        try:
            # wait for the password prompt input
            await page.wait_for_selector('#password_prompt_input', timeout=timeout)
            await page.fill('#password_prompt_input', password)
            await page.click('#password_submit_button')
            # click the "Informationen" nav item to show the information list
            try:
                await page.click("nav#Navigation >> text=Informationen", timeout=2000)
            except Exception:
                # fallback: click first nav link
                try:
                    await page.click('nav#Navigation a', timeout=2000)
                except Exception:
                    pass

            # wait for content section to be populated
            await page.wait_for_selector('#Content:not(:empty)', timeout=timeout)

            # extract structured data from tables inside #Content
            data = await page.evaluate('''() => {
                const out = {};
                const tables = Array.from(document.querySelectorAll('#Content table'));
                for (const table of tables) {
                    const th = table.querySelector('th');
                    const section = th ? th.innerText.trim() : 'unknown';
                    if (!out[section]) out[section] = {};
                    const rows = Array.from(table.querySelectorAll('tr'));
                    for (const tr of rows) {
                        const tds = Array.from(tr.querySelectorAll('td'));
                        if (tds.length < 2) continue;
                        const labelEl = tr.querySelector('.output_field_long') || tds[0];
                        const valueEl = tr.querySelector('.output_field') || tds[1];
                        if (!labelEl || !valueEl) continue;
                        const label = labelEl.innerText.trim();
                        const value = valueEl.innerText.trim();
                        if (label === '') continue;
                        if (Object.prototype.hasOwnProperty.call(out[section], label)) {
                            const prev = out[section][label];
                            if (Array.isArray(prev)) {
                                prev.push(value);
                            } else {
                                out[section][label] = [prev, value];
                            }
                        } else {
                            out[section][label] = value;
                        }
                    }
                }
                return out;
            }''')

            import json
            print(json.dumps(data, ensure_ascii=False, indent=2))
        except PWTimeout:
            # maybe the page loaded content directly after clicking; try to print current content
            print(await page.content())
        finally:
            await browser.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default=DEFAULT_URL)
    parser.add_argument('--password', required=True)
    parser.add_argument('--no-headless', dest='headless', action='store_false')
    args = parser.parse_args()

    asyncio.run(run(args.url, args.password, headless=args.headless))


if __name__ == '__main__':
    main()
