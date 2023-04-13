#1/usr/bin/env python3

vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

approved_vendors = ["cisco", "juniper", "arista"]

for vendor in vendors:
    print(f"Our vendor is {vendor}.")
    if vendor in approved_vendors:
        print("<= This is an approved vendors!", end="")

print("Our loop has completed.")
