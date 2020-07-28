def most_meetings(start_times, end_times):

    dict = zip(start_times.split(" "), end_times.split(" "))

    activities = list(sorted(dict, key=lambda x: x[1]))

    count = 1

    end = activities[0][1]

    for activity in activities[1:]:
        if activity[0] >= end:
            end = activity[1]
            count += 1

    return count






print(most_meetings("1 3 2 5 8 5", "2 4 6 7 9 9"))
print(most_meetings("1 3 2 4", "2 4 3 6"))



