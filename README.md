# Bitly url shorterer

Python script to short link with bitly service.
For shorted links it print amount of clicks.

### How to install

1. You need to register on https://bitly.com/ and get Generic Access Token
2. Create .env file and put TOKEN to file like this TOKEN=12312J31ASDADS2309UFSFDSK
3. Install dependencies (written below)

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use
```
python main.py https://example.com/page/item
>>Сокращенная ссылка: http://bit.ly/2S5hTtU
```
```
python main.py http://bit.ly/2S5hTtU
>>Количество кликов по ссылке: 3
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).