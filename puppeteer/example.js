const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({'headless': false, 'slowMo': 250});
  const page = await browser.newPage();
  await page.goto('https://www.gymstola.cz');
  await page.click('[title="Jídelníček"]');
  await page.screenshot({ path: 'example.png' });

  // await browser.close();
})();