def main():
    time = "09:21"
    num = set()
    for i in time:
        if i.isdigit():
            num.add(i)

    hour = int(time[:2])
    min = int(time[3:])

    while(True):
        min = min + 1
        if min == 60:
            hour = hour + 1
            min = 0

        if hour == 24:
            hour = 0

        newtime = set()
        for i in str(hour):
            newtime.add(i)
        for j in str(min):
            newtime.add(j)

        if len(str(hour)) == 1 or len(str(min)) == 1:
            newtime.add('0')

        if newtime.issubset(time):
            retval = ""
            if len(str(hour)) == 1:
                retval = "0" + str(hour)
            else:
                retval = str(hour)

            retval = retval + ":"

            if len(str(min)) == 1:
                retval = retval + "0" + str(min)
            else:
                retval = retval + str(min)
            return(retval)


if __name__ == "__main__":
    main()