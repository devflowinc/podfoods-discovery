# Exploring the Search Experience: Pod Foods

See the Trieve demo: [podfoods.trieve.ai](https://podfoods.trieve.ai)

## Introduction

Pod Foods is a wholesale grocery distribution company with a search platform for its B2B marketplace. Their current search is provided by Objective, Inc. We wanted to explore what a simple setup in Trieve could do to improve the search experience.

## Initial Survey

When we looked at the Pod Foods search experience we focused on a few core aspects where we know that we can often make a difference:

1) latency
2) relevance (including both precision and recall)
3) usability (navigation, typo-tolerance, diversity of results)

### Latency

Clicking [candy] as a search query in the dropdown runs an API call that return in 923.88 ms (per the Chrome Web Tools > Networking > Fetch > Timing). Pressing enter on [gummy bears] returns in 1.07 s.

*Preview: The same queries on the Trieve demo return in 312.21 ms and 338.61 ms (and start returning as soon as the user pauses typing for more than 200ms.)*

The user-experienced latency also depends on what is required to initiate a search. Pod Foods does not currently provide a search-as-you-type experience. You have to click the magnifying glass or press enter to see the results. This is typical for many search engine but increasingly customers are appreciating the benefits of seeing some results as they type.

### Relevance

We quickly explored queries related to Austin-based Weird Beverages, such as [[Austin boutique tea yerba]](https://podfoods.co/products?term=Austin%20boutique%20tea%20yerba) (results on left) but did not find a product matching our search intent (right).

<table>
  <tr>
    <td><img src="https://hackmd.io/_uploads/rkR4c0kqA.png" alt="Pod Foods search for [Austin boutique tea yerba]"></td>
    <td><img src="https://hackmd.io/_uploads/Sy_OoRy90.png" alt="Pod Foods product page for Organic Blue Pom Acai Yerba Mate"></td>
  </tr>
</table>

In addition to the **short descriptive query above**, we tried other query types:

**Specific variant:**

Query: [[Orange Blossom Almond tea]](https://podfoods.co/products?term=Orange%20Blossom%20Almond%20tea)

![Pod Foods search for [Orange Blossom Almond tea]](https://hackmd.io/_uploads/HkmFTA1qA.png)

The **fourth** result is a product with a variant that is "Know by Heart - Orange Blossom Almond White Tea".

**Specific ingrediant + form:**

Query: [[raw honey bars]](https://podfoods.co/products?term=raw%20honey%20bars)

![Pod Foods search for [raw honey bars]](https://hackmd.io/_uploads/S11r0C15A.png)

1) "UPGRADED kalumi BEAUTYfood marine collagen bars"
2) a bar with raw honey from Honeymoon Chocolates: right on the package image.
3) a bar from Raw Rev. (Where the description says: **"Not a raw food."**)
4) the "Raw Chocolate Essential Bars" from Rawmio, these are **vegan and do not contain raw honey**.

The next two queries were all looking for the same product, the [Rawmio Essentials 70% Cacao Dark Chocolate Bar](https://podfoods.co/raw-chocolate-essential-bars-rawmio-p10945.html?sku=26894-raw-chocolate-essential-bar-mint&i=765851)

<div style="text-align: center; width: 50%; margin: 0 auto;">
  <img src="https://hackmd.io/_uploads/H1tP7klqA.png" alt="Pod Foods product page for Rawmio Essentials 70% Cacao Dark Chocolate Bar">
</div>

Neither particular bar nor anything from the Rawmio brand return in the top results.

**Full text of description:**

Query: [[Our unique nib-to-bar process begins with the finest organic, fair-trade, single-origin cacao sourced directly from Peru, mineral-rich coconut sugar, and luscious raw cacao butter stone ground at low temperatures. Our signature raw chocolate base is then infused with just the right touch of pure peppermint essence for a mint chocolate bar like none other. Essentially.…purebliss with everybite.]](https://podfoods.co/products?term=Our%20unique%20nib-to-bar%20process%20begins%20with%20the%20finest%20organic,%20fair-trade,%20single-origin%20cacao%20sourced%20directly%20from%20Peru,%20mineral-rich%20coconut%20sugar,%20and%20luscious%20raw%20cacao%20butter%20stone%20ground%20at%20low%20temperatures.%20Our%20signature%20raw%20chocolate%20base%20is%20then%20infused%20with%20just%20the%20right%20touch%20of%20pure%20peppermint%20essence%20for%20a%20mint%20chocolate%20bar%20like%20none%20other.%20Essentially.%E2%80%A6purebliss%20with%20everybite.)

**Keywords from description:**

Query: [[organic fair-trade cacao Peru coconut sugar raw cacao butter dark chocolate]](https://podfoods.co/products?term=organic%20fair-trade%20cacao%20Peru%20coconut%20sugar%20raw%20cacao%20butter%20dark%20chocolate)

<table>
  <tr>
    <td><img src="https://hackmd.io/_uploads/r1Unf1x50.png" alt="Pod Foods search for [organic fair-trade cacao Peru coconut sugar raw cacao butter dark chocolate]"></td>
    <td><img src="https://hackmd.io/_uploads/HJ8nf1x5C.png" alt="Pod Foods search for [Our unique nib-to-bar process begins with the finest organic, fair-trade, single-origin cacao sourced directly from Peru, mineral-rich coconut sugar, and luscious raw cacao butter stone ground at low temperatures. Our signature raw chocolate base is then infused with just the right touch of pure peppermint essence for a mint chocolate bar like none other. Essentially.…purebliss with everybite.]"></td>
  </tr>
</table>

**Location name:**

Query: [[Arizona]](https://podfoods.co/products?term=Arizona)

![Pod Foods search for [Arizona]](https://hackmd.io/_uploads/r1UHVygcC.png)

- The first result is from a brand based in Arizona.
- The third result is not based in Arizona (but does mention the Sonoran desert).
- The rest of the top results are from brands based in Washington, Oregon, California, and Virginia.

Later we tried searching for [[natural toaster pastries]](https://podfoods.co/products?term=natural%20toaster%20pastries), after [a post on LinkedIn about toaster pastries from Pod's Chief Merchandising Officer](https://www.linkedin.com/posts/peter-gialantzis-a14a1b88_cpg-naturalfoods-garbage-activity-7221838546095992832-Gxd0?utm_source=share&utm_medium=member_desktop). While [toaster pastries] successfully returns the Ghetto Gastro pastries at the top, adding words like "natural", "healthy", "real fruit" to the search query does not return toaster pastries at the top.
<table>
  <tr>
    <td><img src="https://hackmd.io/_uploads/ByfbNRy5A.png" alt="Pod Foods search for [toaster pastries]"></td>
    <td><img src="https://hackmd.io/_uploads/BJhe-Ayq0.png" alt="Pod Foods search for [natural toaster pastries]"></td>
  </tr>
  <tr>
    <td><img src="https://hackmd.io/_uploads/BJ8mlCJcA.png" alt="Pod Foods search for [healthy toaster pastries]"></td>
    <td><img src="https://hackmd.io/_uploads/B1AGVRy9C.png" alt="Pod Foods search for [real fruit toaster pastries]"></td>
  </tr>
</table>

***Tip:** Your browser may support site search shortcuts. We setup a shortcut to quickly search the Pod Foods catalog from the address bar with this string: `https://podfoods.co/products?term=%s)`*!


### Usability

The searches return results at the product-level. So when you search [grapefruit weird yerba](https://podfoods.co/products?term=grapefruit%20weird%20yerba) the first result is labelled "WEIRD Iced Tea, Organic | 12 Pack By Weird Beverages". When you hover over the result, the images cycle through variants of the product. You have to click through to the product page to see the different variant names themselves. This can make it hard for a user to know if the product is what they are looking for or if the search results are relevant. This is particularly evident in the results for the [Orange Blossom Almond tea] search, where it would be hard to know that the fourth result was relevant without actually clicking.

<table>
    <tr>
  <td><img src="https://hackmd.io/_uploads/ByH_8kecR.png" alt="Pod Foods search for [grapefruit weird yerba]"></td>
  <td><img src="https://hackmd.io/_uploads/HkmFTA1qA.png" alt="Pod Foods search for [Orange Blossom Almond tea]"></td>
</tr>
</table>


The search has limited typo tolerance.

Compare the results for [apple](https://podfoods.co/products?term=apple) versus [applee](https://podfoods.co/products?term=applee). It isn't just that there are different results, it is that the latter includes mushroom jerky and pork rinds.

<table>
  <tr>
    <td><img src="https://hackmd.io/_uploads/rk9X_Je90.png" alt="Pod Foods search for [apple]"></td>
    <td><img src="https://hackmd.io/_uploads/SJ97d1ecC.png" alt="Pod Foods search for [applee]"></td>
  </tr>
</table>

The professionals at the brands and retailers using Pod Foods' website are probably using fewer alternative spellings and typos than the average person, but the impact from the lack of typo tolerance may be significant, particularly for queries for less common product names or for busy professionals rushing to find the next product to fill their shelves.

## Extract, Chunk and Group, and Load

To explore the search experience further we needed to set it up on Trieve. We gradually scrolled to the bottom of the Pod Foods product catalog, loading all the product page links, and wrote a script to use in the browser console to extract the product URLs.

```javascript
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

*We later adapted this to also extract the data to identify Holiday and Staff Pick items.*

Then on each of the 4202 product pages we extract the `__NUXT__` metadata for the different variants. We used a transfom script to make 6 simple chunks for each variant and grouped them at the variant-level and the product-level (in two datasets). The Trieve API search route we would use, [`/chunk_group/group_oriented_search`](https://docs.trieve.ai/api-reference/chunk-group/search-over-groups), finds the most relevant chunks, returning the groups as the results. In the `transform` script we also set boost phrases for the chunks (a concatenation of the variant name and the brand name), to help the search understand the importance of those strings.

The chunks:

- `description_chunk`
- `name_chunk`
- `ingredients_chunk`
- `page_breadcrumb_chunk`
- `qualities_chunk`
- `brand_chunk`

To load the datasets to Trieve for ingestion we created the groups with [`/chunk_group`](https://docs.trieve.ai/api-reference/chunk-group), each with a unique `tracking_id`, and then loaded the chunks, each with a corresponding `group_tracking_id`, with [`/chunk`](https://docs.trieve.ai/api-reference/chunk/create-or-upsert-chunk-or-chunks).

## Evaluating Difference

At Trieve we are focused on building infrastructure that helps our customers build great search experiences into their search products. Pod Foods knows their customers, and their searches, better than us. So instead of creating a context-free evaluation dataset, we wanted to just highlight the core differences between the search experiences and support their further exploration. [add screenshot tool in open source repo for them to use themselves]

### Latency

This is of course an incomplete demonstration of the latency in the current setup, only searching from the west coast.

<div style="display: flex; justify-content: space-between;">
    <div>
        Podfoods Now<br>
        <img src="https://hackmd.io/_uploads/rJemn0CY0.gif" alt="cookies" width="95%">
    </div>
    <div>
        Podfoods w/ Trieve<br>
        <img src="https://hackmd.io/_uploads/S1g730CF0.gif" alt="cookies_trieve" width="95%">        
    </div>
</div>

The results on the current search setup are cached, so going back to [cookies] after searching for something else does load without another search call.

### Relevance

Here are is a table for all of the queries mentioned above, showing the results for both the current search setup and the Trieve setup.

<table>
  <tr>
    <td>Query</td>
    <td>Current Search</td>
    <td>Trieve Search</td>
  </tr>
  <tr>
    <td>[apple]</td>
    <td><img src="https://hackmd.io/_uploads/SyPTIllq0.png" alt="podfoods-objective_apple_2024_08_06">
    <a href="https://podfoods.co/products?term=apple">[apple]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/H1-dT8xxq0.png" alt="podfoods-trieve_apple_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=apple">[apple]</a>
    </td>
  </tr>
  <tr>
    <td>[applee]</td>
    <td><img src="https://hackmd.io/_uploads/B1OpUgxqR.png" alt="podfoods-objective_applee_2024_08_06">
    <a href="https://podfoods.co/products?term=applee">[applee]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/Sy7_aIeecR.png" alt="podfoods-trieve_applee_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=applee">[applee]</a>
    </td>
  </tr>
  <tr>
    <td>[Arizona]</td>
    <td><img src="https://hackmd.io/_uploads/BJ_TLggcC.png" alt="podfoods-objective_Arizona_2024_08_06">
    <a href="https://podfoods.co/products?term=Arizona">[Arizona]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/BJOaUexqC.png" alt="podfoods-trieve_Arizona_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=Arizona">[Arizona]</a>
    </td>
  </tr>
  <tr>
    <td>[Austin boutique tea yerba]</td>
    <td><img src="https://hackmd.io/_uploads/SyluTLllc0.png" alt="podfoods-objective_Austin_boutique_tea_yerba_2024_08_06">
    <a href="https://podfoods.co/products?term=Austin%20boutique%20tea%20yerba">[Austin boutique tea yerba]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/B1uaIxec0.png" alt="podfoods-trieve_Austin_boutique_tea_yerba_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=Austin%20boutique%20tea%20yerba">[Austin boutique tea yerba]</a>
    </td>
  </tr>
  <tr>
    <td>[grapefruit weird yerba]</td>
    <td><img src="https://hackmd.io/_uploads/Sygu6Igeq0.png" alt="podfoods-objective_grapefruit_weird_yerba_2024_08_06">
    <a href="https://podfoods.co/products?term=grapefruit%20weird%20yerba">[grapefruit weird yerba]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/SJG_aLeeqC.png" alt="podfoods-trieve_grapefruit_weird_yerba_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=grapefruit%20weird%20yerba">[grapefruit weird yerba]</a>
    </td>
  </tr>
  <tr>
    <td>[healthy toaster pastries]</td>
    <td><img src="https://hackmd.io/_uploads/SJl_TLxe50.png" alt="podfoods-objective_healthy_toaster_pastries_2024_08_06">
    <a href="https://podfoods.co/products?term=healthy%20toaster%20pastries">[healthy toaster pastries]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/HJgdT8eec0.png" alt="podfoods-trieve_healthy_toaster_pastries_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=healthy%20toaster%20pastries">[healthy toaster pastries]</a>
    </td>
  </tr>
  <tr>
    <td>[natural toaster pastries]</td>
    <td><img src="https://hackmd.io/_uploads/r1z_68lgcA.png" alt="podfoods-objective_natural_toaster_pastries_2024_08_06">
    <a href="https://podfoods.co/products?term=natural%20toaster%20pastries">[natural toaster pastries]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/SkuT8ee90.png" alt="podfoods-trieve_natural_toaster_pastries_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=natural%20toaster%20pastries">[natural toaster pastries]</a>
    </td>
  </tr>
  <tr>
    <td>[Orange Blossom Almond tea]</td>
    <td><img src="https://hackmd.io/_uploads/r1-O68egqC.png" alt="podfoods-objective_Orange_Blossom_Almond_tea_2024_08_06">
    <a href="https://podfoods.co/products?term=Orange%20Blossom%20Almond%20tea">[Orange Blossom Almond tea]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/ryxOpIlg9A.png" alt="podfoods-trieve_Orange_Blossom_Almond_tea_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=Orange%20Blossom%20Almond%20tea">[Orange Blossom Almond tea]</a>
    </td>
  </tr>
  <tr>
    <td>[organic fair-trade cacao Peru coconut sugar raw cacao butter dark chocolate]</td>
    <td><img src="https://hackmd.io/_uploads/rk-uaUxe5A.png" alt="podfoods-objective_organic_fair-trade_cacao_Peru_coconut_sugar_raw_cacao_butter_dark_chocolate_2024_08_06">
    <a href="https://podfoods.co/products?term=organic%20fair-trade%20cacao%20Peru%20coconut%20sugar%20raw%20cacao%20butter%20dark%20chocolate">[organic fair-trade cacao Peru coconut sugar raw cacao butter dark chocolate]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/HyxdaIggcC.png" alt="podfoods-trieve_organic_fair-trade_cacao_Peru_coconut_sugar_raw_cacao_butter_dark_chocolate_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=organic%20fair-trade%20cacao%20Peru%20coconut%20sugar%20raw%20cacao%20butter%20dark%20chocolate">[organic fair-trade cacao Peru coconut sugar raw cacao butter dark chocolate]</a>
    </td>
  </tr>
  <tr>
    <td>[Our unique nib-to-bar process begins with the fine]</td>
    <td><img src="https://hackmd.io/_uploads/BJxuTLxg90.png" alt="podfoods-objective_Our_unique_nib-to-bar_process_begins_with_the_fine_8f57d13a_2024_08_06">
    <a href="https://podfoods.co/products?term=Our%20unique%20nib-to-bar%20process%20begins%20with%20the%20fine">[Our unique nib-to-bar process begins with the fine]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/r1b_TUexcC.png" alt="podfoods-trieve_Our_unique_nib-to-bar_process_begins_with_the_fine_8f57d13a_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=Our%20unique%20nib-to-bar%20process%20begins%20with%20the%20fine">[Our unique nib-to-bar process begins with the fine]</a>
    </td>
  </tr>
  <tr>
    <td>[raw honey bars]</td>
    <td><img src="https://hackmd.io/_uploads/SyZOT8xlc0.png" alt="podfoods-objective_raw_honey_bars_2024_08_06">
    <a href="https://podfoods.co/products?term=raw%20honey%20bars">[raw honey bars]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/rybd6LlgqC.png" alt="podfoods-trieve_raw_honey_bars_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=raw%20honey%20bars">[raw honey bars]</a>
    </td>
  </tr>
  <tr>
    <td>[real fruit toaster pastries]</td>
    <td><img src="https://hackmd.io/_uploads/SkG_T8egcC.png" alt="podfoods-objective_real_fruit_toaster_pastries_2024_08_06">
    <a href="https://podfoods.co/products?term=real%20fruit%20toaster%20pastries">[real fruit toaster pastries]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/r1vaIxlq0.png" alt="podfoods-trieve_real_fruit_toaster_pastries_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=real%20fruit%20toaster%20pastries">[real fruit toaster pastries]</a>
    </td>
  </tr>
  <tr>
    <td>[toaster pastries]</td>
    <td><img src="https://hackmd.io/_uploads/By_p8lxcR.png" alt="podfoods-objective_toaster_pastries_2024_08_06">
    <a href="https://podfoods.co/products?term=toaster%20pastries">[toaster pastries]</a>
    </td>
    <td><img src="https://hackmd.io/_uploads/Skd68ge9C.png" alt="podfoods-trieve_toaster_pastries_2024_08_06">
    <a href="https://podfoods.trieve.ai/?term=toaster%20pastries">[toaster pastries]</a>
    </td>
  </tr>
</table>

### Usability

In our search interface we add a dropdown option for users to search via different searchtypes: fulltext, semantic, and hybrid.

<div style="text-align: center;">
  <img src="https://hackmd.io/_uploads/H15JJbxqR.png" alt="searchtype dropdown" width="45%">
</div>

- <mark>TODO: URL params for searchtypes.</mark>

The table above shows screenshots for the fulltext searchtype, which uses SPLADE. There is also semantic, a dense vector search using cosine distance vectors on (here using [Jina english embeddings](https://jina.ai/news/jina-ai-launches-worlds-first-open-source-8k-text-embedding-rivaling-openai)), and hybrid, which takes in results both of the preceeding types and re-ranks with a cross-encoder model (here the [BAAI/bge-reranker-large](https://huggingface.co/BAAI/bge-reranker-large)).

- <mark>TODO: a toggle for you to switch between the product-level (the only option in the current setup in Pod Foods) and variant-level search (the default in the Trieve setup).</mark>

Typo tolerance: <mark>TODO: [discuss a test we should be able to pass once the typo tolerance is added]</mark>

## Conclusion


## Bonus

<mark>TODO? Since Pod Foods is a wholesale grocery distribution company, we've also added links for you to find the product to purchase for yourself! [a way to make it more interesting for users]</mark>
