import { ref } from 'vue';
import type { Ref } from 'vue';

export function createDropdownHandlers(initialValue: string) {
    const dropdownLeft: Ref<string> = ref('0px');
    const dropdownTop: Ref<string> = ref('0px');
    const currentValue: Ref<string> = ref(initialValue);
    const isFocused: Ref<boolean> = ref(false);
    const inputRef: Ref<HTMLInputElement | null> = ref(null);

    function toggleDropdown() {
        isFocused.value = !isFocused.value;
        if (isFocused.value && inputRef.value) {
            const rect = inputRef.value.getBoundingClientRect();
            dropdownLeft.value = `${rect.left}px`;
            dropdownTop.value = `${rect.bottom + window.scrollY}px`;
        }
    }

    function closeDropdown() {
        isFocused.value = false;
    }

    return {
        inputRef,
        dropdownLeft,
        dropdownTop,
        currentValue,
        isFocused,
        toggleDropdown,
        closeDropdown
    };
}