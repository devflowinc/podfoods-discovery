<script setup lang="ts">
import pkg from 'lodash';
const { debounce } = pkg;
import CatalogHeaderBar from "./CatalogHeaderBar.vue";
import CatalogContent from "./CatalogContent.vue";
import { useSearchContext } from '../composables/useSearchContext'
import { watch, ref, onMounted } from 'vue'

const route = useRoute()
const router = useRouter()
const { searchTerm, setSearchTerm, pages, setPageSize, tagFilters, performScrollPull } = useSearchContext()

const isFirstLoad = ref(true)

onMounted(() => {
  if (isFirstLoad.value) {
    const queryTerm = route.query?.term?.toString() || ''
    setSearchTerm(queryTerm)
    if (route.query?.pagesize) {
      setPageSize(route.query.pagesize.toString())
    }
    if (!queryTerm) {
      performScrollPull()
    }
    isFirstLoad.value = false
  }
})

// Watch for changes in the searchTerm and pages
const debouncedUpdateRoute = debounce(([newTerm, newPages]) => {
  const query: Record<string, string | undefined> = {}
  
  if (newTerm) {
    query.term = newTerm
  } else {
    performScrollPull()
  }

  if (newPages !== '1') {
    query.pagesize = newPages
  }

  router.push({ query: Object.keys(query).length ? query : undefined })
}, 100)

watch([searchTerm, pages, tagFilters], debouncedUpdateRoute)

</script>

<template>
  <div class="catalog__wrapper">
    <div class="catalog__header">
      <CatalogHeaderBar />
      <CatalogContent />
    </div>
  </div>
</template>
