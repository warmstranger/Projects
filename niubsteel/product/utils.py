import re

def number_only(origin_string):
    result = filter(lambda c: c in '0123456789.', origin_string)
    if not result:
        return 9999999.0
    try:
        number = float(result)
    except ValueError:
        return 9999999.0

    if number == 0:
        return 9999999.0

    return number

def analyze_spec(spec):
    parts = spec.split('*')
    part0, part1 = 0.0, 0.0
    if len(parts) > 0:
        try:
            part0 = float(number_only(parts[0]))
        except:
            print number_only(parts[0])
    if len(parts) > 1:
        try:
            part1 = float(number_only(parts[1]))
        except:
            print number_only(parts[1])
    return part0, part1

def analyze_tags(value, TAGS):
    for tag in TAGS:
        hit = False
        for keyword in tag:
            if re.match(keyword, value):
                hit = True
                break
        if hit:
            yield tag
