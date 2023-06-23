import requests
import json
import re
from bs4 import BeautifulSoup

def get_first_paragraph(wikipedia_url):
    #   print(wikipedia_url) # keep this for the rest of the notebook
    print(wikipedia_url)
    #   get the wiki text
    session = requests.Session()
    r = session.get(wikipedia_url).text
    # make soup :)
    soup = BeautifulSoup(r, "html.parser")
    paragraphs = []
    # find all the paragraphs and put them in varibale paragraphs
    for elem in soup.find_all("p"):
        if elem.find_parent(class_="bandeau-cell"):
            continue
        if elem.text.strip() != "":
            paragraphs.append(elem.text)
            break
    # remove phonetics / tags / endlines / other exceptions
    pattern = r"<.*?>|\(\/.*?\;|\[.{1,2}\]|\n|\(\s.*?\)\)|\[.*?\s.*?\]|\[.*?\s.*?\]|\(/.*?\)|\/.*?\;|\xa0"
    first_para = re.sub(pattern, "", paragraphs[0])
    return first_para

def get_leaders():
    leaders_url = "https://country-leaders.onrender.com/leaders"
    cookie_url = "https://country-leaders.onrender.com/cookie/"
    countries_url = "https://country-leaders.onrender.com/countries"
    # start session
    session = requests.Session()
    # get cookie for session (30 seconds)
    cookies = session.get(cookie_url).cookies
    # get countries to iterate over
    countries = session.get(countries_url, cookies=cookies)
    # create dictionary to store key:values in
    leaders_per_country = {}
    # create extra variable to store the full text (plaintext)
    full_text = []
    for i in countries.json():
        params = {"country":f'{i}'}
        # check if the cookie is still valid (at start of every country call)
        if countries.status_code == 200:
            cookies = session.get(cookie_url).cookies
            leaders = session.get(leaders_url, cookies=cookies, params=params)
            leaders_per_country[f'{i}'] = leaders.json()
            # iterate over all the leaders
            for leader in leaders_per_country[f"{i}"]:
                # get the leader url
                leader_url = leader["wikipedia_url"]
                # extract paragraph out of that url
                first_paragraph = get_first_paragraph(leader_url)
                # add a new entry to the leader dictionary "first_paragraph" and add the first paragraph
                leader["first_paragraph"] = first_paragraph
                full_text.append(first_paragraph)
        #if cookie is expired (not status code 200) request a new cookie
        else:
            cookies = session.get(cookie_url).cookies
    #return both the full_text (plain text) and the leaders_per_country (json - dictionary)
    return full_text, leaders_per_country

# save the added summary into the json file
def save_json(end_text):
    with open("leaders.json", "w") as file:
        # Write the JSON object to the file
        json.dump(end_text, file)
    # Close the file when done writing
    file.close()

def save_text(full_text):
    with open("plaintext.txt", "w") as f:
        for i in full_text:
            #write every paragraph in plain text
            f.write(i)
            f.write("\n"*2)
    # Close the file when done writing
    f.close()

if __name__ == "__main__":
    full_text, end_text = get_leaders()
    save_json(end_text)
    save_text(full_text)
    