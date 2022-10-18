import json
from datetime import datetime

import pandas as pd
import requests


class GoogleScraper():

    def __init__(self, query: str, country: str, language: str):
        self.url = "https://www.google.com/complete/search"
        self.params: dict[str:str] = {
            "client": "chrome",
            "xssi": "t",
            "authuser": 1
        }
        self.headers: dict[str:str] = {
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
        }
        self.params["q"] = query
        self.params["gl"] = country
        self.params["hl"] = language

    def request_suggestions(self):
        response = requests.get(url=self.url, params=self.params, headers=self.headers)
        response_text = response.text
        response_dict = json.loads(response_text[5:])

        return response_dict

    def clean_responses(self, response_dict):
        queries = response_dict[1]
        relevance = response_dict[4]['google:suggestrelevance']
        key_word_relevance = [response_dict[4]['google:verbatimrelevance'] for x in response_dict[1]]

        df = pd.DataFrame()

        df['queries'] = queries
        df['relevance'] = relevance
        df['keyword_relevance'] = key_word_relevance

        return df
