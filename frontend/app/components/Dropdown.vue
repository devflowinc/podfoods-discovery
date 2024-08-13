<script setup>
import { defineProps, computed } from 'vue';

const props = defineProps({
  dropdownLeft: Number,
  dropdownTop: Number,
  currentValue: String,
  options: Array,
  isDropdownFocused: Boolean
});

const emit = defineEmits(['updateValue', 'close']);

const handleOptionClick = (optionValue) => {
  emit('updateValue', optionValue);
  emit('close');
};

const dropdownStyle = computed(() => ({
  top: props.dropdownTop && !isNaN(props.dropdownTop) ? `${props.dropdownTop}px` : 'auto',
  left: props.dropdownLeft && !isNaN(props.dropdownLeft) ? `${props.dropdownLeft}px` : 'auto',
  transformOrigin: 'center top'
}));
</script>

<template>
    <div v-if="isDropdownFocused" class="el-select-dropdown el-popper"
      style="min-width: 205px; position: absolute; z-index: 2001;"
      :style="dropdownStyle"
      @blur="emit('close')">
      <div class="el-scrollbar">
        <div class="el-select-dropdown__wrap el-scrollbar__wrap 
          el-scrollbar__wrap--hidden-default">
          <ul class="el-scrollbar__view el-select-dropdown__list">
            <li v-for="(option, index) in options" :key="index" 
                :class="[
                  'el-select-dropdown__item', 
                  { 
                    hover: option.hover, 
                    selected: option.value === currentValue 
                  }
                ]"
                @click="handleOptionClick(option.value)">
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