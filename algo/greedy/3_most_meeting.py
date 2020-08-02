
def greedy(S,E):

    if not len(S) or not len(E):
        return []

    start_list = S.split()
    end_list = E.split()

    meeting_times = []
    for i in range(len(start_list)):
        meeting_times.append((i + 1, int(start_list[i]), int(end_list[i])))

    meeting_times = sorted(meeting_times, key=lambda x: x[2])

    current_end = None
    meetings = []

    for meeting in meeting_times:
        if not current_end:
            current_end = meeting[2]
            meetings.append(meeting)
            continue

        if meeting[1] > current_end:
            current_end = meeting[2]
            meetings.append(meeting)

    return meetings



print(greedy("34 35 356 545 545 34 343 766 74576 535 3453 765 564 4534 4353", "453 454 452 7657 555 6767 767 7456 435567 646 7657 3659 6767 6767 8768"))

print(greedy("1 3 0 5 8 5", "2 4 6 7 9 9"))
print(greedy("75250 50074 43659 8931 11273 27545 50879 77924", "112960 114515 81825 93424 54316 35533 73383 160252"))


