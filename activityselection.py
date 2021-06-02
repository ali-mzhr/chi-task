def activityselection(start,end,N):
    duration = []
    totaldays = (max(end) - min(start)) + 1 #assuming that all tasks are assigned consecutive days
    for n in range(N):
        diff = (end[n] - start[n]) + 1
        duration.append(diff)
    duration.sort()
    tasks = 0
    days = 0
    while days < totaldays:
        if (days + duration[tasks]) > totaldays:
            break
        days += duration[tasks]
        tasks+=1
    return tasks