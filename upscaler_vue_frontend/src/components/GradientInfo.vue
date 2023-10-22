<template>
    <label class="gradientinfo" shape="round"  >
        <span class="text-2xsm px-1">{{ label }}</span>
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
.gradientinfo {
    /* Adjusting padding and line-height for the label */
    padding: 0.3rem 0.8rem;  /* Reduced padding */
    line-height: 0.6rem;     /* Adjusted line-height */
    border-radius: 90px;
    display: inline-flex;
    font-size: 0.5rem;       /* Reduced font size */
    position: relative;
    background-color: rgba(24, 24, 27, 0.9);
    color: #f4f4f5;
    font-family: Port Lligat Sans;
    transition: background-color 0.3s ease-in-out;
    justify-content: center;
    text-align: center;
}

.gradientinfo:before {
    content: "";
    position: absolute;
    background: linear-gradient(
        to right,
        rgba(255, 159, 159),
        rgba(139, 92, 246)
    );
    inset: -0.5px;
    z-index: 11;
    border-radius: 90px;
    transition: all 0.3s ease 0s;
}

.gradientinfo:after {
    content: "";
    position: absolute;
    background-color: rgba(24, 24, 27, 0.95);
    inset: 1px;
    z-index: 12;
    border-radius: 90px;
    transition: all 0.3s ease 0s;
}

.gradientinfo:hover:after {
    background-color: rgba(12, 12, 13, 0.95);
}

.gradientinfo > span {
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    z-index: 13;
}

</style>