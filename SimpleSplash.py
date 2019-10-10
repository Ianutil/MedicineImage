#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
'''
var ele=documen.getElementById('ele');//先获取元素对象，再绑定onclick事件
ele.onclick=function(){
    alert('这是onclick事件');
};
'''
# js控制浏览器滚动到底部js
js = """
function scrollToBottom() {
    var Height = document.body.clientHeight,  //文本高度
        screenHeight = window.innerHeight,  //屏幕高度
        INTERVAL = 100,  // 滚动动作之间的间隔时间
        delta = 500,  //每次滚动距离
        curScrollTop = 0;    //当前window.scrollTop 值
    console.info(Height)
    var scroll = function () {
        //curScrollTop = document.body.scrollTop;
        curScrollTop = curScrollTop + delta;
        window.scrollTo(0,curScrollTop);
        console.info("偏移量:"+delta)
        console.info("当前位置:"+curScrollTop)
    };
    var timer = setInterval(function () {
        var curHeight = curScrollTop + screenHeight;
        if (curHeight >= Height){   //滚动到页面底部时，结束滚动
            clearInterval(timer);
        }
        scroll();
    }, INTERVAL)
};
scrollToBottom()
"""


search_js = """
function getElementsClass(classnames){
    var classobj = new Array(); // 定义数组
    var classint = 0; // 定义数组的下标
    var tags = document.getElementsByTagName("*"); // 获取HTML的所有标签
    for (var i in tags){// 对标签进行遍历
        if (tags[i].nodeType == 1){// 判断节点类型
            if (tags[i].getAttribute("class") == classnames) { // 判断和需要CLASS名字相同的，并组成一个数组
                classobj[classint]=tags[i];
                classint++;
            }
        }
    }
    return classobj; // 返回组成的数组
}

$("#combobox-placeholder").attr("value","值1234");
$("#word").attr("value","值1234");

function searchBtn() {
    //var e = document.createEvent("MouseEvents");
    //e.initEvent("search", true, true);　
    btn = getElementsClass("searchBtn");
    //btn.dispatchEvent(e);
    //btn.onclick();
    
    search();
};
searchBtn()

"""

def test_spider(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    # 指定谷歌浏览器路径
    # webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
    webdriver.Chrome(chrome_options=chrome_options)

    driver = webdriver.Chrome()
    driver.get(url)

    # 执行js滚动浏览器窗口到底部
    driver.execute_script(search_js)
    # driver.execute_script(js)
    # time.sleep(5)  # 不加载图片的话，这个时间可以不要，等待JS执行
    content = driver.page_source.encode('utf-8')
    driver.find_element_by_class_name("combobox-placeholder").__setattr__("value", "****************")
    # driver.find_element_by_class_name("searchBtn").click()



    time.sleep(10)

    driver.close()
    driver.quit()
    print(str(content, "utf-8"))
    return content

    # soup = BeautifulSoup(driver.page_source, "lxml")
    # for img_tag in soup.body.seltect("img[src]"):
    #     url = img_tag.attr["src"]
    #     print(url)

if __name__ == "__main__":
    print("Hello World")
    # url = "https://www.111.com.cn/search/search.action?keyWord=%25E5%25B8%2583%25E6%25B4%259B%25E8%258A%25AC%25E7%25BC%2593%25E9%2587%258A%25E8%2583%25B6%25E5%259B%258A(%25E8%258A%25AC%25E5%25BF%2585%25E5%25BE%2597)"
    url = "https://www.111.com.cn"
    # url = "https://search.jd.com/Search?keyword=%E6%A0%BC%E5%88%97%E7%BE%8E%E8%84%B2%E7%89%87(%E5%A4%84%E6%96%B9%E8%8D%AF)&enc=utf-8&wq=%E6%A0%BC%E5%88%97%E7%BE%8E%E8%84%B2%E7%89%87(%E5%A4%84%E6%96%B9%E8%8D%AF)&pvid=e594be63471b41b2a6821999b9c2e65a"
    test_spider(url)