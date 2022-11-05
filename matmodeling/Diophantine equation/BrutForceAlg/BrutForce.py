def brutForce(x, start):
    for a in range(start, x):
        for b in range(start, x):
            for c in range(start, x):
                for d in range(start, x):
                    if a + 2 * b + 3 * c + 4 * d == x:
                        print("a = " + str(a) + "; b = " + str(b) + "; c = " + str(c) + "; d = " + str(d))

brutForce(30, 1);