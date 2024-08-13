<script setup lang="ts">
import { useSearchContext } from '../composables/useSearchContext'
import { watch } from 'vue'

const { searchTerm, isLoading, error, results } = useSearchContext()

defineProps({
    isFocused: {
        type: Boolean,
        default: false
    }
})

// Watch for changes in the query and log them
watch(searchTerm, (newValue, oldValue) => {
    if (newValue !== oldValue) {
        console.log('searchTerm updated:', newValue)
    }
}, { immediate: true })

// Watch for changes in the results and log them
watch(results, (newResults, oldResults) => {
    if (newResults !== oldResults) {
        console.log('Search results updated:', newResults)
    }
}, { deep: true })

// Function to handle input changes
const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement
    if (target.value !== searchTerm.value) {
        console.log('Input value:', target.value)
    }
}
</script>

<template>
    <div data-v-4321adf5="" class="search-box__input el-input el-input-group el-input-group--append"
    style="border-color: rgb(217, 70, 239);">
        <input v-model="searchTerm" type="search" autocomplete="off"
            placeholder="Search for products, SKUs, UPC, EAN..." class="el-input__inner"
            @input="handleInput"
            @focus="$emit('update:isFocused', true)" @blur="$emit('update:isFocused', false)">
        <div class="el-input-group__append"><span data-v-4321adf5="" class="vam"><i data-v-4321adf5=""
                    class="pf-icon bx bx-search"></i></span>
    </div>
</div>
</template>