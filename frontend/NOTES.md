

- Trieve has the variants as the first-class results, rather than the products. It is not immediately clear which is the better approach, and would be easy enough to change and even provide a toggle for the user.
- Each of the variants are groups in our dataset, each group containing a chunk with different data (meant to ensure the search net catches one of them if it is relevant). Chunk types contained in each group:
    - brand_chunk
    - description_chunk (the variant description with the brand manufactured_in_str added): "Sleep Herbal Tea is a thoughtfully crafted blend of herbs with mild sedative effects which soothe the nervous system, quiet the mind, and relax the body. The herbs in Sleep Herbal Tea help you to fall asleep faster as well as promote a deeper quality of sleep so that you wake up feeling well rested and refreshed.\r\n\r\nFlavor Profile\r\nLight, Simple, Slightly Bitter, Slightly Sweet<br>Cambria, California",
    - name_chunk
    - ingredients_chunk: 
    - page_breadcrumb_chunk: "Grocery > Spice + Seasoning > Organic Turmeric - 10oz pouch/"
    - qualities_chunk: "['Soy-Free', 'Paleo', 'No Artificial Sweeteners', 'Dairy-Free', 'Vegan', 'Organic', 'Nut-Free', 'Sugar-Free', 'Non-GMO', 'Gluten-Free', '100% Natural', 'Keto', 'Plant-Based', 'Compostable Packaging', 'Sustainably Grown', '1% for the Planet']"
    


Short descriptive query:

Query: [Austin boutique tea yerba]
- Current: https://podfoods.co/products?term=Austin%20boutique%20tea%20yerba
    - The top row of results are all dry tea products. The first result is based in California, with 230 variants. The term [yerba] does not appear in the product page.
- Trieve: https://podfoods.trieve.ai/products?term=Austin%20boutique%20tea%20yerba
    - Trieve has the variants as the first-class results. The first result is the "Organic Blue Pom Acai Yerba Mate" from Austin's "Weird Beverages".

Specific variant:

Query: [Orange Blossom Almond tea]
- Current: https://podfoods.co/products?term=Orange%20Blossom%20Almond%20tea
    - The fourth result is a product with a variant that is "Know by Heart - Orange Blossom Almond White Tea".
- Trieve: https://podfoods.trieve.ai/products?term=Orange%20Blossom%20Almond%20tea
    - Same product in the 1st result.

Specific ingrediant + form:

Query: [raw honey bars]
- Current: https://podfoods.co/products?term=raw%20honey%20bars
    - The first result is "UPGRADED kalumi BEAUTYfood marine collagen bars"
    - The second is a bar with raw honey from Honeymoon Chocolates: right on the package image.
    - The third is a bar from Raw Rev. (Where the description also says: "Not a raw food.")
    - The fourth is the "Raw Chocolate Essential Bars" from Rawmio, these are vegan and do not contain raw honey.
- Trieve: https://podfoods.trieve.ai/products?term=raw%20honey%20bars
    - The first two results are variants of the Honeymoon Chocolates.
    - The third result is a bar that includes "Raw Honey" in the Ingredients.

Full text of description:

Query: [Our unique nib-to-bar process begins with the finest organic, fair-trade, single-origin cacao sourced directly from Peru, mineral-rich coconut sugar, and luscious raw cacao butter stone ground at low temperatures. Nothing else is added, allowing the complexity of flavor and sensuous texture of 70% dark chocolate to be front and center. Essentially.…pure bliss with every bite.]
- Current: https://podfoods.co/products?term=Our%20unique%20nib-to-bar%20process%20begins%20with%20the%20finest%20organic,%20fair-trade,%20single-origin%20cacao%20sourced%20directly%20from%20Peru,%20mineral-rich%20coconut%20sugar,%20and%20luscious%20raw%20cacao%20butter%20stone%20ground%20at%20low%20temperatures.%20Nothing%20else%20is%20added,%20allowing%20the%20complexity%20of%20flavor%20and%20sensuous%20texture%20of%2070%25%20dark%20chocolate%20to%20be%20front%20and%20center.%20Essentially.%E2%80%A6pure%20bliss%20with%20every%20bite.
    - Various chocolate bars in the results.
- Trieve: https://podfoods.trieve.ai/?term=Our+unique+nib-to-bar+process+begins+with+the+finest+organic,+fair-trade,+single-origin+cacao+sourced+directly+from+Peru,+mineral-rich+coconut+sugar,+and+luscious+raw+cacao+butter+stone+ground+at+low+temperatures.+Nothing+else+is+added,+allowing+the+complexity+of+flavor+and+sensuous+texture+of+70%25+dark+chocolate+to+be+front+and+center.+Essentially.%E2%80%A6pure+bliss+with+every+bite.
    - The "Raw Chocolate Essential Bar - 70% Dark" with that description is the first result. (in the fulltext, semantic, and hybrid searchtypes.)

Location name:

Query: [Arizona]
- Current: https://podfoods.co/products?term=Arizona
    - The first result from a brand based in Arizona.
    - The second result is not based in Arizona (but does mention the Sonoran desert).
    - The rest of the first row is based in Washington, Oregon, California, and Virginia.
- Trieve: https://podfoods.trieve.ai/products?term=Arizona
    - All 25 results are made by brands based in Arizona (fulltext)


Both the Trieve and the Trieve demo prioritize recall over ensuring all returned results are relevant.You could adjust the threshold for results and then provide a "See more" button to let users see more results, or simply indicate as the users do an infinite scroll that the subseqent results will be less relevant.




