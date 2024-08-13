import json
import os
import requests
from typing import List, Dict, Any
from tqdm import tqdm
from dotenv import load_dotenv
import logging

load_dotenv()

# Configure logging
logging.basicConfig(filename='loading.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

BATCH_SIZE = 120
DATASET_NAME = "TRIEVE_DATASET_ID_PRODUCT_LEVEL"

def read_chunks() -> List[Dict[str, Any]]:
    with open('chunks.json', 'r') as f:
        return json.load(f)

def get_configuration() -> Dict[str, str]:
    return {
        "api_key": os.getenv('TRIEVE_API_KEY'),
        "base_path": "https://api.trieve.ai",
        "dataset_id": os.getenv(DATASET_NAME)
    }

def upsert_chunks(chunks: List[Dict[str, Any]], config: Dict[str, str]) -> None:
    url = f"{config['base_path']}/api/chunk"
    headers = {
        "TR-Dataset": config['dataset_id'],
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=chunks, headers=headers)
        response.raise_for_status()
        logging.info(f"Successfully added batch of {len(chunks)} chunks to {DATASET_NAME}")
    except requests.RequestException as e:
        logging.error(f"Failed to add batch. Status code: {response.status_code}")
        logging.error(f"Response: {response.text}")
        logging.error(f"Error: {e}")

def get_product_group_tracking_id(chunk: Dict[str, Any]) -> str:
    return chunk["link"].split("?")[0].strip("https://podfoods.co/").strip(".html")

def main():
    chunks = read_chunks()
    config = get_configuration()

    processed_chunks = []
    for chunk in tqdm(chunks, desc="Processing chunks"):
        # get the url path as the product-level group tracking id
        product_group_tracking_id = get_product_group_tracking_id(chunk)
        # group_tracking_ids = [product_group_tracking_id, chunk["group_tracking_ids"][0]]
        chunk["group_tracking_ids"] = product_group_tracking_id
        
        # add name_chunk tag to name chunks (because they have images)
        if chunk["tracking_id"].endswith("_name_chunk"):
            chunk["tag_set"].append("name_chunk")

        # prepare the chunk for upserting
        # chunk["upsert_by_tracking_id"] = True
        processed_chunks.append(chunk)

        # If we've reached the batch size, upsert the chunks
        if len(processed_chunks) == BATCH_SIZE:
            upsert_chunks(processed_chunks, config)
            processed_chunks = []

    # Upsert any remaining chunks
    if processed_chunks:
        upsert_chunks(processed_chunks, config)

if __name__ == "__main__":
    main()