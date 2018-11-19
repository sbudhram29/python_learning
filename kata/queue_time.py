def queue_time(customers, n):
    time_queue = {}
    smallest = 0

    while(len(customers)):
        for i in range(n):
            if not len(customers):
                break

            if i not in time_queue:
                time_queue[i] = [customers.pop(0)]
            else:
                if sum(time_queue[i]) == smallest:
                    time_queue[i].append(customers.pop(0))

            smallest = min(time_taken(time_queue))

    return max(time_taken(time_queue))


def time_taken(items_queue):
    time_taken = []
    for k, v in items_queue.items():
        time_taken.append(sum(v))

    return time_taken


def queue_time2(customers, n):
    lanes = [0]*n
    for i in customers:
        # get the index of the lanes that is ready
        ready_lane = lanes.index(min(lanes))
        lanes[ready_lane] += i
    # return the lane that took the longest
    return max(lanes)


print(queue_time([2, 2, 3, 3, 4, 4], 2))
print(queue_time([32, 17, 32, 24, 21, 48, 28, 31, 36, 35, 33, 40], 6))
print(queue_time2([32, 17, 32, 24, 21, 48, 28, 31, 36, 35, 33, 40], 6))
