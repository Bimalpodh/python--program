# 1. Write a program that calculates the square of numbers [1,2,3,4,5,6,7,8,9,10]
# Use ThreadPoolExecutor with 3 workers.

from concurrent.futures import ThreadPoolExecutor
import requests
import os 
import time

# def sqr(num):
#   return num*num

# def creatIngThreadpool(li):
#   res=[]
#   with ThreadPoolExecutor(max_workers=3) as executor:
#     future=executor.map(sqr,li)
#     for r in future:
#       res.append(r)
#   return res
      

# try:
  
#   li=list(map(int,input("enter list item by separating ',' ").split(",")))
#   ans=creatIngThreadpool(li)
# except TypeError as e:
#   print(e)
# except ValueError as e:
#   print(e)
# else:
#   print(ans)
# finally:
#   print("keep it up ")
  
  
# task 2

# Given a list of URLs, use ThreadPool to download them in parallel.
# Print size of each downloaded content.
# Handle timeout if download takes more than 5 seconds.


from concurrent.futures import ThreadPoolExecutor
import requests
import os
import time

def downloadImage(url):
    try:
        response = requests.get(url, timeout=5)  # Added timeout
        sizeContainer = {url: len(response.content)}
        return sizeContainer
    except requests.exceptions.Timeout:
        return {url: "Timeout error!"}

def imagDownloadpool(ImageUrlList):
    all_results = []
    with ThreadPoolExecutor(max_workers=len(ImageUrlList)) as executor:
        results = executor.map(downloadImage, ImageUrlList)
        for res in results:
            for key, value in res.items():
                all_results.append(f"{key} --> {value} bytes")
    return all_results

try:
    li = list(map(str,input("Enter all the URLs separated by ',' : ").split(",")))
    result = imagDownloadpool(li)
except ValueError as e:
    print("Valid URL required")
except TypeError as e:
    print(e)
else:
    print(result)
finally:
    print("Keep it up!")
