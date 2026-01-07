import os

def fifo_page_replacement(reference_string, frames_count):
    frames = []
    page_faults = 0
    page_hits = 0

    print("=== FIFO Page Replacement ===")
    for page in reference_string:
        if page in frames:
            page_hits += 1
            print("Page", page, "= HIT | Frame:", frames)
        else:
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            print("Page", page, "= FAULT | Frame:", frames)

    print("Total Page Fault (FIFO):", page_faults)
    print("Total Page Hit (FIFO):", page_hits)
    print()


def lru_page_replacement(reference_string, frames_count):
    frames = []
    page_faults = 0
    page_hits = 0

    print("=== LRU Page Replacement ===")
    for page in reference_string:
        if page in frames:
            page_hits += 1
            frames.remove(page)
            frames.append(page)
            print("Page", page, "= HIT | Frame:", frames)
        else:
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            print("Page", page, "= FAULT | Frame:", frames)

    print("Total Page Fault (LRU):", page_faults)
    print("Total Page Hit (LRU):", page_hits)
    print()


def read_reference_string(file_path):
    with open(file_path, "r") as file:
        return [int(x.strip()) for x in file.read().split(",")]


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ref_path = os.path.join(base_dir, "reference_string.txt")

    reference_string = read_reference_string(ref_path)
    frames_count = 3

    fifo_page_replacement(reference_string, frames_count)
    lru_page_replacement(reference_string, frames_count)
