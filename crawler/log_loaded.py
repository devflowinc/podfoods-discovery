import json

def get_loaded_chunks(tracking_id: str) -> None:
    with open('chunks.json', 'r') as f:
        chunks = json.load(f)

    loaded_chunks = []
    for chunk in chunks:
        loaded_chunks.append(chunk['tracking_id'])
        if chunk['tracking_id'] == tracking_id:
            break

    with open('loaded.json', 'w') as f:
        json.dump(loaded_chunks, f, indent=2)

    print(f"Total loaded chunks: {len(loaded_chunks)}")

    print(f"Total loaded chunks?: {len(list(set(loaded_chunks)))}")

    # Find duplicate chunks:
    duplicate_chunks = []
    for chunk in loaded_chunks:
        if loaded_chunks.count(chunk) > 1:
            duplicate_chunks.append(chunk)

    print(f"Duplicate chunks: {len(duplicate_chunks)}")
    print(f"Unique duplicate chunks: {len(set(duplicate_chunks))}")

if __name__ == "__main__":
    get_loaded_chunks("850037569403-20861_page_breadcrumb_chunk")


    
