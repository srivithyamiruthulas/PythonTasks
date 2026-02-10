bids = [("B1", 100), ("B2", 500), ("B1", 200)]

bidder_max = {}
for bidder, amt in bids:
    if amt > bidder_max.get(bidder, 0):
        bidder_max[bidder] = amt

top_bidder = max(bids, key=lambda x: x)[0]

print(bidder_max)
print(top_bidder)
