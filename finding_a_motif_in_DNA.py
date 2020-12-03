def substring_loc(t, s):
    position = []
    for i in range(len(t)):
        if s == t[i: i+len(s)]:
            position.append(i+1)
    return position

if __name__ == "__main__":
    with open("rosalind_subs.txt", 'r') as f:
        t = f.readline().strip()
        s = f.readline().strip()
    position = substring_loc(t, s)
    for i in position:
        print(i, end=" ")