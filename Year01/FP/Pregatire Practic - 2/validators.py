class Validator:
    def validate(self, exam):
        errors = ""
        date = exam.getDate().split('.')
        hour = exam.getHour().split(':')

        if len(date) != 2:
            errors += "Validator -> 8: Invalid type of date\n"
        else:
            if not 1 <= int(date[0]) <= 31 or not 1 <= int(date[1]) <= 12:
                errors += "Validator -> 11: Invalid date\n"

        if len(hour) != 2:
            errors += "Validator -> 14: Invalid type of hour\n"
        else:
            if not 0 <= int(hour[0]) <= 23 or not 0 <= int(hour[1]) <= 59:
                errors += "Validator -> 17: Invalid hour\n"

        if errors != "":
            raise ValueError(errors)
