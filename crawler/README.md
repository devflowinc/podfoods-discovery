Manually scrolled through the products page and then typed in: 

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

Saved to `products.json`

## Crawling



## Transforming the data

adding staff picks and holiday items

re-used the js 


 In the load we did some deduplication verification. The initial pull did get duplicated items, but the tracking ID we set is unique.

## Testing queries

frozen fish