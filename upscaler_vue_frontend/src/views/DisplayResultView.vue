<template>
<div class="background-container">
<div v-for="(style, index) in gradientStyles" :key="index" :style="style"/>
<div class="relative w-full h-screen flex gap-10">
    

    <div class="flex-initial mx-auto h-full w-3/4 ml-10">
        <div class="flex justify-center items-center gap-1 h-full">
            <img :src="imageUrl" :class="divImageClasses" class="object-contain mx-auto rounded-lg image-not-dragable shadow-2xl" ref="imageRef"  @click="toggleFreeze">
        </div>
    </div>





    <div :class="divClasses" class="w-1/2">
        <div class="flex-initial bg-[rgba(20,20,20,0.75)] rounded-xl  h-full justify-self-end left-0 p-5 ">
            
            <div class="relative h-full w-full z-10">

                <div class="miniature flex mb-6">
                    <img :src="originalImageUrl" class="h-12 object-certain rounded-sm image-not-dragable">

                    <span class="text-white mx-3 font-port-lligat-sans text-md title"> 
                        {{ imageTitle }} 
                        <span class="text-[#cdcdcd] font-port-lligat-sans text-xsm"> 
                            <br/>{{ originalImageWidth * 4 }}x{{ originalImageHeight * 4 }}px
                        </span>
                    </span>
                    <gradient-info label="resolution x4" class="absolute top-0 right-0"/>
                </div>

                <span class="text-white my-4 font-port-lligat-sans text-md"> 
                    Method comparison <br/>
                </span>   

                <div class="magnifying_glass grid grid-cols-2 gap-4 my-4 text-center">
                    <div v-for="type in imageTypes" :key="type" @click="updatePreview(type)" class="relative" >
                        <div class="w-full aspect-square rounded-lg z-[10] highlight" :class="{ 'selected-image': type == selectedAlgorithm }">
                            <div class="miniature-view">
                                <img :src="imageUrls[type]" 
                                class="w-full h-full object-contain miniature-image image-not-dragable" 
                                :style="{ transform: `translate(${-percentX * 100}%, ${-percentY * 100}%) scale(${scaleValue})`}">
                            </div>    
                        </div>
                        <span class="text-white  font-port-lligat-sans text-sm"> 
                            {{ getAlgorithmName(type) }}
                        </span>
                    </div>
                </div>


                <span class="text-white mt-7 my-4 font-port-lligat-sans text-sm absolute bottom-8 left-0"> 
                    Choose a method and download your image <br/>
                </span>    

                <div class=" bg-[#242424] rounded-[100px] w-[100px] h-[22px] absolute bottom-2 left-0">
                    <select v-model="selectedAlgorithm" id="upscaleAlgorithm" class="appearance-none bg-transparent grid grid-cols-2 items-center rounded-[100px] w-full h-full text-white font-port-lligat-sans text-smm pr-5 pl-3 focus:bg-[#3d3d3d] outline-none">
                        <optgroup label="AI algorithms">
                            <option value="dwsr"> DWSR </option> 
                            <option value="esrgan"> ESRGAN </option>
                        </optgroup>
                        <optgroup label="Traditional algorithms">
                            <option value="bilinear"> Bilinear </option> 
                        </optgroup>
                        <optgroup label="Original image">
                            <option value="original"> Original </option>
                        </optgroup>
                    </select>

                    <svg class="absolute top-1/2 transform -translate-y-1/2 right-2" width="8" height="11" viewBox="0 0 8 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M3.17574 0.754882C3.41005 0.560873 3.78995 0.560873 4.02426 0.754883L7.02426 3.23885C7.25858 3.43286 7.25858 3.74741 7.02426 3.94142C6.78995 4.13543 6.41005 4.13543 6.17574 3.94142L3.6 1.80874L1.02426 3.94142C0.789949 4.13543 0.41005 4.13543 0.175736 3.94142C-0.0585786 3.74741 -0.0585786 3.43286 0.175736 3.23885L3.17574 0.754882ZM0.175736 7.2132C0.41005 7.01919 0.789949 7.01919 1.02426 7.2132L3.6 9.34588L6.17574 7.2132C6.41005 7.01919 6.78995 7.01919 7.02426 7.2132C7.25858 7.40721 7.25858 7.72176 7.02426 7.91577L4.02426 10.3997C3.78995 10.5937 3.41005 10.5937 3.17574 10.3997L0.175736 7.91577C-0.0585786 7.72176 -0.0585786 7.40721 0.175736 7.2132Z" fill="white" />
                    </svg>
                </div>
                <!-- download button -->
                <gradient-button label="Download" shape="round" class="absolute bottom-0 right-0" @click="downloadImage"/>
            </div>
        </div>
    </div>
