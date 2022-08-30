FROM python:3.8.10

ARG SAMPLE_ARG

# COPY {{cookiecutter.app_name}}/requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY {{cookiecutter.app_name}}/app/ /app
WORKDIR /app

CMD ["main.py"]
ENTRYPOINT ["python3"]