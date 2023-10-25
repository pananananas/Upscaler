<template>

    <body>
        <svg class="absolute top-0 left-0 z-0" xmlns="http://www.w3.org/2000/svg" width="219" height="404" viewBox="0 0 219 404" fill="none">
            <path d="M99 237.5C88.5 374.5 0 404 0 404V-1.90735e-06H218.234C218.234 -1.90735e-06 109.5 100.5 99 237.5Z" fill="#054049"/>
        </svg>
        <div class="relative w-full h-screen flex">
            <svg xmlns="http://www.w3.org/2000/svg" width="404" height="819" viewBox="0 0 404 819" fill="none" class="absolute bottom-0 right-0">
                <path d="M240 403.5C220 259.561 404 0 404 0L404 819L0 819C69.1759 819 260 547.439 240 403.5Z" fill="#054049"/>
            </svg>

            <div class="flex-initial mx-auto  h-full">

                <div class="flex justify-center items-center gap-1 h-full">


                    <img v-if="isVertical" :src="require('@/assets/image.png')" class="h-4/5 object-contain mx-auto rounded-md">
                    <img v-else            :src="require('@/assets/vertical.png')" class="w-4/5 object-contain my-auto rounded-md">
                </div>
                <!-- <div
                    class="bg-[rgba(37,37,37,0.80)] rounded-full border-2 border-solid w-[39.94px] h-[39.94px] relative"
                    style="
                    border-image: linear-gradient(
                        135deg,
                        rgba(255, 159, 159, 1) 0%,
                        rgba(139, 92, 246, 1) 100%
                    );
                    border-image-slice: 1;">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                    </svg>
                </div> -->

                <!-- <div class="bg-[rgba(217,217,217,0.10)] rounded-[10px] border-solid border-[rgba(255,255,255,0.30)] border w-[119.83px] h-[119.83px] relative"> </div> -->
                
            </div>
            <div :class=divClasses>
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


export default defineComponent({
    setup() {
        onMounted(() => {            
        });
        return {
        };
    },
    data() {
        return {
            selectedFile: null,
            isVertical: true,
        };
    },
    methods: {

    },
    components: { GradientButton, GradientInfo },
    computed: {
        divClasses() : string[] {
        return [
            'm-5',
            'z-10',
            this.isVertical ? 'w-1/4' : 'w-1/2',
        ];
        },
    },
});
</script>

<style>
body {
    background-color: #1A1A1A;
}
</style>