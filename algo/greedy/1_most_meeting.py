def most_meetings(start_times, end_times):

    start_list = start_times.split(" ")
    end_list = end_times.split(" ")

    dict = []

    for i, start in enumerate(start_list):
        # save a tuple with i + 1, start and end time
        dict.append( (i + 1,start, end_list[i]))

    # sort activities by end time
    activities = sorted(dict, key=lambda x: int(x[2]))

    end = None
    result = []
    for act in activities:
        if not end:
            end = int(act[2])
            result.append(str(act[0]))

        if int(act[1]) >= end:
            end = int(act[2])
            result.append(str(act[0]))



    return " ".join(result)

"""
must figure out a way to deal with same start time
"""
print(most_meetings("34 35 356 545 545 34 343 766 74576 535 3453 765 564 4534 4353",
                    "453 454 452 7657 555 6767 767 7456 435567 646 7657 3659 6767 6767 8768"))

print(most_meetings("1 3 0 5 8 5", "2 4 6 7 9 9"))
print(most_meetings("75250 50074 43659 8931 11273 27545 50879 77924",
                    "112960 114515 81825 93424 54316 35533 73383 160252"))
