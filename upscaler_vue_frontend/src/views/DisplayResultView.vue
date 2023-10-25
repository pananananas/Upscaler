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
                    <img :src="require('@/assets/image.png')" class=" object-certain rounded-md">
                </div>

                <!-- <div class="bg-[rgba(217,217,217,0.10)] rounded-[10px] border-solid border-[rgba(255,255,255,0.30)] border w-[119.83px] h-[119.83px] relative"> </div> -->
                
            </div>
            <div class="m-5 w-1/4 z-10">
                <div class="flex-initial bg-[rgba(20,20,20,0.7)] rounded-xl  h-full justify-self-end left-0 p-5">
                    
                    <div class="relative h-full w-full">

                        <div class="miniature flex mb-5">
                            <img :src="require('@/assets/image.png')" class="h-12 object-certain rounded-sm">

                            <span class="text-white mx-3 font-port-lligat-sans text-md"> 
                                image.png 
                                <span class="text-[#cdcdcd] font-port-lligat-sans text-xsm"> 
                                    <br/>248x360px
                                </span>
                            </span>

                            
                            <gradient-info label="resolution x4" class="absolute top-0 right-0"/>
                        </div>
                        <span class="text-white mt-7 my-4 font-port-lligat-sans text-md"> 
                            Method comparison <br/>
                        </span>   

                        <span class="text-white mt-7 my-4 font-port-lligat-sans text-smm"> 
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
import { defineComponent, onMounted, ref, nextTick } from 'vue';
import GradientButton from '@/components/GradientButton.vue';
import GradientInfo from '@/components/GradientInfo.vue';



// write export default:
export default {
    setup() {
        onMounted(() => {            
            // get fileName from image
        });

        return {

        };
    },
    data() {
        
    


        return {
            selectedFile: null
        };
    },
    methods: {

    },
    components: { GradientButton, GradientInfo }
};
</script>

<style>
body {
    background-color: #1A1A1A;
}
</style>