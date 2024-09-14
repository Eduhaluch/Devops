FROM python:3.12-slim

RUN pip install "fastapi[standard]" uvicorn

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

COPY . .

EXPOSE 80
CMD [ "fastapi", "run", "main.py", "--port", "80" ]
#CMD ["main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]
