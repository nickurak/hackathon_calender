import time

def periodic(interval):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if not hasattr(f, "last_run") or (time.time() - f.last_run) > interval:
                f.last_run = time.time()
                return f(*args, **kwargs)
            return None
        return wrapper
    return decorator

@periodic(1)
def every_one():
    print("every one")


@periodic(5)
def every_five():
    print("every five")


@periodic(10)
def every_ten():
    print("every ten")

# Start your app
if __name__ == "__main__":
    while True:
        every_one()
        every_five()
        every_ten()
        time.sleep(1)
