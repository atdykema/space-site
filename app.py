

from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
# import asyncio
app = Flask(__name__)


@app.route("/")
def index():

    return render_template("fetching.html", var="home")


@app.route("/home")
def home():

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Firefox(executable_path="geckodriver", options=options)

    driver.get('https://www.jwst.nasa.gov/content/webbLaunch/news.html')

    not_found = True
    while not_found:
        try:
            posts = driver.find_element(By.ID, "ssdNewsFeed").find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')
            not_found = False
        except Exception as e:
            pass
    
    print(posts)
    post_info = []
    for post in posts[:5]:
        not_found = True
        while not_found:
            try:
                date = post.find_element(By.TAG_NAME, 'span')
                link = post.find_element(By.TAG_NAME, 'a')
                post_info.append({'news_date' : date.text, 'news_href' : link.get_attribute('href'), 'news_title' : link.text})
                not_found = False
            except Exception as e:
                pass
    
    link = None
    is_not_complete = True
    while is_not_complete:
        try:
            driver.get('https://www.flickr.com/photos/nasawebbtelescope/albums')

    #         # print(driver.title)

            container = driver.find_element(By.CLASS_NAME, 'photo-list-view')

    #       print(container.get_attribute('class'))

            posts = container.find_elements(By.CLASS_NAME, 'photo-list-album-view')

            # print(len(posts))

            latest_album = posts[1]

            link = latest_album.find_element(By.CLASS_NAME, 'interaction-view').get_attribute('href')

             # print(link.get_attribute('href'))

            is_not_complete = False
        except:
            pass
    
    driver.close()

    driver.quit()

    return render_template("index.html", news=post_info, link=link)

@app.route("/fetching_images")
def fetching():

    return render_template("fetching.html", var="latest_images")


# @app.route("/latest_images")
# async def latest_images():
    

#     # async def get_image_list(input, output):
#     #     not_found = True
#     #     while not_found:
#     #         try:
#     #             ele = input.find_element(By.CLASS_NAME, 'overlay')
#     #             output.append({'src':ele.get_attribute('href'),'caption':ele.get_attribute('aria-label')})
#     #             not_found = False
#     #         except Exception as e:
#     #             pass

#     # async def get_image_list_final(driver, input, output):
#     #     stale_ele = True
#     #     while stale_ele:
#     #         try:
#     #             driver.get(input['src'])
#     #             input['src'] = driver.find_element(By.CLASS_NAME, 'main-photo').get_attribute('src')
#     #             output.append(input)
#     #             print(input['src'])
#     #             stale_ele = False
#     #         except Exception as e:
#     #             pass
    
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

#     options = webdriver.FirefoxOptions()
#     options.headless = True
#     options.add_argument(f'user-agent={user_agent}')
#     driver = webdriver.Firefox(executable_path="geckodriver", options=options)

#     is_not_complete = True
#     while is_not_complete:
#         try:
#             driver.get('https://www.flickr.com/photos/nasawebbtelescope/albums')

#     #         # print(driver.title)

#             container = driver.find_element(By.CLASS_NAME, 'photo-list-view')

#     #       print(container.get_attribute('class'))

#             posts = container.find_elements(By.CLASS_NAME, 'photo-list-album-view')

#             # print(len(posts))

#             latest_album = posts[1]

#             link = latest_album.find_element(By.CLASS_NAME, 'interaction-view')

#              # print(link.get_attribute('href'))

#             driver.get(link.get_attribute('href'))
#             is_not_complete = False
#         except:
#             pass

    #         # print(driver.title)

    #         images = driver.find_element(By.CLASS_NAME, 'photo-list-view')

    #         image_list = images.find_elements(By.CLASS_NAME, 'photo-list-photo-view')

    #         is_not_complete = False
    #     except Exception as e:
    #         return render_template('err_page.html', err=e)

    # amt_of_imgs = len(image_list)

    # for _ in range(amt_of_imgs):
    #     await asyncio.gather(get_image_list(image_list.pop(0), image_list))

    # for _ in range(amt_of_imgs):
    #     await asyncio.gather(get_image_list_final(driver, image_list.pop(0), image_list))

    #driver.close()

    #driver.quit()
    
    #return render_template("latest_images.html", imgs=image_list)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)