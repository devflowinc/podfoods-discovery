import time
import json
import os
from typing import List, Dict, Any
import requests
import re
from tqdm import tqdm
import logging

from dotenv import load_dotenv

# Configure logging
logging.basicConfig(filename='loading.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

BATCH_SIZE_LIMIT = 10

def clean_chunk_html(chunk):
    html = chunk['chunk_html']
    
    # Remove extra newlines
    html = re.sub(r'\n+', ' ', html)
    
    # Convert <br> tags to newlines
    html = html.replace('<br>', '\n')
    
    # Remove any remaining HTML tags
    html = re.sub(r'<[^>]+>', '', html)
    
    # Fix the specific issue with multiple \r characters
    html = re.sub(r'(\\r\s*)+', ' ', html)
    
    # Strip leading/trailing whitespace
    html = html.strip()
    
    chunk['chunk_html'] = html
    return chunk

def read_chunks_to_create() -> List[Dict[str, Any]]:
    with open('chunks.json', 'r') as f:
        return json.load(f)

def get_configuration() -> Dict[str, str]:
    return {
        "api_key": os.getenv('TRIEVE_API_KEY'),
        "base_path": "https://api.trieve.ai",
        "dataset_id": os.getenv('TR_DATASET')
    }

def create_chunks(chunks: List[Dict[str, Any]], config: Dict[str, str]) -> None:
    url = f"{config['base_path']}/api/chunk"
    headers = {
        "TR-Dataset": config['dataset_id'],
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=chunks, headers=headers)
        response.raise_for_status()
        print(response.json())
        print(f"Successfully added batch of {len(chunks)} chunks")
        logging.info(f"Successfully added batch of {len(chunks)} chunks")
    except requests.RequestException as e:
        error_msg = (f"Failed to add batch of chunks. Status code: "
                     f"{response.status_code}\nResponse: {response.text}\n"
                     f"Error: {e}")
        print(error_msg)
        logging.error(error_msg)
        logging.error(f"Payload: {json.dumps(chunks, indent=2)}")

def read_loaded_tracking_ids() -> List[str]:
    try:
        with open('loaded.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def update_loaded_tracking_ids(new_ids: List[str]) -> None:
    loaded_ids = read_loaded_tracking_ids()
    loaded_ids.extend(new_ids)
    with open('loaded.json', 'w') as f:
        json.dump(loaded_ids, f)

def get_not_loaded_chunks(chunks: List[Dict[str, Any]], loaded_ids: List[str]) -> List[Dict[str, Any]]:
    return [chunk for chunk in chunks if chunk['tracking_id'] not in loaded_ids]

def main():
    chunks_to_create = read_chunks_to_create()
    loaded_ids = list(set(read_loaded_tracking_ids()))
    print(f"Total chunks to create: {len(chunks_to_create)}")
    logging.info(f"Total chunks to create: {len(chunks_to_create)}")

    print(f"Total loaded chunks: {len(loaded_ids)}")
    logging.info(f"Total loaded chunks: {len(loaded_ids)}")
    not_loaded_chunks = get_not_loaded_chunks(chunks_to_create, loaded_ids)
    print(f"Total remaining to create: {len(not_loaded_chunks)}")
    logging.info(f"Total remaining to create: {len(not_loaded_chunks)}")
    config = get_configuration()
    
    continue_ = input("Press enter to continue: ")
    if continue_ == "":
        pass
    else:
        exit()

    for i in tqdm(range(0, len(not_loaded_chunks), BATCH_SIZE_LIMIT), desc="Processing batches"):
        batch = not_loaded_chunks[i:i+BATCH_SIZE_LIMIT]
        cleaned_batch = [clean_chunk_html(chunk) for chunk in batch]
        
        if cleaned_batch:
            create_chunks(cleaned_batch, config)
            new_ids = [chunk['tracking_id'] for chunk in cleaned_batch]
            
            update_loaded_tracking_ids(new_ids)
            logging.info(f"Processed batch {i//BATCH_SIZE_LIMIT + 1}: "
                         f"{len(cleaned_batch)} chunks")
            time.sleep(1)
        else:
            skip_msg = f"Skipping batch {i//BATCH_SIZE_LIMIT + 1}: All chunks already loaded"
            print(skip_msg)
            logging.info(skip_msg)

if __name__ == "__main__":
    main()