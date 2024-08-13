<script setup lang="ts">
import { ref } from 'vue';
import { useSearchContext } from '../composables/useSearchContext';
import { qualityTagOptions } from '../utils/qualityTagOptions';

const { tagFilters, updateTagFilters } = useSearchContext();

const qualityTags = ref(qualityTagOptions.map(tag => ({
  ...tag,
  checked: tagFilters.value.some(filter => filter.value === tag.value)
})));

const handleTagChange = (qualityTag: { label: string; value: string; checked: boolean }) => {
  if (qualityTag.checked) {
    updateTagFilters([...tagFilters.value, { label: qualityTag.label, value: qualityTag.value }]);
  } else {
    updateTagFilters(tagFilters.value.filter(tag => tag.value !== qualityTag.value));
  }
};
</script>

<template>
  <section class="product-qualities" data-v-18b5105c="">
    <div class="title" data-v-18b5105c="">Product Quality</div>
    <div role="group" aria-label="checkbox-group" class="el-checkbox-group list" data-v-18b5105c="">
      <label v-for="qualityTag in qualityTags" :key="qualityTag.value" class="el-checkbox">
        <span class="el-checkbox__input" :class="{ 'is-checked': qualityTag.checked }">
          <span class="el-checkbox__inner"></span>
          <input 
            type="checkbox" 
            v-model="qualityTag.checked"
            :value="qualityTag.value"
            class="el-checkbox__original"
            @change="handleTagChange(qualityTag)"
          >
        </span>
        <span class="el-checkbox__label">{{ qualityTag.label }}</span>
      </label>
    </div>
  </section>
</template>