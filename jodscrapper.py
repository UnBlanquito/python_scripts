import sys
from io import open
import requests
from bs4 import BeautifulSoup


def scrapping_seek():
    url = (
        "https://www.seek.com.au/python-jobs?salaryrange=40000-200000&salarytype=annual"
    )
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    def has_data_search(tag):
        return tag.has_attr("data-search-sol-meta")

    results = soup.find_all(has_data_search)
    try:
        file = open("archivo.txt", "a")
        for job in results:
            title_element = job.find("a", attrs={"data-automation": "jobTitle"})
            title = title_element.get_text()
            company = job.find("a", attrs={"data-automation": "jobCompany"}).get_text()
            job_link = "https://www.seek.co.nz" + title_element["href"]
            salary = job.find("span", attrs={"data-automation": "jobSalary"})
            salary = salary.get_text() if salary else "n/a"
            job = f"Title: {title}\nEnterprise: {company}\nLink: {job_link}\n"
            print(job)
            file.write(job + "\n")
        file.close()
    except Exception as e:
        print(e)
        sys.exit("Error, try again!")


if __name__ == "__main__":
    scrapping_seek()
