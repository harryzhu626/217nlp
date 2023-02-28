import streamlit as st
from ner import SpacyDocument
import streamlit.components.v1 as components
import pandas as pd
from spacy import displacy

st.title("NER with spacy API")
st.snow()

def enter_sentence() -> str:
    return st.text_area("Enter your text here:", placeholder="type then press cmd/⌘+enter")

def ner():
    text = enter_sentence()
    doc = SpacyDocument(text)
    xml = doc.get_entities_with_markup()
    entities = doc.get_entities() # each ent is a tuple of (range, type, string)
    tokens = doc.get_tokens()
    return xml, entities, tokens, doc.doc

def display_markup(xml):
    path = '"https://github.com/harryzhu626/217nlp_pa/blob/main/pa1/static/css/main.css"'
    xml = '<link rel="stylesheet" href=' + path + '> ' + xml
    components.html(xml)
    

def to_df(entities: list) -> pd.DataFrame:
    return pd.DataFrame(data=entities, columns=['start pos', 'end pos', 'entity type', 'string'])

def display_entities(ent_df: pd.DataFrame):

    col, buff, buff2 = st.columns([2,2,1])

    temp_series = pd.concat([pd.Series('All Types'), ent_df['entity type']])
    option = col.selectbox(
        "Select the entity type you'd like to view",
        temp_series.unique())
    
    f'Here are all strings labeled "{option}": ',
    if option == 'All Types':
        ent_df
    else:
        ent_df[ent_df['entity type'] == option]

def display_new(doc):
    displacy.serve(doc, style="ent")

if __name__ == "__main__":
    xml, entities, tokens, doc = ner()
    ent_df = to_df(entities)
    display_entities(ent_df)
    #display_new(doc)
    #display_markup(xml)
