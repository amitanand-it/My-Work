def count_overlapping(string, substr):
    count = 0
    for i, ch in enumerate(string):
        if string[i:].startswith(substr):
            count += 1
    return count


#print(count_overlapping('banana', 'ana'))
print(count_overlapping('bananan', 'nan'))
