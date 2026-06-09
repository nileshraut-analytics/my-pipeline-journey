from datetime import datetime

# current_time = datetime.now()
# print(current_time)
# formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_time)

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

print(get_timestamp())