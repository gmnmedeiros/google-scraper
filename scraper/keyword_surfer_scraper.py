import json
from datetime import datetime

import pandas as pd
import requests


class KeyWordSurferScraper():

    country = ''

    def __init__(self, country):
        self.country = country

    def prepare_keywords(self, keywords):
        keyword_array = pd.Series(keywords).drop_duplicates(keep='first')
        refined_keyword_array = keyword_array.str.replace(' ', '%20').unique()
        keyword_chunks = [refined_keyword_array[x:x + 25] for x in range(0, len(refined_keyword_array), 25)]

        return keyword_chunks

    def request_keyword_metrics(self, keyword_chunks):
        country = self.country

        keyword_surfer_url = (
            f'https://db2.keywordsur.fr/keyword_surfer_keywords?country={country}&keywords=[%22' +
            '%22,%22'.join(keyword_chunks[0]) + '%22]'
        )

        metrics_response = requests.get(keyword_surfer_url)
        metrics_json = json.loads(metrics_response.text)

        return metrics_json

    def metrics_json_to_dataframe(self, metrics_json):
        df = pd.DataFrame(metrics_json).T
        df = df.rename_axis('queries').reset_index(drop=False)

        return df
