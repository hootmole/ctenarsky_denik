"""
this file will act as the main text generator, collecting all the necessary text.
Then a post-processing pipeline will be used, such as error correction and text optimization.
In the final stage, the data will be translated and placed in a user-friendly file such as word (docx).
"""

import requests
import json
import deepl
import random
import os
import openai
import math
import cv2
import numpy
# base libraries


# global functions
def translateTo(text: str, target_lang="CS") -> str:
    with open("key.txt", "r") as key:
        for line in key.readlines():
            if "deepl: " in line:
                deepl_key = line.replace("deepl: ", "").replace("\n", "")

    translator = deepl.Translator(deepl_key)
    result = translator.translate_text(text, target_lang=target_lang)
    translated_funfact = result.text

    return translated_funfact


def openai_response(prompt: str, token_lenght=150, ) -> str:
    with open("key.txt", "r") as key:
        for line in key.readlines():
            if "openai: " in line:
                openai.api_key = line.replace("openai: ", "").replace("\n", "")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text'].replace("\n", " ")


# stencil list, used for storing stock data for Languange Model ML (openai GPT) guidence

stencil = [
    """
    author: William Shakespeare
    ilustrator: none

    """
]
