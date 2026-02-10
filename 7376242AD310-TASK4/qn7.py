messages = ["Hello!", "", "How are you?", "Hello!", " ", "Good morning.", ""]
seen = set()
cleaned_messages = []

for msg in messages:
    if msg.strip() and msg not in seen:
        cleaned_messages.append(msg)
        seen.add(msg)
print(cleaned_messages)
