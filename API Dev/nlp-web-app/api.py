
import paralleldots
paralleldots.set_api_key('HLMjlryOowK4DX6sEXL0QrEBT4IUgwifZqBru55zEmw')

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def abuse(text):
    abuse = paralleldots.abuse(text)
    return abuse

def emotion(text):
    emotion = paralleldots.emotion(text)
    return emotion

def keywords(text):
    keywords = paralleldots.keywords(text)
    return keywords
