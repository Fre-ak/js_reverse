# Install the Python Requests library:
# `pip install requests`

import requests
import time

from Crypto.Cipher import DES3
import base64
import execjs

ctx = execjs.compile(open("./t.js").read())


class EncryptDate:
    def __init__(self, key):
        self.key = key  # 初始化密钥
        self.iv = b"01234567"  # 偏移量
        self.length = DES3.block_size  # 初始化数据块大小
        self.des3 = DES3.new(self.key, DES3.MODE_ECB)  # 初始化AES,CBC模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0 : -ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode("utf-8"))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数

        res = self.des3.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        # msg =  res.hex()
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        # res = bytes.fromhex(decrData)
        msg = self.des3.decrypt(res).decode("utf8")
        return self.unpad(msg)


def send_request():
    # cURL
    # GET https://m.ctyun.cn/account/login
    userName = ""
    password = ""

    k = ctx.call("F", userName)
    print(k)

    e = EncryptDate(k)
    password = e.encrypt(password)

    comParam_curTime = int(time.time())

    comParam_seqCode = ctx.call("getSeqCode")

    comParam_signature = ctx.call("getSignature", comParam_curTime, comParam_seqCode)

    try:
        response = requests.get(
            url="https://m.ctyun.cn/account/login",
            params={
                "userName": userName,
                "password": password,
                "referrer": "wap",
                "mainVersion": "300021100",
                "comParam_curTime": comParam_curTime,
                "comParam_seqCode": comParam_seqCode,
                "comParam_signature": comParam_signature,
                "isCheck": "true",
                "locale": "zh-cn",
            },
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Referer": "https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Accept-Encoding": "gzip",
            },
        )
        print(
            "Response HTTP Status Code: {status_code}".format(
                status_code=response.status_code
            )
        )
        print("Response HTTP Response Body: {content}".format(content=response.text))
    except requests.exceptions.RequestException:
        print("HTTP Request failed")


send_request()
