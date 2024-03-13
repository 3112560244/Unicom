import datetime
import time
import pytz
import requests
import threading

# 设置时区为北京时间
tz = pytz.timezone('Asia/Shanghai')

# 获取当前时间
now = datetime.datetime.now(tz)

print(f"当前北京时间是: {now}")


def send_request(url, headers, data):
    start = datetime.datetime.now()
    response = requests.post(url, headers=headers, json=data)
    print(f"{start}---{datetime.datetime.now()}{response.json()}")


if __name__ == "__main__":
    url = "https://10010.woread.com.cn/ng_woread_service/rest/activity423/receiveActiveTask"
    headers = {
        "accesstoken": "ODZERTZCMjA1NTg1MTFFNDNFMThDRDYw",
    }
    data = {
        "sign": "NmE2MmQxZTlmYTQ0MjMzMzMzYmFhMWM1NzkxYmEyMWRmYmRkYjc5OTUxZjJiYjQ5NTgyMGEyODhmZmY5NjkzOTIxZDZmNDlkYzE0NjlkOTg2ODQ4YWM1MzMxMTU3Y2U0ZTg1MGQ0ODY2NzI1MWNkMWVlOWE2ZjEwYzk5MGNlMzYxZDhiMzAyODNhY2VkMTdjNjBhNjRiNzg5Mjc1ZmQ2YmU3NmY2NmIxNDdmZjNiYTQ3YWViZDliMjlhOGYzZWNhZDI3NTNhZTJkN2NjOTIzMzQ4Yzk0MTFiOWJkOWUwNDUxOTUyMmIzYTk2ZjI0YTBhOWUwOTIxYjFjYTIxMjUxYmJkZDk2MGRjMWRiYTE5MjUxZjQxYTIwZTExZWFkNDVhYWE5MDQ4ZWVjZWI3NTcxNDk4OTEwYTkxN2M0ZTM3MmY5OWY5ZjQ3NTcyZWE0OTkxOWVmZTQ2ZjAyODRhNmUyNWQ3MTg5ZjMwNmZkNGE0OGQ4MmQzMDJhYjdjMjI1YmI2"
    }
    # 获取当前时间
    now = datetime.datetime.now(tz)
    print(now)
    # 计算距离下一天零点的时间间隔
    next_day = now + datetime.timedelta(days=1)
    next_day = next_day.replace(hour=0, minute=0, second=0, microsecond=0)

    next_day = now
    next_day = next_day.replace(hour=23, minute=37, second=0, microsecond=0)

    delta = next_day - now
    # 计算时间间隔的秒数
    seconds = delta.total_seconds()
    print(seconds)
    # 设置定时器
    if seconds >= 1:
        time.sleep(seconds - 1.5)

    # 并发发送 10 个请求
    threads = []
    for _ in range(35):
        time.sleep(0.1)
        thread = threading.Thread(target=send_request, args=(url, headers, data))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()
