with open('athlete_events.tsv') as file:
    next_line = file.readline()
    store = [next_line]
    while next_line:
        next_line = file.readline()
        store.append(next_line)

print(store[1].split('\t'))
