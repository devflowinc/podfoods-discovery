import { ref, provide, inject, watch, type Ref } from 'vue'
import { groupOrientedSearch, scrollChunks } from '../utils/search'

interface SearchContext {
  searchTerm: Ref<string>
  results: Ref<any[]>
  isLoading: Ref<boolean>
  error: Ref<string | null>
  pages: Ref<string>
  searchType: Ref<string>
  searchTypeOptions: Ref<Array<{ label: string, value: string }>>
  setSearchTerm: (term: string) => void
  setPageSize: (pages: string) => void
  updateSearchType: (newSearchType: string) => void
  sortOrder: Ref<string>
  sortOptions: Ref<Array<{ label: string, value: string }>>
  updateSortOrder: (newSortOrder: string) => void
  tagFilters: Ref<Array<{ label: string, value: string }>>
  updateTagFilters: (newTagFilters: Array<{ label: string, value: string }>) => void
  removeTagFilters: (tagToRemove: { value: string }) => void
  clearTagFilters: () => void
  performScrollPull: () => void
}

const SearchSymbol = Symbol()

export function provideSearchContext() {
  const context: SearchContext = {
    tagFilters: ref([]),
    updateTagFilters: (newTagFilters: Array<{ label: string, value: string }>) => {
      if (!Array.isArray(newTagFilters)) {
        console.error('Invalid input: newTagFilters must be an array');
        return;
      }
      const validTagFilters = newTagFilters.filter(tag => 
        typeof tag === 'object' && 
        typeof tag.label === 'string' && 
        typeof tag.value === 'string'
      );
      context.tagFilters.value = validTagFilters;
    },
    removeTagFilters: (tagToRemove: { value: string }) => {
      if (typeof tagToRemove !== 'object' || typeof tagToRemove.value !== 'string') {
        console.error('Invalid input: tagToRemove must be an object with a string value');
        return;
      }
      context.tagFilters.value = context.tagFilters.value.filter(tag => 
        tag.value !== tagToRemove.value
      );
    },
    clearTagFilters: () => {
      context.tagFilters.value = []
    },
    sortOrder: ref('Order by Popularity'),
    sortOptions: ref([
      { label: 'Order by Popularity', value: 'Order by Popularity' },
      { label: 'Order by Relevance', value: 'Order by Relevance' }
    ]),
    updateSortOrder: (newSortOrder: string) => {
      context.sortOrder.value = newSortOrder
    },
    searchTerm: ref(''),
    searchType: ref('fulltext'),
    updateSearchType: (newSearchType: string) => {
      context.searchType.value = newSearchType
    },
    searchTypeOptions: ref([
      { label: 'Fulltext', value: 'fulltext' },
      { label: 'Semantic', value: 'semantic' },
      { label: 'Hybrid', value: 'hybrid' }
    ]),
    results: ref([]),
    isLoading: ref(false),
    error: ref(null),
    pages: ref('1'),
    setSearchTerm: (term: string) => {
      context.searchTerm.value = term
    },
    setPageSize: (pages: string) => {
      context.pages.value = pages
    },
    performScrollPull: () => {
      performScrollPull()
    }
  }

  provide(SearchSymbol, context)


  const performSearch = async () => {
    const query = context.searchTerm.value.trim()
    if (query === '') {
      context.results.value = []
      return
    }

    context.isLoading.value = true
    context.error.value = null
    console.log('Searching for:', query)
    try {
      const filters = context.tagFilters.value.map(tag => tag.label)
      const response = await groupOrientedSearch(query, context.pages.value, context.searchType.value, filters)
      console.log('Search response:', response)
      
      const data = await response
      console.log('Search data:', data)
      context.results.value = data
    } catch (err) {
      console.error('Search error:', err)
      context.error.value = 'An error occurred while searching'
    } finally {
      context.isLoading.value = false
    }
  }

  let debounceTimeout: ReturnType<typeof setTimeout> | null = null

  watch(context.searchTerm, (newQuery) => {
    if (debounceTimeout) {
      clearTimeout(debounceTimeout)
    }

    debounceTimeout = setTimeout(performSearch, 300) // Debounce delay of 300ms
  }, { immediate: true })

  watch(context.tagFilters, () => {
    performSearch()
  })

  watch(context.searchType, () => {
    performSearch()
  })

  const performScrollPull = async () => {
    context.isLoading.value = true
    context.error.value = null
    try {
      const filters = context.tagFilters.value.map(tag => tag.label)
      const response = await scrollChunks(filters)
      const data = await response
      console.log('Scroll pull data:', data)
      context.results.value = data
    } catch (err) {
      console.error('Scroll pull error:', err)
      context.error.value = err instanceof Error ? err.message : 'An error occurred while fetching results'
    } finally {
      context.isLoading.value = false
    }
  }


  return context
}

export function useSearchContext() {
  const context = inject<SearchContext>(SearchSymbol)
  if (!context) {
    throw new Error('useSearchContext must be used within a provider')
  }
  return context
}