FROM python:3.10.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/duswns094/Pom.git

WORKDIR /home/Pom/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-rmt623a6@=c&5a^(oir1^hi!o1(!-=$^bomq7euga21zj@qqx!" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c","python manage.py migrate --settings=Pom.settings.deploy && gunicorn Pom.wsgi --env DJANGO_SETTINGS_MODULE=Pom.settings.deploy --bind 0.0.0.0:8000"]