</div>

<div class="magnify-cursor">
    <div :style="{ top: cursorY + 'px', left: cursorX + 'px', transform: 'translate(-100%, -100%)', width: magnifyWindowSize + 'px', height: magnifyWindowSize + 'px' }" class="bg-[rgba(217,217,217,0.30)] rounded-lg border-solid border-[rgba(255,255,255,0.54)] border absolute drop-shadow-4xl pointer-events-none mix-blend-difference"/>
    <magnify-round-icon :style="{ top: cursorY + 'px', left: cursorX + 'px', transform: 'translate(-50%, -50%)' }" :locked="isFrozen" class="absolute drop-shadow-4xl pointer-events-none"/>
    <scale-progress-bar :cursorX="cursorX" :cursorY="cursorY" :magnifyWindowSize="magnifyWindowSize" :scaleValue="scaleValue" />
    
</div>
</div>
</template>
  
  
<script lang="ts">
import { defineComponent, onMounted, onBeforeUnmount, ref, Ref, nextTick, computed, watch } from 'vue';
import { useRouter } from 'vue-router';

import ScaleProgressBar from '@/components/ScaleProgressBar.vue';
import MagnifyRoundIcon from '@/components/MagnifyRoundIcon.vue';
import GradientButton from '@/components/GradientButton.vue';
import GradientInfo from '@/components/GradientInfo.vue';


