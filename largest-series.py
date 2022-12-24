def largest_function(input_string, span):
    if span < 0:
        raise ValueError("span must be greater than zero")

    if span > len(input_string):
        raise ValueError("span must be smaller than string length")

    if not input_string.isdigit():
        raise ValueError("digits input must only contain digits")

    largest_product = 0
    for i in range(len(input_string) - span + 1):
        product = 1
        for j in range(span):
            product *= int(input_string[i + j])
        if product > largest_product:
            largest_product = product
    return largest_product


print(largest_function("73167176531330624919225119674426574742355349194934", 6))
