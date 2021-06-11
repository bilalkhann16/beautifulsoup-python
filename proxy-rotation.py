from fp.fp import FreeProxy
import requests

#proxy = FreeProxy(country_id=['US'], rand  = True).get()
proxy = FreeProxy(rand=True).get()
proxies = {
    'http': proxy,
    'https': proxy
}
res = requests.get('https://httpbin.org/ip',proxies = proxies)
print(res.json())
