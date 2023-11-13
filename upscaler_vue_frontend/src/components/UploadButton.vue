<template>
    <label class="bg-[#D09C6B] hover:bg-[#e7b37f] transition ease-in-out duration-300 rounded-[10px] w-[140px] h-10 text-[#000000] font-larken-sans font-semibold flex items-center justify-center" shape="round" for="fileInput" >
        <span class="px-2 text-base">{{ label }}</span>
    </label>
</template>


<script setup>
import { defineProps, } from 'vue';


const props = defineProps({
    label: {
        type: String,
    },
}
);
</script>

<style>


</style>