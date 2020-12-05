import re


def get_formatted_document_data():
    documents = []
    with open("passport_processing_input.txt", "r") as documents_file:
        passport_buffer = []
        for line in documents_file.readlines():
            if line == "\n":
                passport = buffer_to_dict(passport_buffer)
                documents.append(passport)
                passport_buffer.clear()
            else:
                passport_buffer.append(line)

        if passport_buffer:
            passport = buffer_to_dict(passport_buffer)
            documents.append(passport)
            passport_buffer.clear()

    return documents


def buffer_to_dict(buffer):
    passport = dict()
    for content in buffer:
        content.strip()
        components = content.split()

        for component in components:
            key, val = component.split(":")
            passport[key] = val

    return passport


def count_valid_passports():
    passports = get_formatted_document_data()
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    optional_fields = {"cid"}
    valid_count = 0

    for passport in passports:
        passport_fields = set(passport.keys())
        if passport_fields == required_fields or passport_fields == (required_fields.union(optional_fields)):
            if is_valid_byr(passport["byr"]) \
                    and is_valid_iyr(passport["iyr"]) \
                    and is_valid_eyr(passport["eyr"]) \
                    and is_valid_hgt(passport["hgt"]) \
                    and is_valid_hcl(passport["hcl"]) \
                    and is_valid_ecl(passport["ecl"]) \
                    and is_valid_pid(passport["pid"]):
                valid_count += 1

    return valid_count


def is_valid_byr(byr):
    return len(byr) == 4 and (1920 <= int(byr) <= 2002)


def is_valid_iyr(iyr):
    return len(iyr) == 4 and (2010 <= int(iyr) <= 2020)


def is_valid_eyr(eyr):
    return len(eyr) == 4 and (2020 <= int(eyr) <= 2030)


def is_valid_hgt(hgt):
    if len(hgt) <= 2:
        return False

    unit = hgt[-2:]

    if unit == "cm":
        return 150 <= int(hgt[:-2]) <= 193
    elif unit == "in":
        return 59 <= int(hgt[:-2]) <= 76
    else:
        return False


def is_valid_hcl(hcl):
    if len(hcl) == 7 and hcl[0] == "#":
        hex_code = hcl[1:]
        match = re.match(r"[0-9a-f]+", hex_code)

        if match:
            return True

    return False


def is_valid_ecl(ecl):
    valid_ecls = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return ecl in valid_ecls


def is_valid_pid(pid):
    is_all_digits = re.match(r"[0-9]+", pid)
    return len(pid) == 9 and is_all_digits


def main():
    print(count_valid_passports())


if __name__ == "__main__":
    main()
