import random

def generate_random_ips():
    prefixes = [
        "104.16", "104.17", "104.18", "104.19", "104.20", "104.21", "104.22", "104.24", "104.25", "104.26", "104.27",
        "172.66", "172.67", "162.159"
    ]
    
    ip_set = set()
    while len(ip_set) < 100:
        prefix = random.choice(prefixes)
        last_two = f"{random.randint(0, 255)}.{random.randint(0, 255)}"
        ip_set.add(f"{prefix}.{last_two}")
    
    with open("ip.txt", "w") as f:
        f.write("\n".join(ip_set))

if __name__ == "__main__":
    generate_random_ips()
