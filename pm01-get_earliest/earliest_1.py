def get_earliest(d0, d1):
    if d0 is None or d1 is None:
        return None

    month0, date0, year0 = d0.split('/')
    month1, date1, year1 = d1.split('/')
    return d0 if (year0, month0, date0) < (year1, month1, date1) else d1

if __name__ == "__main__":
    d0 = "02/29/1972"
    d1 = "12/21/1946"
    result = get_earliest(d0, d1)
    print(result)