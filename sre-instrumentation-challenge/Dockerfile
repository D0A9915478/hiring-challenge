FROM python:3

COPY /src/ .
RUN pip3 install -e .
EXPOSE 5000

CMD [ "python3", "./run.py" ]