# DASHBOARD SERVICE HOSPITAL
Restfull-API dashboard rumah sakit memiliki beberapa service:
1. employee
2. doctor
3. patient
4. appointment

## Stack-tech
1. flask
2. postgree
3. jwt
4. docker
5. SqlAlchemy
6. Pydantic

## cara menjalankan
1. Buatlah file `.env` dan `env.db.local` seperti contoh-nya dan isikan nilai env sesuai dengan configurasi local komputer anda.

2. jalankan perintah `docker-compose up -d` untuk melakukan build dan membuat container dengan nama flask_app dan flask_db

3. jika container flask_app tidak dapat berjalan, coba cek kembali nilai env untuk database host-nya. jika ingin menjalankan tanpa docker ubah nilai env host database anda dengan `localhost` jika anda ingin menjalankan di docker container ubah dengan `flask_db`.