def factors(filename):
    with open(filename, 'r') as file:
        for line in file:
            n = int(line.strip())
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                print(f"{n}={i}*{n//i}")
                break
            else:
                print(f"{n}=1*{n}")

factors('your_file.txt')
