shows = {
    "12PM": {1, 2, 3, 4},
    "3PM": {2, 3},
    "6PM": {1, 2, 3}
}
total_seats = {1, 2, 3, 4}

full_booked = [time for time, seats in shows.items() if seats == total_seats]
booked_in_every = set.intersection(*shows.values())

print(full_booked)
print(booked_in_every)
