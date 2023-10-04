import json
import time

import requests;
from bs4 import BeautifulSoup;
def getScholarData():
    try:
        url = "https://scholar.google.com/scholar?q=automotive+worker+well+being+&hl=en&as_sdt=0,5"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        scholar_results = []
        # select class name from all kinds of html tags
        # append data object into empty array
        for el in soup.select(".gs_ri"):
            scholar_results.append({
                "title": el.select(".gs_rt")[0].text,
                "title_link": el.select(".gs_rt a")[0]["href"],
                "id": el.select(".gs_rt a")[0]["id"],
                "displayed_link": el.select(".gs_a")[0].text,
                "snippet": el.select(".gs_rs")[0].text.replace("\n", ""),
                "cited_by_count": el.select(".gs_nph+ a")[0].text,
                "cited_link": "https://scholar.google.com" + el.select(".gs_nph+ a")[0]["href"],
                "versions_count": el.select("a~ a+ .gs_nph")[0].text,
                "versions_link": "https://scholar.google.com" + el.select("a~ a+ .gs_nph")[0]["href"] if
                el.select("a~ a+ .gs_nph")[0].text else "",
            })

        # clean data items in the array
        for i in range(len(scholar_results)):
            scholar_results[i] = {key: value for key, value in scholar_results[i].items() if
                                  value != "" and value is not None}

        print(len(scholar_results), scholar_results)

        with open("paper_list.json", "w", encoding="utf-8") as file:
            json.dump(scholar_results, file, ensure_ascii=False, indent=1)
    except Exception as e:
        print(e)


getScholarData()



# read next pages

        #next_page = soup.find('td', align="left")
        #next_url = 'https://scholar.google.com/' + next_page.find('a').attrs['href']
        #time.sleep(1)
        #print('scrapping next page')
        #print(next_url)