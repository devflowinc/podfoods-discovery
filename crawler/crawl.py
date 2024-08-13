"""This is a Selenium Web Scraper for the website https://podfoods.co/.

The purpose is to conduct user testing on the search.
"""

import os
import json
import time
import logging
import random
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.chrome.options import Options


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='scraper.log',
    filemode='w'
)

def initialize_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    return webdriver.Chrome(options=chrome_options)


def navigate_to_page(driver, url):
    driver.get(url)
    logging.info(f"Navigated to URL: {url}")
    print(f"Navigated to URL: {url}")


def extract_page(driver, url):
    try:
        # Wait for the main content to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.pf-break-word'))
        )

        product_info = driver.execute_script("""
        function extractProductInfo() {
            const productInfo = {};

            // Extract breadcrumb
            productInfo.breadcrumb = Array.from(document.querySelectorAll('.el-breadcrumb__item'))
                .map(item => item.textContent.trim())
                .filter(text => text !== '/');

            // Extract product name
            productInfo.name = document.querySelector('h1.pf-break-word').textContent.trim();

            // Extract brand name and location
            const brandElement = document.querySelector('a.brand');
            productInfo.brand = {
                name: brandElement.querySelector('.name').textContent.trim(),
                location: brandElement.querySelector('.address').textContent.trim()
            };

            // Extract UPC
            productInfo.upc = document.querySelector('.upc-number').textContent.trim();

           // Extract case pack
            productInfo.casePack = document.querySelector('dd[data-v-df46d3ca]:nth-of-type(2)').textContent.trim();

            // Extract additional details
            const detailsElement = document.querySelector('#pane-detail .metas');
            productInfo.details = {};
            const dts = detailsElement.querySelectorAll('dt');
            dts.forEach(dt => {
                const key = dt.textContent.trim();
                const value = dt.nextElementSibling.textContent.trim();
                productInfo.details[key] = value;
            });

            // Extract product qualities
            productInfo.qualities = Array.from(document.querySelectorAll('.product-qualities li'))
                .map(li => li.textContent.trim());

            // Extract ingredients
            productInfo.ingredients = document.querySelector('.ingredients .content').textContent.trim();

            // Extract description
            productInfo.description = document.querySelector('.description').textContent.trim();

            // Extract nutrition label URLs
            productInfo.nutritionLabels = Array.from(document.querySelectorAll('.nutrition-images-swiper .swiper-slide .contain'))
                .map(div => div.style.backgroundImage.match(/url\((.*?)\)/)[1]);

            return productInfo;
        }
        return extractProductInfo();
        """)

        product_info['url'] = url
    
        product_info['nuxt'] = driver.execute_script("""
        return JSON.stringify(window.__NUXT__);
        """)

        # Validate the product information
        if not product_info:
            logging.error(f"No product information extracted for URL: {url}")
            print(f"No product information extracted for URL: {url}")
            return

        # Save the extracted information
        with open('pages.json', 'r+') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            
            data.append(product_info)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

        logging.info(f"Extracted and saved information for URL: {url}")
        # print(f"Extracted and saved information for URL: {url}")
        

    except Exception as e:
        logging.error(f"Error extracting information from {url}: {str(e)}")
        print(f"Error extracting information from {url}: {str(e)}")
        exit()


def main():
    driver = initialize_driver()

    with open('products.json', 'r') as file:
        products = json.load(file)
    urls = [product['href'] for product in products if 'href' in product]

    extracted_urls = [page['url'] for page in json.load(open('pages.json', 'r'))]
    total_urls = len(urls)
    extracted_count = len(extracted_urls)
    percentage = (extracted_count / total_urls) * 100 if total_urls > 0 else 0
    
    print(f"Percentage of URLs already extracted: {percentage:.2f}%")

    total_urls = len(urls)
    for index, url in enumerate(urls, 1):
        if url in extracted_urls:
            continue
        navigate_to_page(driver, url)
        extract_page(driver, url)
        progress = (index / total_urls) * 100
        print(f"Progress: {progress:.2f}% ({index}/{total_urls} URLs processed)")


    driver.quit()

if __name__ == "__main__":
    main()