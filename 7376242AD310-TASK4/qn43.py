attendance = [("S1", "A1"), ("S2", "A1"), ("S1", "A2")]

session_counts = {}
attendee_sessions = {}

for sid, aid in attendance:
    session_counts[sid] = session_counts.get(sid, 0) + 1
    if aid not in attendee_sessions:
        attendee_sessions[aid] = set()
    attendee_sessions[aid].add(sid)

multi_session = [aid for aid, sids in attendee_sessions.items() if len(sids) > 1]

print(session_counts)
print(multi_session)
