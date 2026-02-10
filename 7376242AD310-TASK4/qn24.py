visits = [
    {"id": "P1", "dr": "Smith", "count": 2},
    {"id": "P2", "dr": "Jones", "count": 5},
    {"id": "P1", "dr": "Jones", "count": 3}
]

# Doctor-wise total visits
dr_visits = {}
patient_totals = {}

for v in visits:
    dr_visits[v["dr"]] = dr_visits.get(v["dr"], 0) + v["count"]
    patient_totals[v["id"]] = patient_totals.get(v["id"], 0) + v["count"]

top_patient = max(patient_totals, key=patient_totals.get)

print(dr_visits)
print(top_patient)
