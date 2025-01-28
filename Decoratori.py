from datetime import datetime

def logare_actiuni(func):
    def wrapper(*args, **kwargs):
        rezultat = func(*args, **kwargs)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] [LOG]: Funcția '{func.__name__}' a fost apelată cu argumentele {args[1:]}")
        return rezultat
    return wrapper

