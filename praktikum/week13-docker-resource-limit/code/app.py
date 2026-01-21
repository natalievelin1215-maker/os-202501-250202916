import time

data = []
i = 0

print("=== PRAKTIKUM DOCKER RESOURCE LIMIT ===")

try:
    while True:
        i += 1
        # Beban CPU
        x = i * i * i

        # Alokasi memori bertahap (1 MB)
        data.append("X" * 1024 * 1024)

        print(f"Iterasi: {i} | Memori terpakai: {len(data)} MB")
        time.sleep(0.2)

except MemoryError:
    print("ERROR: Memori tidak mencukupi!")
