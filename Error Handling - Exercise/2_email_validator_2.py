class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def at_symbol_validation(current_email_parts):
    no_at_symbol = False
    more_than_one_at_symbol = False

    if len(current_email_parts) < 2:
        no_at_symbol = True

    elif len(current_email_parts) > 2:
        more_than_one_at_symbol = True

    return no_at_symbol, more_than_one_at_symbol


def name_too_short(current_name):
    if len(current_name) <= 4:
        return True
    return False


def domain_is_invalid(domain):
    valid_domains = ['.com', '.bg', '.org', '.net']
    if domain in valid_domains:
        return False
    return True


email = input()

while email != "End":

    parts_of_email = email.split("@")

    at_symbol_missing, at_symbol_more_than_once = at_symbol_validation(parts_of_email)
    if at_symbol_missing:
        raise MustContainAtSymbolError("Email must contain @")
    elif at_symbol_more_than_once:
        raise MoreThanOneAtSymbolError("Email must contain only one @ symbol")

    name = parts_of_email[0]
    if name_too_short(name):
        raise NameTooShortError("Name must be more than 4 characters")

    domain_name = email.split(".")[-1]
    current_domain = f".{domain_name}"
    if domain_is_invalid(current_domain):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()





