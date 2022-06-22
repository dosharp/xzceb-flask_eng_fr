"""
June 20 - added test for null input and removed test print statements
June 19 - this works in Anaconda base with a 10/10 rating.
        - only fix was to change format of .env entries to remove quotes
        - also changes variable names to imply constant for URL and APIKEY
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
load_dotenv()

APIKEY = os.environ.get('apikey')
URL = os.environ.get('url')


authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)

def e2f(english_text):
    """
    English to French translator.
    """
    if english_text == '':    # test for null input
        return ''
    
    translation_response = language_translator.translate(
    text = english_text,
    model_id='en-fr')
    trans_dict = translation_response.get_result()
    trans_text = trans_dict['translations'][0]['translation'] # pylint: disable=unsubscriptable-object
    return trans_text

def f2e(french_text):
    """
    French to English
    """
    if french_text == '':      # test for null input
        return ''
    
    # following translate() has get_result() dotted on instead of separate like above.
    trans_dict = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    trans_text = trans_dict['translations'][0]['translation'] # pylint: disable=unsubscriptable-object
    return trans_text

