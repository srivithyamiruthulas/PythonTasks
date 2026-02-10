earnings = [("P1", 100), ("P2", 200), ("P1", 150)]

totals = {}
counts = {}
for pid, amt in earnings:
    totals[pid] = totals.get(pid, 0) + amt
    counts[pid] = counts.get(pid, 0) + 1

avg_earnings = {pid: totals[pid] / counts[pid] for pid in totals}

top_partner = max(avg_earnings, key=avg_earnings.get)

print(totals)
print(top_partner)