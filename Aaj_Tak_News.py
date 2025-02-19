from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Open the news website (Example: Aaj Tak)
driver.get("https://www.aajtak.in/")
time.sleep(2)  # Wait for page to load

# Extract news headlines and links using XPath
news_data = []
headlines = driver.find_elements(By.XPATH, "//a[contains(@class, 'news-title')]")  # Adjust XPath as needed

for headline in headlines:
    title = headline.text.strip()
    link = headline.get_attribute("href")
    
    if title and link:  # Avoid empty values
        news_data.append({"Title": title, "Link": link})

# Convert to DataFrame
df = pd.DataFrame(news_data)

# Save to CSV file
df.to_csv("aajtak_news.csv", index=False)

# Close the browser
driver.quit()

print("News saved successfully!")
