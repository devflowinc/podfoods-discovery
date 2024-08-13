<script setup lang="ts">
import Results from "./Results.vue"
import ProductQualities from "./ProductQualities.vue"
import { useSearchContext } from '../composables/useSearchContext';
import Dropdown from './Dropdown.vue';
import { createDropdownHandlers } from '../utils/dropdownHandler';
import { ref, reactive } from 'vue';
import { locationOptions } from '../utils/locationOptions';


const { searchType, searchTypeOptions, updateSearchType, tagFilters, updateTagFilters } = useSearchContext();

// Usage for search type dropdown
const searchTypeDropdown = reactive(createDropdownHandlers(searchType.value));

// Usage for location dropdown
const locationDropdown = reactive(createDropdownHandlers(''));

const handleSearchTypeUpdate = (newValue: string) => {
  updateSearchType(newValue);
  searchTypeDropdown.currentValue = newValue;
  searchTypeDropdown.isFocused = false;
};

const handleLocationUpdate = (newValue: string) => {
  locationDropdown.currentValue = newValue;
  locationDropdown.isFocused = false;
  // Add any additional logic for location update
};

// Add this new reactive object for tags
const tags = reactive({
  holiday: false,
  staffPicks: false
});
</script>

<template>
    <div class="catalog__content" data-v-25f971ce="">
        <div data-fetch-key="data-v-d7dded24:0" class="page catalog" data-v-d7dded24="" data-v-25f971ce="">
            <div class="inner-gap" data-v-d7dded24="">
                <div class="layout flex" data-v-d7dded24="">
                    <div class="aside" data-v-d7dded24="">
                        <div class="products-side-bar" data-v-18b5105c="" data-v-d7dded24="">
                            <section class="express" data-v-18b5105c=""></section>
                            <section class="Search Type" data-v-18b5105c="" style="padding: 10px; border: 1px solid rgb(217 70 239); border-radius: 8px; background: rgb(253, 244, 255);">
                                <div class="title" data-v-18b5105c="">
                                    <span class="help-tag has-tooltip" data-v-7dba5623="" data-v-18b5105c="" data-original-title="null">Search Type<i class="bx bxs-help-circle" data-v-7dba5623=""></i></span>
                                </div>
                                <div size="small" clearable=""
                                     class="el-select entity-select el-select--small address-state-select" 
                                     data-v-18b5105c="">
                                    <div class="el-input el-input--small el-input--suffix"
                                         @click="searchTypeDropdown.toggleDropdown"
                                         @blur="searchTypeDropdown.closeDropdown">
                                        <input
                                               ref="searchTypeDropdown.inputRef"
                                               type="text" 
                                               :value="searchTypeDropdown.currentValue.charAt(0).toUpperCase() + searchTypeDropdown.currentValue.slice(1)"
                                               class="el-input__inner"
                                               autocomplete="off">
                                        <span class="el-input__suffix">
                                            <span class="el-input__suffix-inner">
                                                <i class="el-select__caret el-input__icon el-icon-arrow-up"></i>
                                            </span>
                                        </span>
                                    </div>
                                </div>
                                <Dropdown 
                                    :dropdownLeft="Number(searchTypeDropdown.dropdownLeft)"
                                    :dropdownTop="Number(searchTypeDropdown.dropdownTop)"
                                    :currentValue="searchTypeDropdown.currentValue"
                                    :options="searchTypeOptions"
                                    :isDropdownFocused="searchTypeDropdown.isFocused"
                                    @toggleDropdown="searchTypeDropdown.toggleDropdown"
                                    @updateValue="handleSearchTypeUpdate"
                                />
                            </section>
                            <section class="brand-locations" data-v-18b5105c="">
                                <div class="title" data-v-18b5105c="">
                                    <span class="help-tag has-tooltip" data-v-7dba5623="" data-v-18b5105c="" data-original-title="null">State (Province/Territory)<i class="bx bxs-help-circle" data-v-7dba5623=""></i></span>
                                </div>
                                <div size="small" clearable="" placeholder="Select brand location" class="el-select entity-select el-select--small address-state-select" data-v-18b5105c="">
                                    <div class="el-input el-input--small el-input--suffix"
                                         @click="locationDropdown.toggleDropdown"
                                         @blur="locationDropdown.closeDropdown">
                                        <input ref="locationDropdown.inputRef" type="text" 
                                               :value="locationDropdown.currentValue"
                                               placeholder="Select brand location"
                                               class="el-input__inner"
                                               autocomplete="off">
                                        <span class="el-input__suffix">
                                            <span class="el-input__suffix-inner">
                                                <i class="el-select__caret el-input__icon el-icon-arrow-up"></i>
                                            </span>
                                        </span>
                                    </div>
                                </div>
                                <Dropdown 
                                    :dropdownLeft="Number(locationDropdown.dropdownLeft)"
                                    :dropdownTop="Number(locationDropdown.dropdownTop)"
                                    :currentValue="locationDropdown.currentValue"
                                    :options="locationOptions"
                                    :isDropdownFocused="locationDropdown.isFocused"
                                    @toggleDropdown="locationDropdown.toggleDropdown"
                                    @updateValue="handleLocationUpdate"
                                />
                            </section>
                            <section class="product-tags" data-v-18b5105c="">
                                <div class="title" data-v-18b5105c="">Tag</div>
                                <div role="group" aria-label="checkbox-group" class="el-checkbox-group list" 
                                     data-v-18b5105c="">
                                  <label title="Holiday" class="el-checkbox" data-v-18b5105c="">
                                    <span class="el-checkbox__input"
                                    :class="{ 'is-checked': tags.holiday }">
                                        
                                      <span class="el-checkbox__inner"></span>
                                      <input type="checkbox" v-model="tags.holiday" value="69" 
                                             class="el-checkbox__original"
                                             
                                             @change="updateTagFilters(
                                               tagFilters.some(tag => tag.value === '69')
                                                 ? tagFilters.filter(tag => tag.value !== '69')
                                                 : [...tagFilters, { label: 'Holiday', value: '69' }]
                                             )">
                                    </span>
                                    <span class="el-checkbox__label">Holiday</span>
                                  </label>
                                  <label title="Staff Picks" class="el-checkbox" data-v-18b5105c="">
                                    <span class="el-checkbox__input"
                                    :class="{ 'is-checked': tags.staffPicks }">
                                        
                                      <span class="el-checkbox__inner"></span>
                                      <input type="checkbox" v-model="tags.staffPicks" value="2" 
                                             class="el-checkbox__original"
                                             
                                             @change="updateTagFilters(
                                               tagFilters.some(tag => tag.value === '2')
                                                 ? tagFilters.filter(tag => tag.value !== '2')
                                                 : [...tagFilters, { label: 'Staff Picks', value: '2' }]
                                             )">
                                    </span>
                                    <span class="el-checkbox__label">Staff Picks</span>
                                  </label>
                                </div>
                            </section>
                            <ProductQualities />
                        </div>
                    </div>
                    <Results />
                </div>
            </div>
        </div>
    </div>
</template>