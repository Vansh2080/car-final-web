
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));
  page.on('pageerror', err => console.log('BROWSER ERROR:', err.message));
  await page.goto('file:///C:/Users/admin/Documents/final car model - Copy (3)/index.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);
  const bodyText = await page.evaluate(() => document.body.innerText);
  console.log('BODY:', bodyText.substring(0, 500));
  const introState = await page.evaluate(() => typeof introState !== 'undefined' ? introState : 'undefined');
  console.log('introState:', introState);
  await browser.close();
})();

