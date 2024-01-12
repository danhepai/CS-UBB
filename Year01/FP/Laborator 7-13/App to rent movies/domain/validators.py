class MovieValidator:
    """
    Description: Validates a movie.
    """
    def validate(self, film):
        errors = ""
        if film.getTitle() == "":
            errors += "The title cannot be empty.\n"
        if film.getDescription() == "":
            errors += "The description cannot be empty.\n"
        if film.getType() == "":
            errors += "The type cannot be empty.\n"
        if len(film.getDescription()) > 1000:
            errors += "The description should be less than 10000 characters. \n"
        if len(film.getTitle()) > 200:
            errors += "The title should be less than 200 characters. \n"

        if len(errors) > 0:
            raise ValueError(errors)


class ClientValidator:
    """
    Description: Validates a client.
    """
    def validate(self, person):
        errors = ""
        if person.getName() == "":
            errors += "The name cannot be empty.\n"

        if person.getCNP() == "":
            errors += "The CNP cannot be empty.\n"
        else:
            cnp = person.getCNP().strip()
            if len(cnp) != 13:
                raise ValueError("The CNP length is invalid.\n")
            if not cnp.isdigit():
                raise ValueError("The CNP must be formed only with digits.\n")
            else:
                cnp_const = "279146358279"
                cnp_sum = 0
                for digit in range(12):
                    cnp_sum += int(cnp_const[digit]) * int(cnp[digit])

                if cnp_sum % 11 < 10:
                    if str(cnp_sum % 11) != cnp[12]:
                        raise ValueError("The CNP is invalid numeric - last digit is invalid.\n")
                else:
                    if str(cnp[12]) != 1:
                        raise ValueError("The CNP is invalid numeric - last digit is invalid.\n")

        if len(errors) > 0:
            raise ValueError(errors)
