class Time:
    """Represents the time of day.abs

    attributes: hour, minute, second
    """

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print("{0:0=2d}:{1:0=2d}:{2:0=2d}".format(
            self.hour, self.minute, self.second))

    def is_after(self, t1, t2):

        # works because comparing tuples
        return tuple([t1.hour, t1.minute, t1.second]) > tuple([t2.hour, t2.minute, t2.second])


def main():

    time = Time(9, 54, 23)

    time.print_time()

    isAfter = time.is_after(Time(11, 25, 25), Time(9, 56, 23))

    print(isAfter)

    isAfter = time.is_after(Time(1, 25, 25), Time(9, 56, 23))

    print(isAfter)


if __name__ == '__main__':
    main()
