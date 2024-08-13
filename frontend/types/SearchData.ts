export interface ScrollChunksResponse {
  chunks: Chunk[];
  total_pages: number;
}

export interface GroupOrientedSearchResponse {
  id: string;
  results: SearchResult[];
  total_pages: number;
}

interface SearchResult {
  chunks: Chunk[];
  file_id: string;
  group: Group;
}

interface Chunk {
  chunk: {
    chunk_html: string;
    content: string;
    id: string;
    link: string;
    metadata: Record<string, string>;
    time_stamp: string;
    weight: number;
  };
  highlights: string[];
  score: number;
}

interface Group {
  created_at: string;
  dataset_id: string;
  description: string;
  metadata: Record<string, string>;
  name: string;
  tag_set: string[];
  tracking_id: string;
  updated_at: string;
}
