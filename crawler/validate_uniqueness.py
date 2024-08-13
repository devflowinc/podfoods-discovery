import json

def check_unique_upcs(pages_file):
    with open(pages_file, 'r', encoding='utf-8') as f:
        pages = json.load(f)

    tracking_ids = {}
    duplicate_pages = []
    for page in pages:
        nuxt_data = json.loads(page["nuxt"])
        product_details = nuxt_data["fetch"]["data-v-df46d3ca:0"]["record"]
        variants = product_details["variants"]
        
        for item_key, variant_details in variants.items():
            combined_key = page["upc"] + item_key
            if combined_key in tracking_ids:
                existing_page = tracking_ids[combined_key]
                if compare_pages_without_nuxt(page, existing_page):
                    duplicate_pages.append(page)
                else:
                    print(f"Duplicate UPC but different item found: {page['upc']}")
                    print(f"https://podfoods.co/products?term={page['upc']}")
            tracking_ids[combined_key] = page

    reused_upcs = [upc for upc, page in tracking_ids.items() if list(tracking_ids).count(upc) > 1]
    print(f"Re-used UPCs: {len(reused_upcs)}")
    print(f"Duplicate pages: {len(duplicate_pages)}")

def compare_pages_without_nuxt(page1, page2):
    page1_copy = {k: v for k, v in page1.items() if k != "nuxt"}
    page2_copy = {k: v for k, v in page2.items() if k != "nuxt"}
    return page1_copy == page2_copy
    
if __name__ == "__main__":
    # Check uniqueness of UPCs in pages.json
    check_unique_upcs('pages.json')

