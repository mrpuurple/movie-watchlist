FROM python:3.11
WORKDIR /movie_library
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
RUN chmod +x gunicorn.sh
ENTRYPOINT ["./gunicorn.sh"]