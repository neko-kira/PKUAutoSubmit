import requests
url = "https://sc.ftqq.com/"+str(sckey)+".send?text=自动备案失败"
response = requests.get(url).text
print(response)
