n = 4
delay = 1
forget = 3

arr = [[delay, forget]]  # first person knows on day 1
for day in range(2, n+1):  # start from day 2
    new_people = []
    next_arr = []
    for can_share, will_forget in arr:
        # decrement their counters
        can_share -= 1
        will_forget -= 1

        # if they can share now → spawn a new person
        if can_share == 0 and will_forget > 0:
            new_people.append([delay, forget])

        # keep them if they haven't forgotten
        if will_forget > 0:
            next_arr.append([can_share, will_forget])

    # add new people into population
    next_arr.extend(new_people)
    arr = next_arr

print(len(arr))
