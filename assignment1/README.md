# 217nlp spacy NER apps

## How to run:

download the repo. set up your virtual env. in terminal, cd to directory and run
```sh
pip install -r requirements.txt 
```

### main_flask.py

to run flask app, in terminal, type and enter the command 

```sh
python main_flask.py
```

go to http://localhost:5000, type in your text, press enter to see the entities being highlighted. 

### main_streamlit.py
to run streamlit app, in terminal type and enter the command
```sh
streamlit run main_streamlit.py
```

go to http://localhost:8501, type in your text, press enter to see the named entities in a table. In the drop down menu, you can select which entity type to display in the table.  

### restful.py
to run flask restful api, in terminal type and enter the command
```sh

```
