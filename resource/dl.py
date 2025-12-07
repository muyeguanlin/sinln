from playwright.async_api import  async_playwright
import asyncio
import time
import os
import aiohttp


async def download_single_image(session, url, index,word_origin ):
        """异步下载单张图片"""
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    filename=f"{word_origin}_{index+1}.jpg"
                    local_path = f"images/{word_origin}_{index+1}.jpg"
                    with open(local_path, "wb") as f:
                        f.write(content)
                    # print(f"下载成功：{word_origin}_{index+1}.jpg")

                    return (filename, url, word_origin,local_path)
        except Exception as e:
            print(f"下载失败 {url}: {e}")




async def download(max_images):
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=False)
        con_text=await browser.new_context()
        page=await con_text.new_page()
        await page.goto("https://www.1688.com/zw/hamlet.html?scene=2&keywords=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4&cosite=bingjj&trackid=885235714308742809168995&format=normal&location=landing_t4&m_k=82533176094889&m_a=1320515787216775&m_p=519835145&m_clk=07f7ef37c6e5128c89798619180fd93f&m_c=82532463471873&m_q=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4&m_mt=be&m_ep=e&m_o=82533176094889&m_site=o&d27=c&m_cext=&m_aud=kwd-82533176094889:loc-39&msclkid=07f7ef37c6e5128c89798619180fd93f")

        word_origin = input("请输入搜索内容：")
        await page.fill("#alisearch-keywords", word_origin+"游泳", timeout=60000)
        await page.press('button[id="alisearch-submit"]', "Enter")
        time.sleep(10)

         #模拟滚动加载更多图片
        for _ in range(5):  # 滚动5次加载更多内容
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            # await page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(2000)  # 等待加载
            # await asyncio.sleep(2000)  # 异步等待
        await page.wait_for_selector("img[src]", timeout=6000)
        img_elements = await page.locator("img[src]").all()  # 创建定位器 locator 对动态页面更棒：page.locator() 不需要 await，但加上.all（）就是异步的
        img_urls =set()  # 使用集合去重

        while len(img_urls) < max_images:
            # a_elements = await page.query_selector_all("a[download]")
            # for img in a_elements:
            for img in img_elements:
                # url = await img.get_attribute("href")
                src = await img.get_attribute("src")         
                data_src = await img.get_attribute("data-src")
            # # 优先使用data-src（懒加载图片）
                url = data_src or src
                # print(url)
                if url and url.startswith("http"):
                    img_urls.add(url)
                



            await page.mouse.wheel(0, 1000)  # 异步滚动
            await asyncio.sleep(2)  # 异步等待
                        
            print(len(await page.query_selector_all("img[src]")))  # 检查实际有多少个 img 元素
            # self.logger.info(f"已获取 {len(img_urls)} 张图片")

        
        # 创建目录
        os.makedirs("images", exist_ok=True)
        # 异步下载图片
        downloaded_images = []
        async with aiohttp.ClientSession() as session:
            tasks = [download_single_image(session, url, i,word_origin) for i,url in enumerate(list(img_urls)[:max_images])]
            # tasks = []
            # for i, url in enumerate(list(img_urls)[:max_images]):
            #     tasks.append(download_single_image(session, url, i))
            
            results = await asyncio.gather(*tasks)  # 并发下载
            
            downloaded_images= [result for result in results if result is not None]
        

        await browser.close()
        # print(downloaded_images)
        return downloaded_images



asyncio.run(download(100))
