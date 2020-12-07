def get_customs_forms():
    forms = []
    with open("custom_customs_input.txt", "r") as customs_forms_file:
        buffer = []
        for line in customs_forms_file.readlines():
            if line == "\n":
                forms.append(buffer.copy())
                buffer.clear()
            else:
                buffer.append(line.strip())

        if buffer:
            forms.append(buffer.copy())
            buffer.clear()

    return forms


def total_number_of_yes_responses():
    customs_forms = get_customs_forms()
    total_yes_responses = 0

    for group in customs_forms:
        group_answers = set()
        for form in group:
            for response in form:
                group_answers.add(response)
        total_yes_responses += len(group_answers)

    return total_yes_responses


def main():
    print(total_number_of_yes_responses())


if __name__ == "__main__":
    main()
