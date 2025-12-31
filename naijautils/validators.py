def validate_bvn(bvn):
    return isinstance(bvn, str) and len(bvn) == 11 and bvn.isdigit()

def validate_nin(nin):
    return isinstance(nin, str) and len(nin) == 11 and nin.isdigit()
