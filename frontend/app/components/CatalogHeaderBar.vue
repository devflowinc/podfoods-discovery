<script setup lang="ts">
import { ref } from 'vue';
import CategoriesBar from "./CategoriesBar.vue"
import SearchBox from "./SearchBox.vue"

const isFocused = ref(false);

</script>

<template>
    <div class="catalog-header-bar">
        <div class="top flex inner-gap" data-v-4ac4b396="" style="background: rgb(253, 244, 255);">
            <div
                class="logo"
                data-v-4ac4b396=""
                style="margin: 5px; background: white; border-radius: 8px;"
                >
                <a href="/" title="Trieve Search Demo - Pod Foods" class="nuxt-link-active"
                data-v-4ac4b396=""><img src="/img/trieve-podfoods-logo.png" data-v-4ac4b396="">
                </a>
            </div>
            <div class="search" data-v-4ac4b396="">
                <div data-v-4321adf5="" data-v-4ac4b396="" class="search-box">
                    <div v-if="isFocused" data-v-4321adf5="" class="search-box__mask">
</div>
                    
                    <SearchBox :isFocused="isFocused" />
                    <span v-if="isFocused" data-v-4321adf5="" class="search-box__popover" style="">
                        <div role="tooltip" id="el-popover-7036" aria-hidden="false"
                            class="el-popover el-popper search-box-popper" style="width: 640px;">
                            <section data-v-678bd2ad="" data-v-4321adf5="" class="search-section trending-keywords">
                                <div data-v-678bd2ad="" class="search-section__content"><a data-v-678bd2ad=""
                                        href="/products?term=gummies" class="nuxt-link-active">
                                        <div data-v-678bd2ad="" class="stamp">
                                            <div data-v-678bd2ad="" class="stamp__icon"><i data-v-678bd2ad=""
                                                    class="bx bx-trending-up"></i>
</div>
                                            <div data-v-678bd2ad="" class="stamp__info">
                                                <div data-v-678bd2ad="" class="stamp__title">gummies</div>
                                            </div>
                                            <div data-v-678bd2ad="" class="stamp__type">Trending in Jul</div>
                                        </div>
                                    </a><a data-v-678bd2ad="" href="/products?term=candy" class="nuxt-link-active">
                                        <div data-v-678bd2ad="" class="stamp">
                                            <div data-v-678bd2ad="" class="stamp__icon"><i data-v-678bd2ad=""
                                                    class="bx bx-trending-up"></i>
</div>
                                            <div data-v-678bd2ad="" class="stamp__info">
                                                <div data-v-678bd2ad="" class="stamp__title">candy</div>
                                            </div>
                                            <div data-v-678bd2ad="" class="stamp__type">Trending in Jul</div>
                                        </div>
                                    </a><a data-v-678bd2ad="" href="/products?term=sea%20moss" class="nuxt-link-active">
                                        <div data-v-678bd2ad="" class="stamp">
                                            <div data-v-678bd2ad="" class="stamp__icon"><i data-v-678bd2ad=""
                                                    class="bx bx-trending-up"></i>
</div>
                                            <div data-v-678bd2ad="" class="stamp__info">
                                                <div data-v-678bd2ad="" class="stamp__title">sea moss</div>
                                            </div>
                                            <div data-v-678bd2ad="" class="stamp__type">Trending in Jul</div>
                                        </div>
                                    </a><a data-v-678bd2ad="" href="/products?term=non-alcoholic"
                                        class="nuxt-link-active">
                                        <div data-v-678bd2ad="" class="stamp">
                                            <div data-v-678bd2ad="" class="stamp__icon"><i data-v-678bd2ad=""
                                                    class="bx bx-trending-up"></i>
</div>
                                            <div data-v-678bd2ad="" class="stamp__info">
                                                <div data-v-678bd2ad="" class="stamp__title">non-alcoholic</div>
                                            </div>
                                            <div data-v-678bd2ad="" class="stamp__type">Trending in Jul</div>
                                        </div>
                                    </a><a data-v-678bd2ad="" href="/products?term=adaptogen" class="nuxt-link-active">
                                        <div data-v-678bd2ad="" class="stamp">
                                            <div data-v-678bd2ad="" class="stamp__icon"><i data-v-678bd2ad=""
                                                    class="bx bx-trending-up"></i>
