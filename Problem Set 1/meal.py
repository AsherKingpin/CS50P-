
def main():
    time = input("what time is it ? ")
    time = convert(time)
    if 7.00 <= time <= 7.50:
        print("breakfast time")
    elif 12.50 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 18.30:
        print("dinenr time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes/60)

if __name__ == "__main__":
    main()
