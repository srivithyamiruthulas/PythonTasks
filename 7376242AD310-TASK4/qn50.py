papers = {"P1": ["A", "B"], "P2": ["B", "C"], "P3": ["B"]}

unique_all = set().union(*papers.values())
common_all = set.intersection(*papers.values())
max_unique_paper = max(papers, key=lambda p: len(set(papers[p])))

print(unique_all)
print(common_all)
print(max_unique_paper)
