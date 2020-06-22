from datetime import datetime

def log(message):
    text = '[{time}] {message}'.format(
        time=datetime.now(),
        message=message
    )
    print(text)
