import requests
import time

def measure_website_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time

print(measure_website_load_time("https://www.google.com/"))
print(measure_website_load_time("https://www.ynet.co.il/"))
print(measure_website_load_time("https://www.imdb.com/"))

# 0.419283390045166
# 0.639101505279541
# 0.5469121932983398