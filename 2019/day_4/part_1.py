min_password = 357253
max_password = 892942


def validate_password(password):
    password = str(password)

    adjacent_rule = any(
        password[i] == password[i + 1]
        for i in range(len(password) - 1)
    )
    if not adjacent_rule:
        return False

    increasing_order_rule = all(b > a for a, b in zip(password, password[1:]))
    return increasing_order_rule


print(
    sum(
        validate_password(password)
        for password in range(min_password, max_password + 1)
    )
)
