
def greedy(st, et):

    st = st.split()
    et = et.split()

    meeting_times = []

    for i in range(1, len(st) + 1):
        meeting_times.append((i, int(st[i - 1]), int(et[i-1])))

    meeting_times.sort(key=lambda x: x[2])

    meetings = []

    current_end = None


    for meeting in meeting_times:

        if not current_end or meeting[1] >= current_end:
            current_end = meeting[2]
            meetings.append(meeting)


    return meetings


"""
must figure out a way to deal with same start time
"""
print(greedy("34 35 356 545 545 34 343 766 74576 535 3453 765 564 4534 4353", "453 454 452 7657 555 6767 767 7456 435567 646 7657 3659 6767 6767 8768"))

print(greedy("1 3 0 5 8 5", "2 4 6 7 9 9"))
print(greedy("75250 50074 43659 8931 11273 27545 50879 77924", "112960 114515 81825 93424 54316 35533 73383 160252"))




