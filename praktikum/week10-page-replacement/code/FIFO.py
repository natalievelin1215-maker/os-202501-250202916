# FIFO Page Replacement

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

memory = []
page_fault = 0
page_hit = 0

print("=== FIFO Page Replacement ===")

for page in reference_string:
    if page in memory:
        page_hit += 1
        status = "HIT"
    else:
        page_fault += 1
        status = "FAULT"
        if len(memory) < frame_size:
            memory.append(page)
        else:
            memory.pop(0)
            memory.append(page)

    print(f"Page: {page} | Frame: {memory} | {status}")

print("\nTotal Page Hit   :", page_hit)
print("Total Page Fault :", page_fault)
