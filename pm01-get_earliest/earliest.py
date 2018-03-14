def get_earliest(date0, date1):
    if date0 is None or date1 is None:
        return None

    date0_a = date0.split('/')
    date1_a = date1.split('/')

    if int(date0_a[2]) < int(date1_a[2]):
        return date0
    if int(date0_a[2]) > int(date1_a[2]):
        return date1

    if int(date0_a[0]) < int(date1_a[0]):
        return date0
    if int(date0_a[0]) > int(date1_a[0]):
        return date1

    if int(date0_a[1]) < int(date1_a[1]):
        return date0

    return date1

if __name__ == "__main__":
    d0 = "02/29/1972"
    d1 = "12/21/1946"
    result = get_earliest(d0, d1)
    print(result)
