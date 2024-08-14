import { transformResultsForGrid } from "./transformResultsForGrid";
import type {
  GroupOrientedSearchResponse,
  ScrollChunksResponse,
} from "@/types/SearchData";

const datasetId = import.meta.env.VITE_TRIEVE_DATASET_ID;
const apiKey = import.meta.env.VITE_TRIEVE_API_KEY;
if (!datasetId || !apiKey) {
  console.log("Error: Environment variables are missing");
  throw new Error("Environment variables are missing");
}

function isSearchData(data: unknown): data is GroupOrientedSearchResponse {
  return typeof data === "object" && data !== null && "results" in data;
}

function isScrollData(data: unknown): data is ScrollChunksResponse {
  return typeof data === "object" && data !== null && "chunks" in data;
}

export const scrollChunks = async (filters: string[]) => {
  let parsedFilters;
  if (filters.length) {
    parsedFilters = {
      must: filters.map((tag: string) => ({
        field: "tag_set",
        match: [tag],
      })),
      must_not: [],
      should: [],
      jsonb_prefilter: true,
    };
  }

  const search_body = {
    filters: parsedFilters,
    offset_chunk_id: null,
    page_size: 75,
  };

  try {
    if (!datasetId || !apiKey) {
      console.log("Error: Environment variables are missing");
      throw new Error("Environment variables are missing");
    }

    const headers = {
      "Content-Type": "application/json",
      "TR-Dataset": datasetId,
      Authorization: apiKey,
    };

    const response = await fetch("https://api.trieve.ai/api/chunks/scroll", {
      method: "POST",
      headers: headers,
      body: JSON.stringify(search_body),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.log(JSON.stringify(errorText, null, 2));
      throw new Error(
        `API request failed: ${response.status} ${response.statusText}. ${errorText}`
      );
    }

    const searchData = await response.json();
    let results = [];
    if (!isScrollData(searchData)) {
      console.log("Invalid search data received");
      console.log(JSON.stringify(searchData, null, 2));
    } else {
      results = transformResultsForGrid(searchData.chunks, true);
    }
    return results;
  } catch (error) {
    console.error("Error fetching data:", error);
    if (error instanceof Error) {
      throw new Error(error.message);
    } else {
      throw new Error("An unknown error occurred");
    }
  }
};

export const groupOrientedSearch = async (
  query: string,
  pages: string,
  searchType: string,
  filters: string[]
) => {
  const queryLower = query.toLowerCase();
  const searchTypeLower = searchType?.toLowerCase();
  let parsedFilters: { must?: Array<{ field: string; match: string[] }> } = {};

  if (filters && filters.length > 0) {
    try {
      const tags: string[] = filters;
      if (Array.isArray(tags) && tags.length > 0) {
        parsedFilters.must = tags.map((tag) => ({
          field: "tag_set",
          match: [tag],
        }));
      }
    } catch (error) {
      console.error("Error parsing filters:", error);
    }
  }
  const search_body: {
    query: string;
    filters?: any;
    search_type: string;
    page: number;
    page_size: number;
  } = {
    query: queryLower ?? "",
    filters: parsedFilters,
    search_type: searchTypeLower ?? "group_oriented_search",
    page: 1,
    page_size: 25,
  };

  if (!parsedFilters) {
    delete search_body.filters;
  }

  try {
    const headers = {
      "Content-Type": "application/json",
      "TR-Dataset": datasetId,
      Authorization: apiKey,
    };
    const body = JSON.stringify(search_body);
    const response = await fetch(
      "https://api.trieve.ai/api/chunk_group/group_oriented_search",
      {
        method: "POST",
        headers: headers,
        body: body,
      }
    );

    if (!response.ok) {
      const errorText = await response.text();
      console.log(JSON.stringify(errorText, null, 2));
      throw new Error(
        `API request failed: ${response.status} ${response.statusText}. ${errorText}`
      );
    }

    const searchData = await response.json();

    if (!isSearchData(searchData)) {
      throw new Error("Invalid search data received");
    }
    const results = transformResultsForGrid(searchData.results, false);
    return results;
  } catch (error) {
    console.error("Error fetching data:", error);
    if (error instanceof Error) {
      throw new Error(error.message);
    } else {
      throw new Error("An unknown error occurred");
    }
  }
};
