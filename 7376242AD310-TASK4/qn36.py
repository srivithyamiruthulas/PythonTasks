transactions = [
    {"account_id": "A1", "amount": 1000, "type": "CREDIT"},
    {"account_id": "A2", "amount": 500, "type": "CREDIT"},
    {"account_id": "A1", "amount": 200, "type": "DEBIT"}
]

balances = {}
for t in transactions:
    aid = t["account_id"]
    amt = t["amount"]
    if aid not in balances:
        balances[aid] = 0
    if t["type"] == "CREDIT":
        balances[aid] += amt
    else:
        balances[aid] -= amt

max_balance_account = max(balances, key=balances.get)

print(balances)
print(max_balance_account)
