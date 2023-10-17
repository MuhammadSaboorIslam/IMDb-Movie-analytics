from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

def search(query):
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--blink-settings=imagesEnabled=false'")  # Disable image loading
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.imdb.com/find/?q={query}&s=tt&exact=true&ref_=fn_tt_ex")
    movies_list = driver.find_elements(By.XPATH , "//a[@class='ipc-metadata-list-summary-item__t']")
    top_movie = movies_list[0]
    top_movie.click()
    page_source = driver.page_source
    beautifulSoup_source = BeautifulSoup(page_source, "html.parser")
    reviews = [i.text for i in beautifulSoup_source.find_all("span" ,class_="three-Elements")]
    if not reviews:
        reviews = [i.text for i in beautifulSoup_source.find_all("span" ,class_="less-than-three-Elements")]
    info_html = beautifulSoup_source.find("ul" ,class_="ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt")
    info = [i.text for i in info_html.find_all("li")]

    movie_properties = {
        'name': beautifulSoup_source.find("span", class_="fDTGTb").text,
        'genre': [i.text for i in beautifulSoup_source.find_all("a", class_="ipc-chip")],
        'release_year': info[0] if info[0] != "TV Series" else info[1],
        'rated': info[1] if info[0] != "TV Series" else info[2],
        'length': info[2] if info[0] != "TV Series" else info[3],
        'seasons': beautifulSoup_source.find('label',class_="ipc-simple-select__label").text if info[0] == "TV Series" else None,
        'story': beautifulSoup_source.find("span", class_="kJJttH").text,
        "rating": beautifulSoup_source.find("span", class_="iZlgcd").text,
        'rater': beautifulSoup_source.find("div" ,class_="bjjENQ").text,
        'user_reviews': reviews[0],
        'critic_reviews': reviews[1],
        'meta_score': reviews[2] if len(reviews)>2 else None,
        'awards': beautifulSoup_source.find("span" ,class_="ipc-metadata-list-item__list-content-item").text if info[0] != "TV Series" else None,
        'link': driver.current_url,
        'trailer_link': "https://www.imdb.com/" + beautifulSoup_source.find('a', class_="ipc-lockup-overlay sc-e4a5af48-0 gOsOae ipc-focusable").get('href')
    }
    driver.quit()
    return movie_properties


