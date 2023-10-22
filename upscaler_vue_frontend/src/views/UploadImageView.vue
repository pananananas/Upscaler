<template>
    <body>
        <svg class="absolute top-0 left-0 z-0" width="791" height="577" viewBox="0 0 791 577" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M467 404.5C354.5 505.5 62.5 438.5 0 577V-3.8147e-06L791 -1.20013e-07C791 -1.20013e-07 691.5 4.50001 620 117C548.5 229.5 579.5 303.5 467 404.5Z" fill="#054049"/>
        </svg>

        <div class="container relative mx-40 z-10 py-40">

            <div class="justify-self-start">
                <div class="text-7xl font-port-lligat-slab leading-[60px] text-white w-full">
                    Upscale your
                    <br />
                    <span class="magic_text">
                    images
                    </span>
                    
                </div>
                <div class="text-white mt-7 mb-4 font-port-lligat-sans text-xl leading-6" >
                    Enhance resolution of your images using 
                    <br/>
                    fast and reliable AI powered algorithms.
                </div>
                <div class="bg-[rgba(22,22,22,0.80)] hover:bg-[rgba(22,22,22,0.9)] transition ease-in-out duration-300 rounded-[10px] w-[200px] h-9 text-white font-port-lligat-sans cursor-pointer flex items-center justify-center">
                    <span class="  "> How does it work? </span>
                </div>
            </div>

            <div class="bg-[rgba(5,64,73,0.90)] aspect-[4/3] h-[280px] rounded-[10px] border-dashed border-[transparent] border flex flex-col gap-2.5  relative overflow-hidden items-center justify-center">
                <div>
                    <input type="file" ref="fileInput" class="hidden" id="fileInput" @change="uploadImage" accept="image/*">
                    <gradient-button label="Upload image" shape="round"/>
                </div>
                <span class="text-[#dddddd] text-center relative font-port-lligat-sans text-xsm leading-6">
                    Drop your images here
                </span>
                <div class="bg-[rgba(30,30,30,0.80)] rounded-lg shrink-0 w-[160px] h-[50px] relative">

                </div>
            </div>
        </div>
    </body>
</template>
  
  
<script lang="ts">
import GradientButton from '@/components/GradientButton.vue';


interface Data {
    selectedFile: File | null;
}

export default {
    data(): Data {
        return {
            selectedFile: null
        };
    },
    methods: {
        async uploadImage(event: Event) {
            const input = event.target as HTMLInputElement;
            const files = input.files;
            if (files) {
                (this as any).selectedFile = files[0];
            }
            if (!(this as any).selectedFile)
                return;
            const formData = new FormData();
            formData.append('image', (this as any).selectedFile);
            try {
                const response = await fetch('http://localhost:8000/upload/', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                console.log(data);
            }
            catch (error) {
                console.error("Błąd podczas wysyłania obrazu:", error);
            }
        }
    },
    components: { GradientButton }
};
</script>


<style>
body {
    background-color: #1A1A1A;
}

.card {
    display: inline-flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    flex-shrink: 0;
    border-radius: 10px;
    background: rgba(5, 64, 73, 0.90);
}

.container {
    display: grid;
    grid-template-rows: 280px;
    grid-template-columns: 1fr 1fr;
    grid-gap: 1rem 1rem;
    justify-items: center;
    align-items: center;
}

:root {
    --orange: #FF9F9F;
    --purple: #8B5CF6;
}

@keyframes background-pan {
    from {
        background-position: 0% center;
    }
    to {
        background-position: -200% center;
    }
}

.magic_text {
    animation: background-pan 3s linear infinite;
    background: linear-gradient(
        to right, 
        var(--orange),
        var(--purple),
        var(--orange)
    );
    background-size: 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    white-space: nowrap;
}
</style>