# 217nlp spacy NER app dockerized

## requirements (listed in requirements.txt)

## how to run:

download the repo. make sure you have docker desktop downloaded and opened. in terminal, cd to assignment2 directory and run this command to build docker image from dockerfile:

```sh
docker build --tag ner .   
```

```sh
docker run -dp 5000:5000 ner
```
