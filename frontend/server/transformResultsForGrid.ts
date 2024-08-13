// Receives an array of results from the search API and transforms it into an array of objects
// that can be used to populate the ProductsGrid component

export function transformResultsForGrid(results: any[], isScrollData: boolean): any[] {
    if (results.length === 0) {
        return [];
  }
    if (isScrollData) {
        return results.reduce((acc, result, index) => {
            if (result.tracking_id.endsWith('name_chunk')) {
                acc.push({
                    id: index,
                    name: result.metadata.name,
                    imageUrl: result.image_urls[1],
                    url: result.link,
                    brand: result.metadata.brand,
                    brandUrl: result.metadata.brand,
                    tags: result.metadata.tag_set,
                });
            }
            return acc;
        }, []);
    }
    return results.reduce((acc, result, index) => {
        acc.push({
            id: index,
            name: result.group.name,
            imageUrl: result?.group?.metadata?.image_urls?.[1],
            url: result.chunks[0].chunk.link,
            brand: result.group.metadata.brand,
            tags: result.group.tag_set,
        });
        return acc;
    }, []);
}