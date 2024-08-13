<script setup>
import Dropdown from './Dropdown.vue';
import { createDropdownHandlers } from '../utils/dropdownHandler';
import { reactive } from 'vue';
import { useSearchContext } from '../composables/useSearchContext';


const { sortOrder, sortOptions, updateSortOrder } = useSearchContext();

const sortDropdown = reactive(createDropdownHandlers(sortOrder.value));

const handleSortUpdate = (newValue) => {
  updateSortOrder(newValue);
  sortDropdown.currentValue = newValue;
  sortDropdown.isFocused = false;
};


</script>

<template>
  <div class="sort-area tr mb-2" data-v-d7dded24="">
    <div class="el-select sort vam" data-v-d7dded24="">
        <div :class="{ 'el-input el-input--suffix': true }"
        @click="sortDropdown.toggleDropdown"
             @blur="sortDropdown.closeDropdown">

            <input 
            ref="sortDropdown.inputRef"
            type="text" 
            :value="sortDropdown.currentValue.charAt(0).toUpperCase() + sortDropdown.currentValue.slice(1)"
            class="el-input__inner"
            autocomplete="off">
            <span class="el-input__suffix">
                <span class="el-input__suffix-inner">
                    <i :class="{ 'el-select__caret el-input__icon el-icon-arrow-up is-reverse': true}"></i>
                </span>
            </span>
        </div>
    </div>
    <button
        type="button"
        class="el-button filter vam hidden-md-and-up ml-1 el-button--default el-button--small"
        data-v-d7dded24="">
      <span><i class="pf-icon icon bx bx-filter-alt" data-v-d7dded24=""></i></span>
    </button>
  </div>
  <Dropdown 
      :dropdownLeft="Number(sortDropdown.dropdownLeft)"
      :dropdownTop="Number(sortDropdown.dropdownTop)"
      :currentValue="sortDropdown.currentValue"
      :options="sortOptions"
      :isDropdownFocused="sortDropdown.isFocused"
      @toggleDropdown="sortDropdown.toggleDropdown"
      @updateValue="handleSortUpdate"
  />
</template>