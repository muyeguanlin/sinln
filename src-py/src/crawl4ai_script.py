import asyncio
from crawl4ai import AsyncWebCrawler
# 这里以伪代码示意，你需要安装对应AI库
# from openai import OpenAI 

async def main():
    async with AsyncWebCrawler() as crawler:
        # 获取网页的Markdown文本
        result = await crawler.arun(url="https://example.com")
        webpage_markdown = result.markdown
        
        # 将Markdown文本和你的指令一起发送给LLM
        prompt = f"""
        请根据以下网页内容执行提取任务：
        
        {webpage_markdown}
        
        ---
        提取要求：从上面的内容中提取新闻的标题、链接、所属板块和发布时间。
        输出格式：一个JSON列表，每个元素是字典，包含键: title, time, topic, url。
        注意：如果某项信息没找到，就留空字符串。
        """
        # 此处调用你选择的LLM API
        # extracted_data = call_llm_api(prompt)
        # print(extracted_data)

asyncio.run(main())
        print(result.extractions) # 获取LLM提取的结构化数据

# asyncio.run(main())
# import asyncio
# from crawl4ai import AsyncWebCrawler

# async def crawl_baidu():
#     async with AsyncWebCrawler(verbose=True) as crawler:
#         result = await crawler.arun(
#             # url="https://www.baidu.com/s?wd=冬装",
#             url="https://www.1688.com/zw/page.html?hpageId=old-sem-pc-list&scene=2&keywords=%E5%86%AC%E8%A3%85&cosite=gdtsogoujj&format=normal&location=landing_t4&m_kw=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4%E7%BD%91&m_k=54712074865&m_r=labknt34c7szg&m_c=26613419839&m_ac=25379785&m_a=26613418796&m_p=26613171477&m_clk=4iisc2icaaajzozff7lq&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA&p_rs=true&exp=pcSemFumian%3AC%3Bqztf%3AF%3BpcSemWwClick%3AA%3BpcSemDownloadPlugin%3AA%3Basst%3AF&ptid=017700000006aaa2069a06656e36f14d&spm=a312h.2018_new_sem.dh_004.submit",
#             css_selector=".result", # 示例选择器，请根据实际页面结构调整
#             bypass_cache=True
#         )
#         # 打印Markdown格式的清理后内容
#         print(result.markdown)
#         # 或者打印原始的HTML内容
#         # print(result.html)

# if __name__ == "__main__":
#     asyncio.run(crawl_baidu())