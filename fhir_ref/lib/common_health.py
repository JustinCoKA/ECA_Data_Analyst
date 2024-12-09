def generate_medicare_number():
    return fake.random_number(digits=10, fix_len=True)

def generate_ihi_number():
    return fake.random_number(digits=16, fix_len=True)

def generate_dva_number():
    return fake.lexify(text="??????")
