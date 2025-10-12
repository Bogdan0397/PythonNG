try:
    with open('try.txt') as f:
        for t in f:
            print(t)
except FileNotFoundError as e:
    print(e)