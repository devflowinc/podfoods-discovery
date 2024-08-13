<script setup>
import { useSearchContext } from '../composables/useSearchContext';

const { results } = useSearchContext();
</script>

<template>
  <article
    v-for="product in results"
    :key="product.id"
      class="product-card default-card"
      data-v-aa41a82c=""
      data-v-257419ec=""
    >
      <div class="combined" data-v-aa41a82c="">
        <div class="frame" data-v-aa41a82c="">
          <a :href="product.url" class="preview" data-v-aa41a82c="">
           <div class="flex flex-row justify-between w-full" style="display: flex; justify-content: space-between; width: 100%;">
  <div style="height: 24px;">
    <span 
      v-if="product.tags && product.tags.includes('product-level-group')" 
      class="product-level-label"
      style="align-self: flex-start;"
    >
      Product Group
    </span>
  </div>

</div>
            <div class="thumbnail-rotator" data-v-56c478cc="" data-v-aa41a82c="">
              <div class="thumbnail-rotator__current" data-v-56c478cc="">
                <img :src="product.imageUrl" data-v-56c478cc="">
              </div>
            </div>
          </a>
          <div class="overlay" data-v-aa41a82c="">
            <div class="tags" data-v-aa41a82c=""></div>
          </div>
          <div class="info" data-v-aa41a82c="">
            <div class="product" data-v-aa41a82c="">
              <a :href="product.url" :title="product.name" data-v-aa41a82c="" class="">
                {{ product.name }}
              </a>
            </div>
            <div class="brand" data-v-aa41a82c="">
              <span data-v-aa41a82c="">By&nbsp;</span>
              <a :href="product.url"
                 :title="product.brand"
                 class="pf-ellipsis"
                 data-v-aa41a82c="">
                {{ product.brand }}
              </a>
            </div>
          </div>
        </div>
      </div>
    </article>  
</template>

            <style scoped>
            .product-level-label {
              font-family: 'Arial', sans-serif;
              font-weight: bold;
              font-size: 12px;
              text-align: center;
              color: #333;
              /* background-color: #f0f0f0; */
              padding: 4px 8px;
              border: 1px solid #b02386;
              border-radius: 5px;
              /* box-shadow: 0 2px 4px rgba(0,0,0,0.1); */
            }
            .combined:hover .product-level-label {
              background-color: #fff;
              color: #b02386;
            }
            </style>