</div>
                                            <div data-v-678bd2ad="" class="stamp__info">
                                                <div data-v-678bd2ad="" class="stamp__title">adaptogen</div>
                                            </div>
                                            <div data-v-678bd2ad="" class="stamp__type">Trending in Jul</div>
                                        </div>
                                    </a><a data-v-678bd2ad="" href="/products?term=supplements"
                                        class="nuxt-link-active">
                                        <div data-v-678bd2ad="" class="stamp">
                                            <div data-v-678bd2ad="" class="stamp__icon"><i data-v-678bd2ad=""
                                                    class="bx bx-trending-up"></i>
</div>
                                            <div data-v-678bd2ad="" class="stamp__info">
                                                <div data-v-678bd2ad="" class="stamp__title">supplements</div>
                                            </div>
                                            <div data-v-678bd2ad="" class="stamp__type">Trending in Jul</div>
                                        </div>
                                    </a>
</div>
                            </section>
                            <section data-v-991ff42e="" data-v-4321adf5="" class="search-section recent-keywords">
                                <div data-v-991ff42e="" class="search-section__header">
                                    <div data-v-991ff42e="" class="search-section__title">Recently searched keywords
                                    </div>
                                    <div data-v-991ff42e="" class="search-section__actions"><a data-v-991ff42e=""
                                            href="#" class="search-section__clear">Clear</a>
</div>
                                </div>
                                <div data-v-991ff42e="" class="search-section__content"><a data-v-991ff42e=""
                                        href="/products?term=test" class="nuxt-link-exact-active nuxt-link-active"
                                        aria-current="page">test</a><a data-v-991ff42e=""
                                        href="/products?term=orange%20colored%20can%20austin%20tea"
                                        class="nuxt-link-active">orange colored can austin tea</a><a data-v-991ff42e=""
                                        href="/products?term=Orange%20colored%20can%20austin%20tea"
                                        class="nuxt-link-active">Orange colored can austin tea</a><a data-v-991ff42e=""
                                        href="/products?term=Orange%20colored%20austin%20tea"
                                        class="nuxt-link-active">Orange colored austin tea</a><a data-v-991ff42e=""
                                        href="/products?term=Orange%20colored%20%20tea" class="nuxt-link-active">Orange
                                        colored tea</a><a data-v-991ff42e=""
                                        href="/products?term=Orange%20colored%20Blossom%20Almond%20tea"
                                        class="nuxt-link-active">Orange colored Blossom Almond tea</a><a
                                        data-v-991ff42e="" href="/products?term=Austin%20bougie%20tea%20yerba"
                                        class="nuxt-link-active">Austin bougie tea yerba</a><a data-v-991ff42e=""
                                        href="/products?term=Austin%20tea%20yerba" class="nuxt-link-active">Austin tea
                                        yerba</a><a data-v-991ff42e="" href="/products?term=gummies"
                                        class="nuxt-link-active">gummies</a>
</div>
                            </section>
                            <section data-v-4321adf5="" class="search-section brands">
                                <div class="search-section__header">
                                    <div class="search-section__title">Recently browsed brands</div>
                                    <div class="search-section__actions"><a href="#"
                                            class="search-section__clear">Clear</a>
</div>
                                </div>
                                <div class="search-section__content">
                                    <div class="search-grid">
                                    </div>
                                </div>
                            </section>
                            <section data-v-4321adf5="" class="search-section products">
                                <div class="search-section__header">
                                    <div class="search-section__title">Recently browsed products</div>
                                    <div class="search-section__actions"><a href="#"
                                            class="search-section__clear">Clear</a>
</div>
                                </div>
                                <div class="search-section__content">
                                    <div class="search-grid"></div>
                                </div>
                            </section>
                        </div><span class="el-popover__reference-wrapper"></span>
                    </span>
                </div>
            </div><a href="#" class="search-toggler" data-v-4ac4b396=""><i class="pf-icon bx bx-search"
                    data-v-4ac4b396=""></i></a>
        </div>
        <div class="bottom flex inner-gap" data-v-4ac4b396="">
                    <div class="expander" data-v-4ac4b396=""></div>
                    <div class="menu" data-v-4ac4b396="">
                        <a href="/" title="Catalog" class="nuxt-link-active" data-v-4ac4b396="">Catalog</a>
                        <a href="/" title="Brands" data-v-4ac4b396="" class="">Brands
                        </a>
                    </div>
                </div>
        <CategoriesBar/>
    </div>
</template>