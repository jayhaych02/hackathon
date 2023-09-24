import re
import requests
import json
from bs4 import BeautifulSoup


# Define the base URL and user agent
base_url = "https://water.phila.gov/projects/"
user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
)
header = {
    "User-Agent": user_agent
}

# Send an HTTP GET request to the webpage
url = "https://water.phila.gov/projects/phase/construction/"
response = requests.get(url, headers=header)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")


neighborhood_paragraphs = soup.find_all("h3", class_="post-title")

# Initialize a list to store unique project URLs
unique_urls_construction = []
# Iterate through project titles to extract and store the unique URLs
for title in neighborhood_paragraphs:
    # Find the link (<a>) element within the project title
    project_link = title.find("a")
    if project_link:
        project_url = project_link.get("href")
        unique_urls_construction.append(project_url)


# Now we have a list of the unique URLs of each construction project

streets = []
for x in unique_urls_construction:
  response = requests.get(x,headers = header)
  soup = BeautifulSoup(response.content,"html.parser")
  streets_affected_heading = soup.find("h4", string="Streets Affected")

  if streets_affected_heading:
      # Find the next <ul> element which contains the list of streets
      ul_element = streets_affected_heading.find_next("ul")

      # Extract the list of streets as text
      streets_list = [li.text.strip() for li in ul_element.find_all("li")]

      # Print the project URL followed by the list of streets affected
      print("Project URL:", x)
      print("Streets Affected:", ", ".join(streets_list))  # Join the list with commas
      streets.append(streets_list)
      print()  # Print a blank line for separation





















