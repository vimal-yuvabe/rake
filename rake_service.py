# pylint: disable=missing-module-docstring
import re
from typing import List
from rake_nltk import Rake


class RakeService():
    """ Rake Service Object """

    def __init__(self):
        self.rake = Rake()

    def clean_text(self, message: str) -> str:
        """ Cleans the input text

        Parameters:
        message (str): Input text

        Returns:
        str: cleaned text

        """
        try:
            # remove "http"+link
            message = re.sub(r'http\S+', '', message)
            # remove "RT"
            message = re.sub(r'RT', '', message)
            # remove "@"+name
            message = re.sub(r'@\S+', '', message)
            # remove white space when there are more than one
            message = re.sub(r'\s+', ' ', message)
            # remove white space at the beginning of the string
            message = re.sub(r'\A\s', '', message)
        except Exception as e:
            pass
        return message

    def get_phrases(self, text: str) -> List:
        """ Extract the key phrases from input text

        Parameters:
        text (str): Input text

        Returns:
        List: Rake keywords

        """
        try:
            if type(text) != str or text is None:
                return []
            else:
                self.rake.extract_keywords_from_text(self.clean_text(text))
                return self.rake.get_ranked_phrases()
        except Exception as err:
            print(err)
            return []




if __name__ == "__main__":
    rk = RakeService()
    print(rk.get_phrases(
        "India will be winning this match. thank for you support and help"))
