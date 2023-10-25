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


                    <img v-if="isVertical" :src="require('@/assets/horizontal.png')" class="h-4/5 object-contain mx-auto rounded-md">
                    <img v-else            :src="require('@/assets/vertical.png')" class="w-4/5 object-contain my-auto rounded-md">
                </div>
                <!-- <div class="bg-[rgba(217,217,217,0.10)] rounded-[10px] border-solid border-[rgba(255,255,255,0.30)] border w-[120px] h-[120px] absolute left-0 up-0"> </div> -->
                
            </div>
            <div :class=divClasses>
                <div class="flex-initial bg-[rgba(20,20,20,0.7)] rounded-xl  h-full justify-self-end left-0 p-5">
                    
                    <div class="relative h-full w-full">

                        <div class="miniature flex mb-6">
                            <img :src="require('@/assets/horizontal.png')" class="h-12 object-certain rounded-sm">

                            <span class="text-white mx-3 font-port-lligat-sans text-md"> 
                                image.png 
                                <span class="text-[#cdcdcd] font-port-lligat-sans text-xsm"> 
                                    <br/>248x360px
                                </span>
                            </span>
                            <gradient-info label="resolution x4" class="absolute top-0 right-0"/>
                        </div>

                        <span class="text-white my-4 font-port-lligat-sans text-md"> 
                            Method comparison <br/>
                        </span>   

                        <div class="magnifying_glass grid grid-cols-2 gap-4 my-4 text-center">
                            <div>
                                <div class="w-full aspect-square bg-white rounded-lg">
                                
                                </div>
                                <span class="text-white mt-7 font-port-lligat-sans text-sm"> 
                                    DWSR
                                </span>
                            </div>
                            <div>
                                <div class="w-full aspect-square bg-white rounded-lg">
                                
                                </div>
                                <span class="text-white mt-7 font-port-lligat-sans text-sm"> 
                                    ESRGAN
                                </span>
                            </div>
                            <div>
                                <div class="w-full aspect-square bg-white rounded-lg">
                                
                                </div>
                                <span class="text-white mt-7 font-port-lligat-sans text-sm"> 
                                    Bilinear
                                </span>
                            </div>
                            <div>
                                <div class="w-full aspect-square bg-white rounded-lg">
                                
                                </div>
                                <span class="text-white mt-7 font-port-lligat-sans text-sm"> 
                                    Original
                                </span>
                            </div>
                        </div>

                        <span class="text-white mt-7 my-4 font-port-lligat-sans text-smm absolute bottom-8 left-0"> 
                            Choose a method and download your image <br/>
                        </span>    

                        <div class=" bg-[#2d2d2d] rounded-[100px] w-[100px] h-[22px] absolute bottom-2 left-0">
                            <select v-model="upscaleAlgorithm" id="upscaleAlgorithm" class="appearance-none bg-transparent grid grid-cols-2 items-center rounded-[100px] w-full h-full text-white font-port-lligat-sans text-smm pr-5 pl-3 focus:bg-[#3d3d3d] outline-none">
                                <option value="dwsr"> DWSR </option> 
                                <option value="esrgan"> ESRGAN </option>
                                <option value="bilinear"> Bilinear </option> 
                            </select>

                            <svg class="absolute top-1/2 transform -translate-y-1/2 right-2" width="8" height="11" viewBox="0 0 8 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M3.17574 0.754882C3.41005 0.560873 3.78995 0.560873 4.02426 0.754883L7.02426 3.23885C7.25858 3.43286 7.25858 3.74741 7.02426 3.94142C6.78995 4.13543 6.41005 4.13543 6.17574 3.94142L3.6 1.80874L1.02426 3.94142C0.789949 4.13543 0.41005 4.13543 0.175736 3.94142C-0.0585786 3.74741 -0.0585786 3.43286 0.175736 3.23885L3.17574 0.754882ZM0.175736 7.2132C0.41005 7.01919 0.789949 7.01919 1.02426 7.2132L3.6 9.34588L6.17574 7.2132C6.41005 7.01919 6.78995 7.01919 7.02426 7.2132C7.25858 7.40721 7.25858 7.72176 7.02426 7.91577L4.02426 10.3997C3.78995 10.5937 3.41005 10.5937 3.17574 10.3997L0.175736 7.91577C-0.0585786 7.72176 -0.0585786 7.40721 0.175736 7.2132Z" fill="white" />
                            </svg>
                        </div>
                        <gradient-button label="Download" shape="round" class="absolute bottom-0 right-0"/>
                    </div>
                </div>
            </div>
        </div>


        <magnify-round-icon class="absolute top-0 left-0"/>
  </body>
  </template>
  
  
<script lang="ts">
import { defineComponent, onMounted, ref, nextTick } from 'vue';
import GradientButton from '@/components/GradientButton.vue';
import GradientInfo from '@/components/GradientInfo.vue';
import MagnifyRoundIcon from '@/components/MagnifyRoundIcon.vue';


export default defineComponent({
    setup() {
        onMounted(() => {            
        });
        const upscaleAlgorithm = ref('dwsr'); // Default value 

        const someMethod = () => {
            console.log(upscaleAlgorithm.value);
        };
        return {
            upscaleAlgorithm,
            someMethod
        };
    },
    data() {
        return {
            selectedFile: null,
            isVertical: true,
            selectedMethod: "DWSR",
        };
    },
    methods: {

    },
    components: { GradientButton, GradientInfo, MagnifyRoundIcon },
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