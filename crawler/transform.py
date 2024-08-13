from tqdm import tqdm
import json
import logging
from validate_uniqueness import compare_pages_without_nuxt



logging.basicConfig(level=logging.INFO)

with open('staff_picks.json', 'r', encoding='utf-8') as f:
    staff_picks_data = json.load(f)

with open('holiday_picks.json', 'r', encoding='utf-8') as f:
    holiday_picks_data = json.load(f)

STAFF_PICKS = [item['href'].split('.html')[0] + '.html' for item in staff_picks_data]
HOLIDAY_PICKS = [item['href'].split('.html')[0] + '.html' for item in holiday_picks_data]

transformed_pages = {}

def process_pages(pages_file, chunks_file):
    with open(pages_file, 'r', encoding='utf-8') as f:
        pages = json.load(f)

    chunks = []
    tracking_ids = set()

    for page in tqdm(pages, desc="Processing pages"):
        
        nuxt_data = json.loads(page["nuxt"])
        product_details = nuxt_data["fetch"]["data-v-df46d3ca:0"]["record"]
        
        variants = product_details["variants"]
        for item_key, variant_details in variants.items():

            # Construct group - variant
            group_tracking_ids = [f"{page['upc']}-{item_key}"]

            boosting = {
                "boost_phrase": {
                    "boost_factor": 1.3,
                    "phrase": f"{variant_details['name']} {variant_details['brand_name']}",
                               },
                "distance_phrase": {
                    "distance_factor": 1.3,
                    "phrase": f"{variant_details['name']} {variant_details['brand_name']}",
                               }
            }

            # description chunk
            description_chunk = {
                "chunk_html": f"{variant_details['description']}<br>{variant_details['manufactured_in_str']}",
            }

            tags = []
            if page["url"].split('.html')[0] + '.html' in HOLIDAY_PICKS:
                tags.append("Holiday")
            if page["url"].split('.html')[0] + '.html' in STAFF_PICKS:
                tags.append("Staff Picks")

            tags.extend(variant_details['qualities'])

            # name chunk
            name_chunk = {
                "chunk_html": f"{variant_details['name']}",
                "image_urls": [value for _, value in variant_details["image_urls"].items()],
            }

            # ingredients chunk
            ingredients_chunk = {
                "chunk_html": f"{variant_details['ingredients']}",
            }

            # brand chunk
            brand_chunk = {
                "chunk_html": f"{variant_details['brand_name']}",
            }

            page_breadcrumb_chunk = {
                "chunk_html": f"{' > '.join(page['breadcrumb'][1:])}",
            }

            qualities_chunk = {
                "chunk_html": f"{variant_details['qualities']}",
            }

            group_chunks = {
                "description_chunk": description_chunk,
                "name_chunk": name_chunk,
                "ingredients_chunk": ingredients_chunk,
                "page_breadcrumb_chunk": page_breadcrumb_chunk,
                "qualities_chunk": qualities_chunk,
                "brand_chunk": brand_chunk
            }

            for chunk_type, chunk in group_chunks.items():
                tracking_id = f"{group_tracking_ids[0]}_{chunk_type}"
                if tracking_id in tracking_ids:
                    if not compare_pages_without_nuxt(page, transformed_pages[tracking_id]):
                        logging.error(f"Duplicate tracking_id found: {tracking_id}. Skipping this chunk.")
                        continue

                transformed_pages[tracking_id] = page
                chunk.update({
                    "tracking_id": tracking_id,
                    "boost_phrase": boosting["boost_phrase"],
                    "distance_phrase": boosting["distance_phrase"],
                    "group_tracking_ids": group_tracking_ids,
                    "tag_set": tags,
                    "link": page["url"],
                    "metadata": {
                        "name": variant_details["name"],
                        "brand": variant_details["brand_name"],
                        "upc": page["upc"],
                        "sku": item_key,
                        "is_staff_pick": page["url"].split('.html')[0] + '.html' in STAFF_PICKS,
                        "is_holiday": page["url"].split('.html')[0] + '.html' in HOLIDAY_PICKS
                    }
                })

                tracking_ids.add(tracking_id)
                chunks.append(chunk)

    # Save to chunks.json
    with open(chunks_file, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=4)

# File paths
pages_file = 'pages.json'
chunks_file = 'chunks.json'

# Process pages.json into chunks.json
process_pages(pages_file, chunks_file)