<template>

    <body>
        <svg class="absolute top-0 left-0 z-0" xmlns="http://www.w3.org/2000/svg" width="219" height="404" viewBox="0 0 219 404" fill="none">
            <path d="M99 237.5C88.5 374.5 0 404 0 404V-1.90735e-06H218.234C218.234 -1.90735e-06 109.5 100.5 99 237.5Z" fill="#054049"/>
        </svg>
        <div class="relative w-full h-screen flex">
            <svg xmlns="http://www.w3.org/2000/svg" width="404" height="819" viewBox="0 0 404 819" fill="none" class="absolute bottom-0 right-0">
                <path d="M240 403.5C220 259.561 404 0 404 0L404 819L0 819C69.1759 819 260 547.439 240 403.5Z" fill="#054049"/>
            </svg>

            <div class="flex-initial mx-auto p-5 grid-cols-1 gap-6 h-full justify-items-center items-center ">

                <div class="">
                    <img :src="require('@/assets/image.png')" alt="Description of Image">
                </div>
                
                
            </div>
            <div class="m-5 w-1/4 z-10">
                <div class="flex-initial bg-[rgba(24,24,24,0.7)] rounded-xl  h-full justify-self-end left-0 p-5">
                    
                    <div class="relative h-full w-full">
                        

                        <span class="text-white mt-7 my-4 font-port-lligat-sans text-sm"> 
                            Choose a method and download your image <br/>
                        </span>    

                        <gradient-button label="Download" shape="round" class="absolute bottom-0 right-0"/>
                    </div>
                </div>
            </div>
        </div>
  </body>
  </template>
  
  
<script lang="ts">
import GradientButton from '@/components/GradientButton.vue';



// write export default:
export default {
    data() {
        return {
            selectedFile: null
        };
    },
    methods: {
        
    },
    components: { GradientButton }
};
</script>

<style>
body {
    background-color: #1A1A1A;
}


</style>