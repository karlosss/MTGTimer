import time


def main():

    time_up = False
    print("\033[32m", end="")

    for i in range(100):
        print()

    while True:
        try:
            inp = input(">")
            duration = float(inp)
            break
        except ValueError:
            continue
        except EOFError:
            return False

    if duration <= 0:
        time_up = True
        duration = abs(duration)
        print("\033[31m", end="")

    m = int(duration)
    s = int((duration - int(duration))*60)

    if time_up:
        s -= 1
    else:
        s += 1

    while True:
        start = time.time()

        if not time_up:
            s -= 1
            if m == 0 and s == 0:
                time_up = True
                print("\033[31m", end="")
            elif s == -1:
                s = 59
                m -= 1
        else:
            s += 1
            if s == 60:
                s = 0
                m += 1

        if 0 <= m <= 1 and not time_up:
            print("\033[33m", end="")
        print("\n%02d:%02d" % (m, s), end="")

        try:
            time.sleep(start+1 - time.time())
        except KeyboardInterrupt:
            return True


while True:
    if not main():
        break
