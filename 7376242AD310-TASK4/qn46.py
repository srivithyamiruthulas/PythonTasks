certs = {"E1": {"C1", "C2"}, "E2": {"C1", "C3"}}

common_certs = set.intersection(*certs.values())

cert_counts = {}
for s in certs.values():
    for c in s:
        cert_counts[c] = cert_counts.get(c, 0) + 1

unique_certs_employees = [e for e, s in certs.items() if any(cert_counts[c] == 1 for c in s)]

print(common_certs)
print(unique_certs_employees)
