FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app
COPY artist/ .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
CMD ["python3", "manage.py", "runserver", "0:8000", "--insecure"]