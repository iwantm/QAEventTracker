FROM python:3.7
WORKDIR /app
ENV DATABASE_URI_PROJECT mysql+pymysql://root:pass@new-sql:3306/event
COPY requirements.txt . 
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod +x start.sh
EXPOSE 5000
ENTRYPOINT ["/bin/bash", "start.sh"]


