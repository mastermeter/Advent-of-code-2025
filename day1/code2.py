def data_preprocess():
    moves = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == 'L':
                moves.append(-int(line[1:]))
            else:
                moves.append(int(line[1:]))
    return moves

moves = data_preprocess()

pos = 50  
c = 0     

for delta in moves:
    step = 1 if delta > 0 else -1
    for _ in range(abs(delta)):
        pos = (pos + step) % 100
        if pos == 0:
            c += 1

print(c)
