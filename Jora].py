from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def setup_driver():
    options = Options()
    # options.add_argument('--headless')  # Uncomment to run headless
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_jobs():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)
    url = "https://nz.jora.com/j?sp=search&trigger_source=serp&a=30d&q=General+Practitioner+%28GP%29&l="
    driver.get(url)
    
    time.sleep(5)  # Allow page to load completely
    
    job_data = []
    current_page = 1
    max_pages = 45  # Set maximum number of pages to scrape
    visited_urls = set()
    
    while current_page <= max_pages:
        try:
            current_url = driver.current_url
            if current_url in visited_urls:
                print("Loop detected, stopping...")
                break
            visited_urls.add(current_url)
            
            job_elements = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'r_')]")
            
            for job in job_elements:
                try:
                    title_element = job.find_element(By.CSS_SELECTOR, "h2.job-title a")
                    title = title_element.text.strip()
                    job_link = title_element.get_attribute("href")
                    
                    company = job.find_element(By.CSS_SELECTOR, "span.job-company").text.strip()
                    location = job.find_element(By.CSS_SELECTOR, "a.job-location").text.strip()
                    posted_date = job.find_element(By.CSS_SELECTOR, "span.job-listed-date").text.strip()
                    platform = job.find_element(By.XPATH, "//*[@id='job-meta']/span[2]").text.strip()
                    
                    profession = "General Practitioner (GP)"
                    
                    job_data.append({
                        "Title": title,
                        "Profession": profession,
                        "Posted Date": posted_date,
                        "Location": location,
                        "Company": company,
                        "Job Link": job_link,
                        "Platform": platform
                    })
                except Exception as e:
                    print(f"Error extracting data for a job: {e}")
            
            # Locate the next page button and click it
            try:
                next_page = driver.find_element(By.XPATH, "//*[@id='jobresults']/div[18]/a[5]")
                if "disabled" in next_page.get_attribute("class"):
                    break  # Stop if there is no next page
                next_page.click()
                time.sleep(5)  # Wait for the next page to load
                current_page += 1
            except Exception as e:
                print("No more pages to navigate.")
                break
        except Exception as e:
            print(f"Error finding job elements: {e}")
            break
    
    driver.quit()
    return job_data

if __name__ == "__main__":
    jobs = scrape_jobs()
    df = pd.DataFrame(jobs)
    print(df)
    df.to_csv("jora_jobs.csv", index=False)
