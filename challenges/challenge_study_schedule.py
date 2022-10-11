def study_schedule(permanence_period, target_time):
    students = 0
    try:
        for hour in permanence_period:
            if hour[0] <= target_time and hour[1] >= target_time:
                students += 1
    except TypeError:
        return None

    return students
