opts = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}
n = int(input())
if n in opts:
    print(opts[n])
else:
    print('Greater than 9')