<script setup lang="ts">
import { ref } from 'vue';
import ProductsGrid from "./ProductsGrid.vue";
import SortArea from "./SortArea.vue"
import { useSearchContext } from '../composables/useSearchContext';

const { tagFilters, updateTagFilters, clearTagFilters, results, isLoading, error, searchTerm, setSearchTerm } = useSearchContext();
const allResults = ref([]);

const removeTag = (tagToRemove: { label: string; value: string }) => {
  updateTagFilters(tagFilters.value.filter(tag => tag.value !== tagToRemove.value));
};
</script>


<template>
  <div class="results" data-v-d7dded24="">
    <div class="page__shelf" data-v-d7dded24="">
      <div data-v-d7dded24="">
        <div data-v-d7dded24="" class="default-catalog">
          <h1 data-v-d7dded24="" class="page__title">Catalog</h1>
        </div>
        <div v-if="searchTerm || tagFilters.length > 0" data-v-d7dded24="" class="page__description paginator">
          <!-- Showing&nbsp;
          <span data-v-d7dded24="" class="count">{{ results.length }}</span>&nbsp;over&nbsp;
          <span data-v-d7dded24="" class="total">{{ allResults.length }}</span>&nbsp;products -->
          Showing&nbsp;
          <span data-v-d7dded24="" class="count">{{ results.length }}</span>&nbsp;products
        </div>
      </div>
    </div>
    <div data-v-5c4730c9="" data-v-d7dded24="" class="filters-bar">
      <div data-v-5c4730c9="" class="chips">
        <a data-v-5c4730c9="" href="/products" class="chip nuxt-link-active has-tooltip" data-original-title="null" v-if="searchTerm">
          <span data-v-5c4730c9="" class="name pf-ellipsis">{{ searchTerm }}</span>
          <span data-v-5c4730c9="" class="times" @click="setSearchTerm('')">×</span>
        </a>
        <a data-v-5c4730c9="" href="/products" class="chip nuxt-link-active has-tooltip" data-original-title="null" v-for="tag in tagFilters" :key="tag.value">
          <span data-v-5c4730c9="" class="name pf-ellipsis">{{ tag.label }}</span>
          <span data-v-5c4730c9="" class="times" @click="removeTag(tag)">×</span>
        </a>
        <a v-if="searchTerm || tagFilters.length > 0" data-v-5c4730c9="" href="/products" class="chip reset nuxt-link-active" @click="setSearchTerm(''); clearTagFilters()">
          <span data-v-5c4730c9="" class="name">Clear all filters</span>
        </a>
      </div>
    </div>
    <SortArea />
    <div class="infinite-fetcher" data-v-a2a20c82="" data-v-d7dded24="">
        <ProductsGrid v-if="results.length > 0" />
        <p v-if="isLoading">Loading...</p>
        <p v-if="error">{{ error }}</p>
      <div class="ender" data-v-a2a20c82="" data-v-d7dded24="">
      </div>
      <div class="fetcher" data-v-a2a20c82="">
      </div>
    </div>
  </div>
</template>