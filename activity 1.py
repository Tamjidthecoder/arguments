def tip(bill,tip):
    total=bill*(1+0.01*tip)
    total=round(total,2)
    print(f"Please give me tip${total}")
tip(5,2)
