<script setup lang="ts">
import { ref } from 'vue';
import CategoriesBar from "./CategoriesBar.vue"
import SearchBox from "./SearchBox.vue"

const isFocused = ref(false);
const isSearching = ref(false);

const toggleSearch = () => {
    isSearching.value = !isSearching.value;
    isFocused.value = isSearching.value;
};
</script>

<template>
    <div class="catalog-header-bar">
        <div id="top-header-bar" :class="['top', 'flex', 'inner-gap', { searching: isSearching }]" data-v-4ac4b396=""
            style="background: rgb(253, 244, 255); align-items: center;">
            <div class="logo" data-v-4ac4b396=""
                style="margin: 5px; margin-right: 30px; padding-right: 10px; background-color: white; border-radius: 8px; max-width: 200px;">
                <a href="/" title="Trieve Search Demo - Pod Foods" class="nuxt-link-active" data-v-4ac4b396="">
                    <img src="/img/trieve-podfoods-logo.png" data-v-4ac4b396="" style="width: 100%; height: auto;">
                </a>
            </div>
            <div class="search" data-v-4ac4b396="" style="flex-grow: 1; justify-content: center;">
                <div data-v-4321adf5="" data-v-4ac4b396="" class="search-box" style="width: 100%; max-width: 600px;">
                    <SearchBox :isFocused="isFocused" />
                </div>
            </div>
            <a href="#" class="search-toggler" data-v-4ac4b396="" style="margin-left: auto;"
                @click.prevent="toggleSearch">
                <i :class="['pf-icon', 'bx', { 'bx-search': !isSearching, 'bx-x': isSearching }]"
                    data-v-4ac4b396=""></i>
            </a>
            <div 
                style="height: auto; border: 1px solid rgb(217 70 239); border-radius: 5px; margin: 2px; padding: 2px; background-color: rgb(253 244 255); display: flex; flex-direction: column;"
                >
                <a href="https://github.com/devflowinc/podfoods-discovery/" 
                   title="GitHub" 
                   data-v-4ac4b396=""
                   class="hover-link">
                    <i class="bx bxl-github mr-1"></i>
                    <span class="font-semibold">GitHub</span>
                </a>
                <a href="https://trieve.ai/podfoods-relevance-blog/" 
                   title="Blogpost: Search Relevance Exploration"
                   data-v-4ac4b396=""
                   class="hover-link"
                   >
                    <i class="bx bx-book mr-1"></i>
                    <span class="font-semibold">Blogpost</span>
                </a>
            </div>
        </div>

        <div class="bottom flex" data-v-4ac4b396="">
            <div class="expander" data-v-4ac4b396=""></div>
            <div class="menu" data-v-4ac4b396="">
                <a href="/" title="Catalog" class="nuxt-link-active" data-v-4ac4b396="">Catalog</a>
                <a href="/" title="Brands" data-v-4ac4b396="" class="">Brands</a>
            </div>
        </div>
        <CategoriesBar />
    </div>
</template>