export default defineComponent({
    setup() {
        type ImageType = 'dwsr' | 'original' | 'esrgan' | 'bilinear';

        const router = useRouter();
        const imageId = router.currentRoute.value.params.image_id;
        const imageTypes: (ImageType)[] = ["dwsr", "esrgan", "bilinear", "original"];
        const imageUrls = ref({ original: '', dwsr: '', esrgan: '', bilinear: '' });
        const imageUrl = ref('');
        const imageTitle: Ref<string> = ref('');
        const imageRef: Ref<HTMLImageElement | null> = ref(null);
        const selectedAlgorithm: Ref<ImageType> = ref('dwsr'); // Default value
        
        const gradientStyles = ref<Array<{ [key: string]: string }>>([]);
        const originalImageUrl = ref('');
        const originalImageWidth = ref(0);
        const originalImageHeight = ref(0);

        const cursorX = ref(-30);
        const cursorY = ref(-30);
        const percentX = ref(0);
        const percentY = ref(0);

        const isFrozen = ref(false);
        const isVertical = ref(true);
        const scaleValue = ref(2);
        const magnifyWindowSize = ref(80);

        let aspectRatio = 0
        let effectiveX: number, effectiveY: number;
        let rect: DOMRect;


        onMounted(() => {
            document.addEventListener('mousemove', updateMousePosition);
            document.addEventListener('keydown', handleKeyDown);
            window.addEventListener('wheel', handleScroll, { passive: false });

            fetchAllImages();
        });

        onBeforeUnmount(() => {
            document.removeEventListener('mousemove', updateMousePosition);
            document.removeEventListener('keydown', handleKeyDown);
            window.removeEventListener('wheel', handleScroll);
        });
        
        const calculateMousePos = (e: any) => {
            if (aspectRatio === 0){
                const image = imageRef.value;
                if (image) {
                    rect = image.getBoundingClientRect();
                    aspectRatio = rect.width / rect.height;
                    scaleValue.value += 0.01; 
                } else 
                    return;
            }

            if (!isFrozen.value) {
                // Clamp the cursor's coordinates within the image's bounds
                effectiveX = Math.min(Math.max(e.clientX, rect.left + magnifyWindowSize.value), rect.right);
                effectiveY = Math.min(Math.max(e.clientY, rect.top + magnifyWindowSize.value), rect.bottom);
                cursorX.value = effectiveX;
                cursorY.value = effectiveY;
            } else {
                effectiveX = cursorX.value;
                effectiveY = cursorY.value;
            }
            // Calculate the relative position of the cursor within the image
            const relativeX = (effectiveX - magnifyWindowSize.value / 2 - rect.left) / rect.width;
            const relativeY = (effectiveY - magnifyWindowSize.value / 2 - rect.top) / rect.height;

            if (aspectRatio < 1) {
                percentX.value = (relativeX * scaleValue.value * aspectRatio) - 0.5 * scaleValue.value * aspectRatio;
                percentY.value = (relativeY * scaleValue.value) - 0.5 * scaleValue.value;
            } else {
                percentX.value = (relativeX * scaleValue.value) - 0.5 * scaleValue.value;
                percentY.value = (relativeY * scaleValue.value / aspectRatio) - 0.5 * scaleValue.value / aspectRatio;
            }
            // console.log("percentX", percentX.value, "percentY", percentY.value);
        };

        const updateMousePosition = (e: MouseEvent) => {
            if (!isFrozen.value) {
                calculateMousePos(e);
            }
        };

        const fetchImage = async (imageType: ImageType) => {
            try {
                const response = await fetch(`http://localhost:8000/get-image/${imageId}/${imageType}/`);
                if (response.ok) {
                    const data = await response.json();
                    imageUrls.value[imageType as keyof typeof imageUrls.value] = `http://localhost:8000${data.image_url}`;
                    if (imageType === "original") {
                        originalImageUrl.value = `http://localhost:8000${data.image_url}`;
                        imageTitle.value = data.image_url.replace("/images/", "");
                    }
                    if (imageType === "dwsr")
                        imageUrl.value = `http://localhost:8000${data.image_url}`;
                    // select image
                    selectedAlgorithm.value = imageType;
                    imageUrl.value = `http://localhost:8000${data.image_url}`;

                } else {
                    console.error('Failed to fetch image info:', response.statusText);
                    return Promise.reject();
                }
            } catch (error) {
                console.error('Failed to fetch the image:', error);
            }
        };

        const fetchImageInfo = async () => {
            try {
                const response = await fetch(`http://localhost:8000/get-image-info/${imageId}/`);
                if (response.ok) {
                    const data = await response.json();
                    if (data.colors === null)   setTimeout(() => fetchImageInfo(), 500);

                    gradientStyles.value = generateGradientStyles(data.colors);
                    
                    originalImageWidth.value = data.width;
                    originalImageHeight.value = data.height;
                    isVertical.value = data.width > data.height ? false : true;
                } else {
                    console.error('Failed to fetch image info:', response.statusText);
                }
            } catch (error) {
                console.error('Error while fetching image info:', error);
            }
        };

        const retryFetchImage = async (imageType: ImageType, retryCount = Number.MAX_SAFE_INTEGER) => {
            console.log(`Fetching ${imageType} image...`);
            try {
                await fetchImage(imageType);
                console.log("Fetched", imageType, "image after", Number.MAX_SAFE_INTEGER - retryCount + 1, "attempts.")
                // if done first time make the magnify-cursor visible
                if (retryCount === Number.MAX_SAFE_INTEGER) {
                    await nextTick();
                    const magnifyCursor = document.querySelector('.magnify-cursor');
                    if (magnifyCursor) 
                        magnifyCursor.classList.remove('magnify-cursor');
                }
            } catch (error) {
                if (retryCount > 0) {
                    setTimeout(() => retryFetchImage(imageType, retryCount - 1), 1000);
                } else {
                    console.error(`Failed to fetch ${imageType} image after multiple attempts.`);
                }
            }
        };

        const fetchAllImages = async () => {
            fetchImageInfo();
            const imageQueue: (ImageType)[] = ["original", "bilinear", "dwsr", "esrgan" ];
            for (const imageType of imageQueue) {
                await retryFetchImage(imageType);
            }
            
        };

        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === '=' || e.key === '+') 
                scaleValue.value = Math.min(10, scaleValue.value + 0.5); 
            else if (e.key === '-' || e.key === '_') 
                scaleValue.value = Math.max(1.5, scaleValue.value - 0.5); 
            else if (e.key === ' ')
                isFrozen.value = !isFrozen.value;
            
            // magnifyWindowSize.value = 80 / scaleValue.value;
            calculateMousePos(e);
        };

        const handleScroll = (e: WheelEvent) => {
            e.preventDefault(); 
            
            const sensitivity = 0.04; // Zooming sensitivity
            let deltaScale = e.deltaY * sensitivity;
            scaleValue.value += deltaScale;
            scaleValue.value = Math.max(1, scaleValue.value); 
            scaleValue.value = Math.min(10, scaleValue.value);

            // console.log("scaleValue", scaleValue.value);
            // magnifyWindowSize.value = 80 / scaleValue.value;

            calculateMousePos(e);
        };

        const generateGradientStyles = (colors: any[]) => {
            const angles = ['45deg', '135deg', '-45deg', '90deg', '0deg'];
            return colors.map((color: any, index: number) => ({
                backgroundImage: `linear-gradient(${angles[index]}, ${color} 0%, transparent 100%)`,
                position: 'absolute',
                top: '0',
                right: '0',
                bottom: '0',
                left: '0',
            }));
        };
        
        return {
            cursorX,
            cursorY,
            percentX,
            percentY,
            isFrozen,
            imageRef,
            imageUrl,
            imageUrls,
            imageTitle,
            imageTypes,
            isVertical,
            scaleValue,
            calculateMousePos,
            magnifyWindowSize,
            selectedAlgorithm,
            originalImageWidth,
            originalImageHeight,
            originalImageUrl,
            gradientStyles,
        };
    },
    data() {
        return {
        };
    },
    methods: {
        async updatePreview(type: 'dwsr' | 'esrgan' | 'bilinear' | 'original') {
            this.imageUrl = this.imageUrls[type];
            this.selectedAlgorithm = type;
        },
        getAlgorithmName(type:any) {
            switch(type) {
                case 'dwsr': return 'DWSR';
                case 'esrgan': return 'ESRGAN';
                case 'bilinear': return 'Bilinear';
                case 'original': return 'Original';
            }
        },
        async downloadImage() {
            try {
                // Fetch the image as a Blob
                const response = await fetch(this.imageUrls[this.selectedAlgorithm]);
                if (!response.ok) {
                    throw new Error('Failed to fetch the image.');
                }
                const blob = await response.blob();

                // Create an Object URL for the blob
                const url = window.URL.createObjectURL(blob);

                const link = document.createElement('a');
                link.href = url;
                link.download = this.imageTitle + '_' + this.getAlgorithmName(this.selectedAlgorithm) + '.png';

                document.body.appendChild(link);
                link.click();

                // Clean up: revoke the Object URL and remove the link from the document
                window.URL.revokeObjectURL(url);
                document.body.removeChild(link);
            } catch (error) {
                console.error('Error downloading the image:', error);
            }
        },

        toggleFreeze(e: MouseEvent) {
            this.isFrozen = !this.isFrozen;
            if (!this.isFrozen) {
                this.calculateMousePos(e);
            }
        },

    },
    components: { GradientButton, GradientInfo, MagnifyRoundIcon, ScaleProgressBar },
    computed: {
        divClasses() : string[] {
            return [
                'my-5',
                'mr-5',
                'z-10',
                this.isVertical ? 'w-1/4' : 'w-1/4',
            ];
        },
        divImageClasses() : string[] {
            return [
                this.isVertical ? 'h-4/5' : 'h-3/5',
            ];
        },

    },
});
</script>

