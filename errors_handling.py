import logging
values = [10, 5, 6, 0, "hello", 23]
for value in values:
    try:
        print(10 / int(value))
    except ZeroDivisionError as e:
        pass
    except ValueError as e:
        print("Pogresan unos")
        raise
    except Exception as e:
        logging.exception(e)
    finally:
        print("ABC")