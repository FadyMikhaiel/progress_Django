from django.http import JsonResponse
from selenium import webdriver
from bs4 import BeautifulSoup

def fetchData(request):
    url = 'http://10.0.2.2:4200/student/1'
    class_names = ['name', 'lecture', 'workshop']
    
    # Use Selenium to scrape data
    driver = webdriver.Chrome() 
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source
    driver.quit()

    # Parse HTML content
    soup = BeautifulSoup(html, 'html.parser')

    class_data_map = {}

    for class_name in class_names:
        elements = soup.find_all(class_=class_name)
        class_data = []
        for element in elements:
            class_data.append(element.text.strip())
        class_data_map[class_name] = class_data

    return JsonResponse(class_data_map)