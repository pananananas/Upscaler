<template>
    <label class="btn font-larken-sans" shape="round" >
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
.btn {
    line-height: 1.3rem;
    border-radius: 90px;
    display: inline-flex;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    position: relative;
    background-color: rgba(24, 24, 27, 0.9);
    color: #f4f4f5;

    transition: background-color 0.3s ease-in-out;
    justify-content: center;
    text-align: center;
    cursor: pointer;
    z-index: 0;
}

:root {
    --orange: #FF9F9F;
    --purple: #8B5CF6;
}

@keyframes background-button {
    from {
        background-position: 0% center;
    }
    to {
        background-position: -200% center;
    }
}

.btn:before {
    content: "";
    position: absolute;
    animation: background-button 3s linear infinite;
    background: linear-gradient(
        to right, 
        var(--orange),
        var(--purple),
        var(--orange)
    );
    background-size: 200%;
    inset: -2px;
    z-index: 1;
    border-radius: 90px;
    transition: all 0.3s ease 0s;
}

.btn:after {
    content: "";
    position: absolute;
    background-color: rgba(24, 24, 27, 0.9);
    inset: 1px;
    z-index: 2;
    border-radius: 90px;
    transition: all 0.3s ease 0s;
}

.btn:hover:before {
    box-shadow: rgba(255, 159, 159, 0.7)  0px 0px 10px 0px,
                rgba(139, 92, 246, 0.7)   0px 0px 20px 0px;
}

.btn:hover:after {
    background-color: rgba(12, 12, 13, 0.9);
}

.btn > span {
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    z-index: 3;
}

</style>