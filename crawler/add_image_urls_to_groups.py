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

def read_chunks() -> List[Dict[str, Any]]:
    with open('chunks.json', 'r') as f:
        return json.load(f)

def get_configuration() -> Dict[str, str]:
    return {
        "api_key": os.getenv('TRIEVE_API_KEY'),
        "base_path": "https://api.trieve.ai",
        "dataset_id": os.getenv('TR_DATASET')
    }

def create_group(group: Dict[str, Any], config: Dict[str, str]) -> None:
    url = f"{config['base_path']}/api/chunk_group"
    headers = {
        "TR-Dataset": config['dataset_id'],
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=group, headers=headers)
        response.raise_for_status()
        logging.info(f"Successfully added group: {group['tracking_id']}")
    except requests.RequestException as e:
        logging.error(f"Failed to add group. Status code: {response.status_code}")
        logging.error(f"Response: {response.text}")
        logging.error("Payload:")
        logging.error(json.dumps(group, indent=2))
        logging.error(f"Error: {e}")

def main():
    chunks = read_chunks()
    config = get_configuration()

    added_groups = []

    for chunk in tqdm(chunks, desc="Processing chunks"):
        group_tracking_id = chunk["group_tracking_ids"][0]
        # if image_urls is not in chunk, continue
        if "image_urls" not in chunk:
            continue
        group_metadata = chunk.get("metadata", {})
        group_metadata["image_urls"] = chunk["image_urls"]
        group = {
            "metadata": group_metadata,
            "name": chunk.get("metadata", {}).get("name", ""),
            "tag_set": chunk.get("tag_set", []),
            "tracking_id": group_tracking_id,
            "upsert_by_tracking_id": True
        }
        if group_tracking_id in added_groups:
            continue
        added_groups.append(group_tracking_id)
        create_group(group, config)

if __name__ == "__main__":
    main()