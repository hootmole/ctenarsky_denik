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
    deepl_key = "674e3591-912f-797e-09bc-591d8631b111:fx"
    translator = deepl.Translator(deepl_key)
    result = translator.translate_text(text, target_lang=target_lang)
    translated_funfact = result.text

    return translated_funfact


def openai_response(prompt: str, token_lenght=150, ) -> str:
    openai.api_key = "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"

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

