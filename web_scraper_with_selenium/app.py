from selenium import webdriver
from pages.quotes_page import QuotesPage, InvalidTagForAuthorError


try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")

# chromedriver.webpage.chromium.org

    chrome = webdriver.Chrome(executable_path="path_to_web_driver_exe_downloaded")
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")
