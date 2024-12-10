# list of customers
customer_names = [
    "  RICHA MEHTA ",
    "  jack sparrow ",
    "bahubalie   mahendra ",
    "  adA sHarMa"
]
# cleaning of names
def clean_names(names):
    cleaned_names = []
    for name in names:

        cleaned_name = " ".join(name.split()).title()
        cleaned_names.append(cleaned_name)
    return cleaned_names
# clean customer names
cleaned_customer_names = clean_names(customer_names)
# printing the claes names
print("Cleaned Customer Names:")
for name in cleaned_customer_names:
    print(name)
