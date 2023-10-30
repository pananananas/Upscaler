<template>
    <transition name="fade" @after-leave="handleAfterLeave">
        <div v-if="isVisible" :style="{ top: cursorY - magnifyWindowSize/2 + 'px', left: cursorX + 20 + 'px', height: magnifyWindowSize + 'px'}" class="bg-[rgba(217,217,217,0.30)] rounded-lg border-solid border-[rgba(255,255,255,0.54)] border absolute drop-shadow-4xl pointer-events-none w-2">
            <div :style="{ height: progress + '%' }" class="bg-[rgba(255,255,255,0.5)] transition-all rounded-lg absolute bottom-0 w-full"></div>
        </div>
    </transition>
</template>

<script setup>
import { defineProps, computed, watch, ref } from 'vue';

const props = defineProps({
    cursorY: {
        type: Number,
        required: true
    },
    cursorX: {
        type: Number,
        required: true
    },
    magnifyWindowSize: {
        type: Number,
        required: true
    },
    scaleValue: {
        type: Number,
        required: true
    }
});

const progress = computed(() => {
    let val = ((props.scaleValue - 1) / (10 - 1)) * 100;
    return Math.min(Math.max(val, 0), 100);  // Ensure the value is between 0 and 100
});

const isVisible = ref(true);

let debounceTimeout;
watch(() => props.scaleValue, (newValue, oldValue) => {
    if (newValue !== oldValue) {
        clearTimeout(debounceTimeout);
        isVisible.value = true;
        debounceTimeout = setTimeout(() => {
            isVisible.value = false;
        }, 1000); // 2 seconds debounce time
    }
});

const handleAfterLeave = () => {
    isVisible.value = false;
};
</script>

<style>
/* ... (your existing styles) ... */

.fade-enter-active, .fade-leave-active {
    transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
}
</style>
