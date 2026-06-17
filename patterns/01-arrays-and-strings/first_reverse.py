def reverse(str):
    original_string = str
    reverse_string = str[::-1]

    if original_string == reverse_string:
        return reverse_string + " (palindrome)"
    else:
        return reverse_string


print(reverse("cooc"))
