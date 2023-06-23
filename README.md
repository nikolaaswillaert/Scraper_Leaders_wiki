## Leader Scraper

![wiki logo](https://github.com/nikolaaswillaert/Scraper_Leaders_wiki/assets/106211266/026413dc-8653-44b0-bee3-d047c277ed15)

This script will scrape the wikipedia page of leaders from BE, FR, RA, RU and US and will return the first paragraph of that wikipedia page. The returned paragraph will be cleaned from phonetic pronunciation and other wiki-unique additions.

![first_paragraph](https://github.com/nikolaaswillaert/Scraper_Leaders_wiki/assets/106211266/2144152c-1682-48c5-8170-d12903f02b65)

I am using an API (country-leaders) to get this information. Documentation below:
[https://country-leaders.onrender.com/docs]

The output of the script: 1 json file and 1 plain text file.
The json file will contain all of the information that has been pulled from the API with an additional key:value pair (first_paragraph:"content of the first paragraph).

The plain text file will only contain the cleaned plain text version of the first paragraph

You will find an additional .pynb file (wikipedia_scraper.ipynb) that will guide you step by step on how I got to the end result.
## Installation
Program was written using python 3.11. Please make sure you have python 3.11 installed.
have added the requirements.txt file as wel if for some reason the code would not run:
```
pip install -r requirements.txt
```

## Usage
Navigate to your workfolder (pro tip: use a virtual environment to avoid errors) and clone the repository:
```
git clone git@github.com:nikolaaswillaert/Scraper_Leaders_wiki.git
cd Scraper_Leaders_wiki
python3 leaders_scraper.py
```

or open in IDE and run the [label](leaders_scraper.py) file

## Timeline
Approximately 2 days (approx. 16 hours) to completion
- Started assignment on 21/06/2023 - 9.30 (am)
- Finished assignment on 23/06/2023 - 10:00 (am)

## Personal situation
This project was done as part of the AI Boocamp at BeCode.org
At this time I was a Junior at Becode (ARAI5)
