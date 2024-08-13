import json
import os
import requests
from typing import List, Dict, Any
from tqdm import tqdm
from dotenv import load_dotenv
import logging

from upsert_to_chunks import get_product_group_tracking_id

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
        "dataset_id": os.getenv('TRIEVE_DATASET_ID_PRODUCT_LEVEL')
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

    prepared_groups = {}

    for chunk in chunks:
        group_tracking_id = get_product_group_tracking_id(chunk)
        if group_tracking_id not in prepared_groups:
            group = {
                "image_urls": [],
                "metadata": chunk.get("metadata", {}),
                "tag_set": chunk.get("tag_set", []) + ["product-level-group"],
                "tracking_id": group_tracking_id,
                "upsert_by_tracking_id": True
            }
            prepared_groups[group_tracking_id] = group
        # add tags to the group
        if chunk.get("tag_set"):
            prepared_groups[group_tracking_id]["tag_set"].extend(chunk.get("tag_set"))

        # add image_urls to the group
        if chunk["tracking_id"].endswith("_name_chunk"):
            if "image_urls" not in prepared_groups[group_tracking_id]["metadata"]:
                prepared_groups[group_tracking_id]["metadata"]["image_urls"] = chunk["image_urls"]
            else:
                prepared_groups[group_tracking_id]["metadata"]["image_urls"].extend(chunk["image_urls"])
                
        
        # page_breadcrumb_chunk
        if chunk["tracking_id"].endswith("_page_breadcrumb_chunk"):
            prepared_groups[group_tracking_id]["name"] = chunk["chunk_html"].split(" > ")[-1].strip("/")
            prepared_groups[group_tracking_id]["metadata"]["name"] = prepared_groups[group_tracking_id]["name"]
            prepared_groups[group_tracking_id]["description"] = "tag: 'product-level-group'; image_urls fixed; added full tags: 2024-07-26 12:42:18"


    for group in tqdm(prepared_groups.values(), desc="Creating groups"):
        # Convert tag_set to a set to remove duplicates
        group['tag_set'] = list(set(group['tag_set']))
        
        # Remove image_urls from group
        if 'image_urls' in group:
            del group['image_urls']

        # Remove duplicates from image_urls if present
        if 'image_urls' in group['metadata']:
            group['metadata']['image_urls'] = list(dict.fromkeys(group['metadata']['image_urls']))
        # group_without_metadata = {k: v for k, v in group.items() if k != 'metadata'}
        # print("#####################")
        # print("Group without metadata:", group_without_metadata)

        # print("Metadata:", group.get('metadata', {}))
        # # exit()
        create_group(group, config)

if __name__ == "__main__":
    main()