<p align="center">
  <img height="100" src="https://cdn.trieve.ai/trieve-logo.png?" alt="Trieve Logo">
</p>
<p align="center">
<strong><a href="https://dashboard.trieve.ai">Sign Up (1k chunks free)</a> | <a href="https://docs.trieve.ai">Documentation</a> | <a href="https://cal.com/nick.k/meet">Meet With a Founder</a> | <a href="https://discord.gg/eBJXXZDB8z">Discord</a> | <a href="https://matrix.to/#/#trieve-general:trieve.ai">Matrix</a>
</strong>
</p>

<p align="center">
    <a href="https://github.com/devflowinc/trieve/stargazers">
        <img src="https://img.shields.io/github/stars/devflowinc/trieve.svg?style=flat&color=yellow" alt="Github stars"/>
    </a>
    <a href="https://github.com/devflowinc/trieve/issues">
        <img src="https://img.shields.io/github/issues/devflowinc/trieve.svg?style=flat&color=success" alt="GitHub issues"/>
    </a>
    <a href="https://discord.gg/CuJVfgZf54">
        <img src="https://img.shields.io/discord/1130153053056684123.svg?label=Discord&logo=Discord&colorB=7289da&style=flat" alt="Join Discord"/>
    </a>
    <a href="https://matrix.to/#/#trieve-general:trieve.ai">
        <img src="https://img.shields.io/badge/matrix-join-purple?style=flat&logo=matrix&logocolor=white" alt="Join Matrix"/>
    </a>
</p>

<h2 align="center">
    <b>Trieve Pod Foods Discovery Project</b>
</h2>

![Screenshot of a search for [Texas boutique tea yerba] on podfoods.trieve.ai](https://cdn.trieve.ai/github/trieve-podfoods-demo-screenshot.webp?)

Preview the output of this project at [podfoods.trieve.ai](https://podfoods.trieve.ai)

## About

Pod Foods co-founders, Fiona Lee and Larissa Russell decided to build their company after identifying how they might address the distribution challenges they experienced with their first business selling cookies.

Pod Foods is currently disrupting grocery distribution with their marketplace enabling retailers and emerging brands to connect.

### Search For More Bespoke, Health-Oriented, and New Products is a Fun Challenge

Keyword search is enough for the vast majority of queries when someone knows what they're looking for, but less so when you're exploring. Pod Foods is really interesting because they are likely to have a significant number of users **exploring** rather than checking if a specific item is present.

Trieve provides vector based search for semantic, fulltext, and hybrid modes which is uniquely well-suited to Pod Foods' dataset.

### Areas We Tried To Improve

We made a few design decisions to help with the search experience:

- Variant-level search results: Instead of seeing product groups with multiple variants (like seeing "August Tea Bags" when searching for [Orange Blossom Almond tea]), you'll see individual variant most relevant to your query.
- Precise recall for descriptive queries: We've simply included the ingredients, brand names, descriptions, and a bit of other metadata in the index to ensure that searching for something like [real fruit toaster pastries] will return toaster pastries that contain real fruit (instead of fruit shakes).
- Search types: Switch between semantic, fulltext, and hybrid search modes to refine your search experience.
- Incremental search: As you type, the search will update to show your results.

## How To Contribute

Set up your local dev environment following the guide in the next section, fork the repo, and post a PR with your changes!

If you are doing something more significant and want to get a hold of us beforehand then send an email to [humans@trieve.ai](mailto:humans@trieve.ai) or ping us on our Matrix or Discord linked in the badges at the top of this README.

## How To Set up Local Dev

### Environment Variables

`.env.dist` in the root folder contains a read-only API key and dataset-ID. These envs will work out of the box for the `frontend`. However, if you want to run the crawler, you will need to get an API key with write permissions. Reach out to us at <humans@trieve.ai> or follow our [quickstart guide](https://docs.trieve.ai/getting-started/quickstart) to create a new dataset.

Run the following to setup `.env` for the frontend:

```
cp .env.dist ./frontend/.env
```

### Run Frontend Locally

Run the frontend of this application:

```
cd frontend
yarn
yarn dev
```

### Run the Crawler

Follow the below steps to build and refine your own dataset. The `crawler` folder contains the individual python scripts used to crawl, transform, and load the data to Trieve.

First navigate to the `crawler` folder, create a virtual environment, and install the dependencies:
```
cd crawler
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Collect product page links

Manually scroll through the product Catalog page ([podfoods.co/products](https://podfoods.co/products)) and then use this script in the developer console to collect the product links: 

```
const articleData = Array.from(document.getElementsByTagName('article'))
    .map(article => {
        // Get the first href in the article, if any
        const firstLink = article.querySelector('a');
        const href = firstLink ? firstLink.href : null;

        return {
            text: article.textContent.trim(),
            href: href
        };
    });

console.log(articleData);

// Copy to clipboard
copy(JSON.stringify(articleData, null, 2));
```

We saved this to `products.json`. (We later re-ran this process with a modified script to also identify which products were tagged as staff picks and which were tagged as holiday items—saved in `staff_picks.json` and `holiday_picks.json` respectively. We also created the `popularity_sort.json` file to sort the products by popularity (not implemented in the live demo).)

#### Crawling

`crawl.py` is the main script for crawling the product pages. It uses Selenium to scroll through the product pages and save the data to the `pages.json` file. This is a small crawl, with minimal costs to the subject site. On each of the 4202 product pages we extract the __NUXT__ metadata for the different variants.

#### Transforming

`transform.py` is the script for transforming the data from the `pages.json`, `staff_picks.json`, and `holiday_picks.json` files to chunks in `chunks.json`. We used the transform script to make 6 simple chunks for each variant and grouped them at the variant-level and the product-level (in two datasets—only the first is in the live demo). You can see the exact implementation of the chunks in the `transform.py` file.

Chunks:

- description_chunk
- name_chunk
- ingredients_chunk
- page_breadcrumb_chunk
- qualities_chunk
- brand_chunk

Note: The chunk construction could be much more data-driven or based on a deeper understanding of the particular search practices of Pod Foods users. We did not optimize chunk construction for this demo—the search quality is a result of this naive baseline approach.

##### Grouping

Since we planned to use the `group_oriented_search` route in the Trieve API ([API reference: Search Over Groups](https://docs.trieve.ai/api-reference/chunk-group/search-over-groups)), we needed to group the chunks with the `group_tracking_id`. Depending on how you group the chunks, you can edit the `group_tracking_id` construction in the `transform.py` file.

#### Loading

**Groups.** In this project we developed the group tracking IDs in the transform and then read from the `chunks.json` file to create the groups themselves (and load them to Trieve ([API reference: Create or Upsert Group or Groups](https://docs.trieve.ai/api-reference/chunk-group/create-or-upsert-group-or-groups))) in the `create_groups.py` and `create_products_groups.py` (not implemented in live demo) files. We also developed a script to confirm the tracking IDs were unique: `validate_uniqueness.py`.

**Chunks.** We loaded the chunks to Trieve with the `load.py` script (and upserted to update them as we refined the chunking strategy with the `upsert_to_chunks.py` script ([API reference: Create or Upsert Chunk or Chunks](https://docs.trieve.ai/api-reference/chunk/create-or-upsert-chunk-or-chunks))).