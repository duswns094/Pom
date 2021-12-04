FROM python:3.10.0

WORKDIR /home/

RUN git clone https://github.com/duswns094/Pom.git

WORKDIR /home/Pom/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-rmt623a6@=c&5a^(oir1^hi!o1(!-=$^bomq7euga21zj@qqx!" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "Pom.wsgi","--bind","0.0.0.0:8000"]