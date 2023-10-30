<template>
    <label class="magnifyroundicon" >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-4 h-4 magnifyicon">
            
            <path v-if="!locked" stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
            
            <path v-else stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
        </svg>
    </label>
</template>


<script setup>
import { defineProps, } from 'vue';
const props = defineProps({
    label: {
        type: String,
    },
    locked: {
        type: Boolean,
        default: false
    },
}
);
</script>


<style>

.magnifyicon {
    z-index: 102;

}
.magnifyroundicon {
    padding: 0.35rem ; 

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

.magnifyroundicon:before {
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
    z-index: 100;
    border-radius: 90px;
    transition: all 0.3s ease 0s;
}

.magnifyroundicon:after {
    content: "";
    position: absolute;
    background-color: rgba(24, 24, 27, 0.95);
    inset: 1px;
    z-index: 101;
    border-radius: 90px;
    transition: all 0.3s ease 0s;
}

.magnifyroundicon > span {
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    z-index: 13;
}

</style>