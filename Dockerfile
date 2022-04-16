FROM python:3.8.11-buster
RUN apt update && apt install gcc -y
ENV PYTHONUNBUFFERED=1
WORKDIR /home/app/
COPY requirements.txt /home/app/
RUN pip install -r requirements.txt
COPY . /home/app/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
