
def calculate_area(length, width):
    return length * width
sections = {
    "parking": (25, 12),
    "servicing space": (78, 5),
    "garage": (15, 32),
    "bodyshop": (25, 36)
}
for section, (length, width) in sections.items():
    area = calculate_area(length, width)
    print(f"The area of the {section} section is {area} square meters.")
