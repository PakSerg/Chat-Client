import datetime


def get_current_time() -> str:
    dt = datetime.datetime.now()

    hours_str =  f'0{dt.hour}' if len(str(dt.hour)) == 1 else dt.hour
    minutes_str = f'0{dt.minute}' if len(str(dt.minute)) == 1 else dt.minute
    time_now = f'{hours_str}:{minutes_str}'

    return time_now