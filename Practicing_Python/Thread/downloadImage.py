import os
from concurrent.futures import ThreadPoolExecutor
import requests

class NotImgUrlError(Exception):
  def __init__(self, url,msg="not a valid url"):
    self.url=url
    self.msg=msg
    super().__init__(self.msg)
  def __str__(self):
    return f"{self.url}:{self.msg}"

def downloadImg(url,index):
  try:
    response=requests.get(url,timeout=5,stream=True)
    # validate the image
    content_Type=response.headers.get('content-type','')
    if not content_Type.startswith('image/'):
      raise NotImgUrlError(url)

    #prepare directory to store
    folder="img"
    os.makedirs(folder,exist_ok=True)
    
    # save imaage with indexed name
    filename=f"image_{index}.{content_Type.split('/')[-1]}"
    filepath=os.path.join(folder,filename)
    
    with open(filepath,'wb') as f:
      for chunk in response.iter_content(1024):
        if chunk:
          f.write(chunk)
    
    return f" {url} saved as {filename}"
  except requests.exceptions.Timeout:
    return f"⏰ {url} -> Download timed out!"
  except NotImgUrlError as e:
    return f" ❌ {e}"
  except Exception as e:
    return f" x {url} -> unknown error: {str(e)}"
  

def downloadImgPool(imgUrlList):
  results=[]
  with ThreadPoolExecutor(max_workers=len(imgUrlList)) as executor:
    futures=[executor.submit(downloadImg,url.strip(),i) for i,url in enumerate(imgUrlList,start=1)]
    for future in futures:
      results.append(future.result())  # ✅ Call the result method

  return results

# main block
try:
  urls=input("enter image URL separate by comma:\n").split(",")
  results=downloadImgPool(urls)
except Exception as e:
    print("Error occurred:", e)
else:
    print("\nDownload Summary:")
    for res in results:
        print(res)
finally:
    print("\n📁 All done. Check 'downloaded_images' folder.")