#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/16 0:10
# @Author  : CherryWh1te
# @Site    : www.mozac.tech
# @File    : sometest.py
# @Software: PyCharm
import requests
import urllib.parse

# 定义URL
url = "https://minekuai.com/sanctum/csrf-cookie"

# 定义请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "minekuai.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 提取cookie并保存到字典
cookies = response.cookies.get_dict()

# 输出结果
print("Status Code:", response.status_code)
print("Cookies:", cookies)

# # 定义新的POST请求
# post_url = "https://minekuai.com/auth/login"
# post_headers = {
#     "Accept": "application/json",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
#     "Connection": "keep-alive",
#     "Content-Type": "application/json",
#     "Host": "minekuai.com",
#     "Origin": "https://minekuai.com",
#     "Referer": "https://minekuai.com/auth/login",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "X-Requested-With": "XMLHttpRequest",
#     "X-XSRF-TOKEN": urllib.parse.unquote(cookies.get("XSRF-TOKEN", ""))
# }
#
# # POST请求体
# post_data = {}
#
# # 发送POST请求
# post_response = requests.post(post_url, headers=post_headers, json=post_data, cookies=cookies)
#
# # 输出POST响应
# print("POST Status Code:", post_response.status_code)
# print("POST Response Body:", post_response.cookies)

# 定义新的POST请求
post_url = "https://api.ungc.com.cn/api/minekuai/points/signIn"
post_headers = {
    "accept": "application/json",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
    "content-type": "application/json",
    "origin": "https://minekuai.com",
    "priority": "u=1, i",
    "referer": "https://minekuai.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": urllib.parse.unquote(cookies.get("XSRF-TOKEN", ""))
}

# POST请求体
post_data = {
    "data": "2161"
}

# 发送POST请求
post_response = requests.post(post_url, headers=post_headers, cookies=cookies, data="2161")

# 输出POST响应
print("POST Status Code:", post_response.status_code)
print("POST Response Body:", post_response.json())

# 发送POST请求
post_response = requests.post(post_url, headers=post_headers, cookies=cookies, data="2394")

# 输出POST响应
print("POST Status Code:", post_response.status_code)
print("POST Response Body:", post_response.json())
