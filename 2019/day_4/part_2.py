min_password = 357253
max_password = 892942


def validate_password(password):
    password = str(password)

    i = 0
    while i < len(password):
        j = i
        while j < len(password) and password[j] == password[i]:
            j += 1
        if j - i == 2:
            break  # We found a 2 length group!
        i = j

    if i >= len(password):
        return False

    increasing_order_rule = all(b >= a for a, b in zip(password, password[1:]))
    return increasing_order_rule


print(
    sum(
        validate_password(password)
        for password in range(min_password, max_password + 1)
    )
)
