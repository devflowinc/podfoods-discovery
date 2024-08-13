<script setup>
const props = defineProps({
  sortDropdownState: Object,
});

const sortOptions = [
  { label: 'Order by Popularity', value: 'Popularity' },
  { label: 'Order by Brand name — A > Z', value: 'BrandAZ' },
  { label: 'Order by Brand name — Z > A', value: 'BrandZA' },
  { label: 'Order by Product name — A > Z', value: 'ProductAZ' },
  { label: 'Order by Product name — Z > A', value: 'ProductZA' },
  { label: 'Order by Relevance', value: 'Relevance' },
];


</script>

<template>
    <div v-if="sortDropdownState.isSortFocused" class="el-select-dropdown el-popper" style="min-width: 205px; position: absolute; z-index: 2001;"
      :style="{ top: sortDropdownState.dropdownTop, left: sortDropdownState.dropdownLeft, transformOrigin: 'center top' }">
      <div class="el-scrollbar">
        <div class="el-select-dropdown__wrap el-scrollbar__wrap el-scrollbar__wrap--hidden-default">
          <ul class="el-scrollbar__view el-select-dropdown__list">
            <li v-for="(option, index) in sortOptions" :key="index" 
                :class="['el-select-dropdown__item', { hover: option.hover, selected: option.value === sortDropdownState.currentSort }]" 
                data-v-d7dded24="">
              <span>{{ option.label }}</span>
            </li>
          </ul>
        </div>
        <div class="el-scrollbar__bar is-horizontal">
          <div class="el-scrollbar__thumb" style="transform: translateX(0%);"></div>
        </div>
        <div class="el-scrollbar__bar is-vertical">
          <div class="el-scrollbar__thumb" style="transform: translateY(0%);"></div>
        </div>
      </div>
      <div x-arrow="" class="popper__arrow" style="left: 46px;"></div>
    </div>
</template>