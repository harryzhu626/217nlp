FROM python:3.10

WORKDIR / 

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY . .

# CMD ["python", "main_flask.py", "--host=0.0.0.0"]
CMD ["python", "-m" , "flask", "--app", "main_flask", "run", "--host=0.0.0.0"]