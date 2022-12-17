# 1 import modules
import requests
from bs4 import BeautifulSoup

job_titles = []
company_name = []
company_location = []
time_job = []
space = []
links = []
page_num = 0
# salary = []

while True:
    try:
        # 2 use requests to use the Url
        result = requests.get(f"https://wuzzuf.net/a/Healthcare-Medical-Jobs-in-Egypt?start={page_num}")

        # 3 save page content => markup of html
        src = result.content

        # 4 create soup object to parse content
        soup = BeautifulSoup(src, "lxml")

        # 5 find the elements containing info we need
        # job titles , link of job ,company_name , company_location , time_job

        job_titles = soup.find_all("h2", {"class": "css-m604qf"})
        company_name = soup.find_all("a", {"class": "css-17s97q8"})
        company_location = soup.find_all("span", {"class": "css-5wys0k"})
        time_job = soup.find_all("span", {"class": "css-1ve4b75 eoyjyou0"})

        # 6  loop returned lists to extract needed info into other lists
        for i in range(len(job_titles)):
            job_titles.append(print("JOB_TITLES : " + job_titles[i].text))
            links.append(print("LINK_JOB : " + job_titles[i].find("a").attrs['href']))
            company_name.append(print("COMPANY_NAMES : " + company_name[i].text))
            company_location.append(print("COMPANY_LOCATION : " + company_location[i].text))
            time_job.append(print("TIME_JOB : " + time_job[i].text))
            space.append(print("----------------------------------------------------------------------"))
        page_num += 1
        if page_num >= 12:
            break
    except:
        print("------------------------ERROR--------------------")
        break

""" 
# find salary in every job
for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    salaries = soup.find("span", {"class": "css-4xky9y"})
    salary.append(print("SALARY : " + salaries.text))
"""
