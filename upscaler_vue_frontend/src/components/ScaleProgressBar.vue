<template>
    <div :style="{ top: cursorY - magnifyWindowSize/2 + 'px', left: cursorX + 20 + 'px', height: magnifyWindowSize + 'px'}" class="bg-[rgba(217,217,217,0.30)] rounded-lg border-solid border-[rgba(255,255,255,0.54)] border absolute drop-shadow-4xl pointer-events-none w-2">
        <div :style="{ height: progress + '%' }" class="bg-[rgba(255,255,255,0.5)] transition-all rounded-lg absolute bottom-0 w-full"></div>
    </div>
</template>

<script setup>
import { defineProps, computed } from 'vue';

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
    let val = ((props.scaleValue - 1.5) / (10 - 1.5)) * 100;
    return Math.min(Math.max(val, 0), 100);  // Ensure the value is between 0 and 100
});
</script>

<style>
/* ... (your existing styles) ... */
</style>
