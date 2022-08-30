def add_time(start, duration, day=None):
    # define beginning
    options = ["PM", "AM"]
    sep = start.split()
    time = sep[0].split(":")
    p_start = options.index(sep[1])
    if sep[1] == "AM":
        day_start = 0
    else:
        day_start = 1
    weekdays = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    if day is not None:
        day_old = day
        day_old_index = weekdays.index(day.lower())

    start_h = time[0]
    start_m = time[1]

    du_sp = duration.split(":")
    duration_h = du_sp[0]
    duration_m = du_sp[1]

    # calc min and store h for adding later
    new_m = int(start_m) + int(duration_m)
    tmp_h = 0
    if new_m > 60:
        tmp_h = new_m // 60
        new_m = new_m % 60

    # Calc h and store period for adding later
    new_h = int(start_h) + int(duration_h)
    tmp_p = 0
    if tmp_h > 0:
        new_h = new_h + tmp_h

    if sep[1] == "PM":
        if new_h >= 12 and new_h % 12 == 0:
            tmp_p = new_h // 12
            new_h = 12
        elif new_h > 12:
            tmp_p = new_h // 12
            new_h = new_h % 12

    elif sep[1] == "AM":
        if new_h >= 12 and new_h % 12 == 0:
            tmp_p = new_h // 12
            new_h = 12
        elif new_h > 12:
            tmp_p = new_h // 12
            new_h = new_h % 12
    # period
    new_p = options[p_start]
    if tmp_p >= 1:
        if tmp_p % 2 != 0:
            if p_start == 0:
                new_p = options[1]
            else:
                new_p = options[0]
    # Calculate day
    day_start = day_start + tmp_p
    if day is None:
        text = ""
        if (
            (day_start % 2) == 0
            and (day_start // 2) == 1
            or (day_start % 2) == 1
            and (day_start // 2) == 1
        ):
            text = "(next day)"
        elif (day_start // 2) > 1:
            hold = tmp_p // 2
            text = "({} days later)".format(hold + 1)
        else:
            new_time = str(new_h) + ":" + "{:0>2d}".format(new_m) + " " + new_p
        if text != "":
            new_time = (
                str(new_h) + ":" + "{:0>2d}".format(new_m) + " " + new_p + " " + text
            )

    # If weekday
    else:
        text = ""
        if (
            (day_start % 2) == 0
            and (day_start // 2) == 1
            or (day_start % 2) == 1
            and (day_start // 2) == 1
        ):
            if day_old_index != 6:
                new_day_index = day_old_index + 1
            else:
                new_day_index = 0
            text = ", " + weekdays[new_day_index].capitalize() + " (next day)"
        elif (day_start // 2) > 1:
            hold = tmp_p // 2
            # Find new index

            new_day_index = day_old_index + ((hold + 1) % 7)
            if new_day_index > 6:
                new_day_index = new_day_index - 7

            text = (
                ", "
                + weekdays[new_day_index].capitalize()
                + " ({} days later)".format(hold + 1)
            )
        else:
            new_time = (
                str(new_h)
                + ":"
                + "{:0>2d}".format(new_m)
                + " "
                + new_p
                + ", "
                + weekdays[day_old_index].capitalize()
            )
        if text != "":
            new_time = str(new_h) + ":" + "{:0>2d}".format(new_m) + " " + new_p + text

    return new_time