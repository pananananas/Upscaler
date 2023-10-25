<template>
    <label class="gradientinfo" shape="round"  >
        <span class="text-xsm px-1">
            {{ label }}
        </span>
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
    padding: 0.3rem 0.8rem; 
    line-height: 0.7rem;    
    border-radius: 90px;
    display: inline-flex;
    font-size: 0.5rem;
    position: relative;
    background-color: rgba(24, 24, 27, 0.9);
    color: #f4f4f5;
    font-family: Port Lligat Sans;
    transition: background-color 0.3s ease-in-out;
    justify-content: center;
    text-align: center;
}
:root {
    --orange2: #f89494;
    --purple2: #aa8ded;
}

.gradientinfo:before {
    content: "";
    position: absolute;
    animation: background-button 4s linear infinite;
    background: linear-gradient(
        to right, 
        var(--orange2),
        var(--purple2),
        var(--orange2)
    );
    background-size: 200%;
    inset: -1px;
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