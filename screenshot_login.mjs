import { chromium } from 'playwright';
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  await page.goto('http://localhost:5173/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);
  await page.screenshot({ path: '/tmp/login_page.png', fullPage: true });
  console.log('Login screenshot saved');
  const btn = await page.locator('text=小熊').first();
  if (await btn.isVisible().catch(() => false)) {
    await btn.click();
    console.log('Clicked 小熊');
  } else {
    console.log('小熊 button not found');
  }
  await page.waitForTimeout(3000);
  await page.screenshot({ path: '/tmp/home_page.png', fullPage: true });
  console.log('Home screenshot saved');
  await browser.close();
})();
