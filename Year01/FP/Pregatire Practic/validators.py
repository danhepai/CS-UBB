class Validator:
    def validate_tractor(self, tractor):
        errors = ""
        if tractor.getName() == "":
            errors += 'The name cannot be empty'
        if not isinstance(tractor.getPrice(), int):
            errors += 'The price must be a integer'
        if tractor.getModel() == "":
            errors += 'The model cannot be empty'
        if not self.validRevisionDate(tractor.getDate()):
            errors += "Invalid revision date"
        if errors != "":
            raise Exception(errors)

    def validRevisionDate(self, revision_date):
        errors = ''
        if revision_date == "":
            errors += 'The revision date cannot be empty'
        revision_date = revision_date.split('/')
        if len(revision_date) != 3:
            errors += 'Revision date is a invalid length'
        else:
            if not 0 < int(revision_date[0]) < 32:
                errors += 'Day is invalid'
            if not 0 < int(revision_date[1]) < 13:
                errors += 'Month is invalid'
            if not 1900 < int(revision_date[0]) < 2100:
                errors += 'Year is invalid'
        return errors

    def validate_filter(self, text, number):
        errors = ''
        if not isinstance(number, int):
            errors += "The filter number must be an integer"

        if errors != '':
            raise Exception(errors)