<style>

.magnifying_glass div:hover img {
    transform: scale(1);
    transition: transform 0.3s;
}
.magnifying_glass > div {
    /* Existing styles... */
    /* transition: transform 0.3s ease; */
    transition: all 0.5s ease 0s;
    transition: transform 0.3s ease-out;
}

:root {
    --orange2: #f89494;
    --purple2: #aa8ded;
}

.highlight:before {
    transform: scale(0.9);
    transition: transform 1.3s ease;
    aspect-ratio: 1 / 1;
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
    inset: -2px;
    z-index: -1;
    border-radius: 10px;
    transition: all 0.3s ease 0s;
}

.highlight:hover:before {
    transform: scale(1.02);
}

.selected-image {
    transform: scale(0.94);
    transition: all 0.5s ease 0s;
}

.selected-image:before {
    transform: scale(1.02);
    transition: transform 1.3s ease;
    aspect-ratio: 1 / 1;
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
    inset: -4px;
    z-index: -1;
    border-radius: 10px;
    transition: all 0.3s ease 0s;
}

.selected-image:hover:before {
    transform: scale(1.05);
}

.miniature-view {
    overflow: hidden;
    width: 100%;
    height: 100%;
    position: relative;
    border-radius: 8px;
}

.miniature-image {
    position: absolute;
    transition: transform 0.1s ease-out;
    scale: 10;
    overflow: hidden;
}

.image-not-dragable {
    user-drag: none;
    -webkit-user-drag: none;
    user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
}

.title {
  display: block;
  width: 110px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.magnify-cursor {
    visibility: hidden;
}

.background-container {
    position: relative;
    overflow: hidden;
}

</style>