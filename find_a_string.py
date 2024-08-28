def count_substring(string, sub_string):
    count = 0
    n = len(sub_string)
    for i in range(len(string)):
        if sub_string == string[i:i+n]:
            count += 1
        # print(f"i = {i} and count = {count} and string = {string[i:i+n]}")
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)