# vcc-tg-bot

Запустить ngrok и скопировать host в .env
```shell
docker run --net=host -it -e NGROK_AUTHTOKEN=2Ga3fo0Od9DkkPQknRqmLc7jbbH_CdrfPSZJnHVViLZjT9Rc ngrok/ngrok:latest http 5001
```

Запустить сервис
```shell
docker-compose up --build
```

Создать CSS
```shell
npx tailwindcss -i ./bot/static/input.css -o ./bot/static/style.css --watch
```
