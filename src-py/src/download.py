####playwright 爬虫
import os
import aiohttp
import asyncio
from urllib import parse #用perse.quote 方法必须引入
from playwright.async_api import async_playwright

# import logging


class BaiduImageDownloader:
    # def __init__(self, download_dir: str = "images"):
       
    #     self.logger = logging.getLogger(__name__)
       



    async def download_single_image(self,session, url, index,word_origin ):
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
        
        


    async def download_images(self,word_origin,max_images=100):
        """
        异步下载图片
        :param max_images: 要下载的数量，默认100张
        """
        async with async_playwright() as p:        
            # browser = await p.chromium.launch(headless=False)
            browser = await p.chromium.launch(headless=True)
            # page = await browser.new_page()#简单场景

            context = await browser.new_context()
            page = await context.new_page()

            # await page.goto("https://www.pexels.com/zh-cn/search/鲜花/",timeout=60000)
            # word_origin = input("请输入搜索内容：")
            # word = parse.quote(word_origin)
            # http_url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="+word
            # print(word)
            # await page.goto(http_url,timeout=6000)

            # 访问百度图片
            await page.goto("https://image.baidu.com/")
            # await page.goto("https://www.taobao.com/wow/z/tbhome/pcsem/alimama?refpid=mm_2898300158_3078300397_115665800437&keyword=%E6%B7%98%E5%AE%9D&bc_fl_src=tbsite_T9W2LtnM&channelSrp=bingSomama&msclkid=a4a83b81eb3210d11c9d53fb57b8ebc7&clk1=940a383ff07244828296edc9876d50ab&upsId=940a383ff07244828296edc9876d50ab")

            print("已打开百度图片")

            # 输入搜索关键词
            # await page.fill("#image-search-input", word_origin)
            await page.fill('input[name="word"]', word_origin)
            # await page.fill('input[name="q"]', word_origin)
            await page.press("#image-search-input", "Enter")
            # await page.press('input[name="q"]', "Enter")
            await page.wait_for_load_state("networkidle")
            print("已提交搜索")

            # 模拟滚动加载更多图片
            for _ in range(5):  # 滚动5次加载更多内容
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                # await page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
                await page.wait_for_timeout(2000)  # 等待加载
                # await asyncio.sleep(2000)  # 异步等待


            # 接受 Cookie
            if await page.query_selector("button:has-text('接受所有')"): 
                await page.click("button:has-text('接受所有')")
            
            # # 等待图片加载
            await page.wait_for_selector("img[src]", timeout=6000)
            # img_elements = await page.query_selector_all("img[src]")
            img_elements = await page.locator("img[src]").all()  # 创建定位器 locator 对动态页面更棒：page.locator() 不需要 await，但加上.all（）就是异步的
            # a_elements = await page.query_selector_all("img[src]")

            # if img_elements:
            #     print("悬浮在第一张图片上...")
            #     await img_elements[0].hover()  # 悬停触发下载按钮
            
            # await page.wait_for_selector("a[download]")

            scroll_pause_time = 2  # 滚动等待时间
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
                await asyncio.sleep(scroll_pause_time)  # 异步等待
                            
                print(len(await page.query_selector_all("img[src]")))  # 检查实际有多少个 img 元素
                # self.logger.info(f"已获取 {len(img_urls)} 张图片")
    
            
            # 创建目录
            os.makedirs("images", exist_ok=True)

            # 异步下载图片
            downloaded_images = []
            async with aiohttp.ClientSession() as session:
                tasks = [self.download_single_image(session, url, i,word_origin) for i,url in enumerate(list(img_urls)[:max_images])]
                # tasks = []
                # for i, url in enumerate(list(img_urls)[:max_images]):
                #     tasks.append(download_single_image(session, url, i))
                
                results = await asyncio.gather(*tasks)  # 并发下载
              
                downloaded_images= [result for result in results if result is not None]
           

            await browser.close()
            # print(downloaded_images)
            return downloaded_images
            # print(tasks)


if __name__ == "__main__":
    downloader=BaiduImageDownloader()
    word_origin = input("请输入搜索内容：")
    asyncio.run(downloader.download_images(word_origin,80))


