# 217nlp spacy NER app dockerized

## how to run:

download the repo. make sure you have docker desktop downloaded and opened. in terminal, cd to assignment2 directory and run this command to build docker image from dockerfile (replace {ner} with any image name you want, and don't forget the period):

```sh
docker build --tag {ner} .   
```

When the image finishes building, check to see if it's present in docker desktop. Now run this command to run docker image in a container: 

```sh
docker run -dp 5000:5000 {ner}
```
Once you see {ner} running in docker desktop under containers, go to http://127.0.0.1:5000/. the ner app will be running. 
