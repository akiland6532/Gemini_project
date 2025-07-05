import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    print(f"現在の時刻は: {get_current_time()} です。")
