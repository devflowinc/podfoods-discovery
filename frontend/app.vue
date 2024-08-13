<script setup lang="ts">
import { provideSearchContext } from './app/composables/useSearchContext'
import ProductCatalog from './app/components/ProductCatalog.vue'

provideSearchContext()

</script>

<template>
  <NuxtLayout>
    <NuxtPage />
    <div id="app" class="layout layout--catalog">
      <ProductCatalog />
    </div>
  </NuxtLayout>
</template>