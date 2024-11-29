# vcc-tg-bot

Заупустить ngrok и скопировать host в .env
```shell
docker run --net=host -it -e NGROK_AUTHTOKEN=TOKEN ngrok/ngrok:latest http 5001
```

Запустить сервис
```shell
docker-compose up --build
```
