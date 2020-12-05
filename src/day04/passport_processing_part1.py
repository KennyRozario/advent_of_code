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
            valid_count += 1

    return valid_count


def main():
    print(count_valid_passports())


if __name__ == "__main__":
    main()
