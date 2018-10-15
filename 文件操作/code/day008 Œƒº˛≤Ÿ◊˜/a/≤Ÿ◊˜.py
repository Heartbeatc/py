import requests # 网络请求

rs = requests.get("http://pic.netbian.com/uploads/allimg/180906/180605-153622836527b2.jpg")
f = open("壁纸.jpg", mode="wb")
f.write(rs.content)
f.flush()
f.close()

