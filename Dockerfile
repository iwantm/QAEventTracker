FROM python:3.7
WORKDIR /app
COPY requirements.txt . 
RUN pip3 install -r requirements.txt
COPY . . 
EXPOSE 5000
ENTRYPOINT ["gunicorn", "--workers=4", "--bind=0.0.0.0:5000", "app:app"]

