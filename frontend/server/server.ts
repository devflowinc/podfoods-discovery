import express from 'express';
import fetch from 'node-fetch';
import dotenv from 'dotenv';
import { fromNodeMiddleware } from 'h3';
import { transformResultsForGrid } from './transformResultsForGrid';
import { GroupOrientedSearchResponse, ScrollChunksResponse } from "../types/SearchData";

dotenv.config();

const app = express();
app.use(express.json());

function isSearchData(data: unknown): data is GroupOrientedSearchResponse {
    return typeof data === 'object' && data !== null && 'results' in data;
}

function isScrollData(data: unknown): data is ScrollChunksResponse {
    return typeof data === 'object' && data !== null && 'chunks' in data;
}

app.get('/api/scroll-chunks', async (req, res) => {
    const startTime = process.hrtime();

    const filtersString = req.query.filters?.toString();
    let parsedFilters;
    const filtersStartTime = process.hrtime();
    if (filtersString && filtersString !== "[]") {
        const tags = JSON.parse(filtersString);
        parsedFilters = {
            must: tags.map((tag: string) => ({
                field: "tag_set",
                match: [tag]
            })),
            must_not: [],
            should: [],
            jsonb_prefilter: true
        };
    }
    const filtersEndTime = process.hrtime(filtersStartTime);
    const filtersDuration = filtersEndTime[0] * 1000 + filtersEndTime[1] / 1e6;

    const search_body = {
        filters: parsedFilters,
        offset_chunk_id: null,  
        page_size: 75,
    };


    try {
        const datasetId = process.env.TRIEVE_DATASET_ID;
        const apiKey = process.env.TRIEVE_API_KEY;

        if (!datasetId || !apiKey) {
            console.log('Error: Environment variables are missing')
            return res.status(500).json({ error: 'Environment variables are missing' });
        }

        const headers = {
            'Content-Type': 'application/json',
            'TR-Dataset': datasetId,
            'Authorization': apiKey
        };

        const fetchStartTime = process.hrtime();
        const response = await fetch('https://api.trieve.ai/api/chunks/scroll', {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(search_body)
        });
        const fetchEndTime = process.hrtime(fetchStartTime);
        const fetchDuration = fetchEndTime[0] * 1000 + fetchEndTime[1] / 1e6;

        if (!response.ok) {
            const errorText = await response.text();
            console.log(JSON.stringify(errorText, null, 2))
            throw new Error(`API request failed: ${response.status} ${response.statusText}. ${errorText}`);
        }

        const searchData = await response.json();
        let results = [];
        const transformStartTime = process.hrtime();
        if (!isScrollData(searchData)) {
            console.log('Invalid search data received')
            console.log(JSON.stringify(searchData, null, 2))
        } else {
            results = transformResultsForGrid(searchData.chunks, true);
        }
        const transformEndTime = process.hrtime(transformStartTime);
        const transformDuration = transformEndTime[0] * 1000 + transformEndTime[1] / 1e6;

        const endTime = process.hrtime(startTime);
        const duration = endTime[0] * 1000 + endTime[1] / 1e6;

        res.setHeader(
            'Server-Timing',
            `total;dur=${duration},fetch;dur=${fetchDuration},` +
            `transform;dur=${transformDuration},filters;dur=${filtersDuration}`
        );
        res.json(results);
    } catch (error) {
        console.error('Error fetching data:', error);
        if (error instanceof Error) {
            res.status(500).json({
                error: 'Internal Server Error',
                details: error.message
            });
        } else {
            res.status(500).json({
                error: 'Internal Server Error',
                details: 'An unknown error occurred'
            });
        }
    }
});

app.get('/api/search', async (req, res) => {
    const startTime = process.hrtime();

    const query = req.query.q?.toString().toLowerCase();
    const searchType = req.query.searchType?.toString().toLowerCase();
    const filtersString = req.query.filters?.toString();
    let parsedFilters: { must?: Array<{ field: string; match: string[] }> } = {};
    const filtersStartTime = process.hrtime();
    if (filtersString && filtersString !== "[]") {
        try {
            const tags: string[] = JSON.parse(filtersString);
            if (Array.isArray(tags) && tags.length > 0) {
                parsedFilters.must = tags.map(tag => ({
                    field: "tag_set",
                    match: [tag]
                }));
            }
        } catch (error) {
            console.error('Error parsing filters:', error);
        }
    }
    const filtersEndTime = process.hrtime(filtersStartTime);
    const filtersDuration = filtersEndTime[0] * 1000 + filtersEndTime[1] / 1e6;

    const parseStartTime = process.hrtime();
    const search_body: { 
        query: string; 
        filters?: any; 
        search_type: string; 
        page: number; 
        page_size: number; 
    } = {
        query: query ?? '',
        filters: parsedFilters,
        search_type: searchType ?? 'group_oriented_search',
        page: 1,
        page_size: 25,
    };

    if (!parsedFilters) {
        delete search_body.filters;
    }
    const parseEndTime = process.hrtime(parseStartTime);
    const parseDuration = parseEndTime[0] * 1000 + parseEndTime[1] / 1e6;
    
    try {
        const datasetId = process.env.TRIEVE_DATASET_ID;
        const apiKey = process.env.TRIEVE_API_KEY;

        if (!datasetId || !apiKey) {
            console.log('Error: Environment variables are missing')
            return res.status(500).json({ error: 'Environment variables are missing' });
        }

        const headers = {
            'Content-Type': 'application/json',
            'TR-Dataset': datasetId,
            'Authorization': apiKey
        };
        const body = JSON.stringify(search_body);
        const fetchStartTime = process.hrtime();
        const response = await fetch('https://api.trieve.ai/api/chunk_group/group_oriented_search', {
            method: 'POST',
            headers: headers,
            body: body
        });
        const fetchEndTime = process.hrtime(fetchStartTime);
        const fetchDuration = fetchEndTime[0] * 1000 + fetchEndTime[1] / 1e6;

        if (!response.ok) {
            const errorText = await response.text();
            console.log(JSON.stringify(errorText, null, 2))
            throw new Error(`API request failed: ${response.status} ${response.statusText}. ${errorText}`);
        }

        const jsonParseStartTime = process.hrtime();
        const searchData = await response.json();
        const jsonParseEndTime = process.hrtime(jsonParseStartTime);
        const jsonParseDuration = jsonParseEndTime[0] * 1000 + jsonParseEndTime[1] / 1e6;

        if (!isSearchData(searchData)) {
            throw new Error('Invalid search data received');
        }
        const transformStartTime = process.hrtime();
        const results = transformResultsForGrid(searchData.results, false);
        const transformEndTime = process.hrtime(transformStartTime);
        const transformDuration = transformEndTime[0] * 1000 + transformEndTime[1] / 1e6;
        
        const endTime = process.hrtime(startTime);
        const duration = endTime[0] * 1000 + endTime[1] / 1e6;

        res.setHeader(
            'Server-Timing',
            `total;dur=${duration},fetch;dur=${fetchDuration},` +
            `transform;dur=${transformDuration},filters;dur=${filtersDuration},` +
            `parse;dur=${parseDuration},jsonParse;dur=${jsonParseDuration}`
        );
        res.json(results);
    } catch (error) {
        console.error('Error fetching data:', error);
        if (error instanceof Error) {
            res.status(500).json({ 
                error: 'Internal Server Error', 
                details: error.message 
            });
        } else {
            res.status(500).json({ 
                error: 'Internal Server Error', 
                details: 'An unknown error occurred' 
            });
        }
    }
});

export default fromNodeMiddleware(app);