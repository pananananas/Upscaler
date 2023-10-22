<template>
    <body class="bg-backgroundcolor">
        <!-- <svg
        class="absolute overflow-visible"
        style=""
        width="795"
        height="593"
        viewBox="0 0 795 593"
        fill="none"
        xmlns="http://www.w3.org/2000/svg">
        <path d="M424 428C311.5 529 62.5 438.5 0 577V-3.8147e-06L791 0C791 0 691.5 4.50001 620 117C548.5 229.5 536.5 327 424 428Z" fill="#054049"/>
      </svg>  -->

        <div class="container">

            <div class="my-5 justify-self-start">
                
                <div class="text-6xl font-port-lligat-slab leading-[50px] text-white w-full">
                    Upscale your
                    <br />
                    <span class="magic_text">
                    images
                    </span>
                    
                </div>
                <div class="text-white my-5" style="font: 400 18px/20px 'Port Lligat Sans', sans-serif">
                    Enhance resolution of your images 
                    <br/>
                    using fast and reliable AI algorithms
                </div>
            </div>

            <gradient-button label="Upload Image" class="m-5"/>
        </div>




  </body>
<div>
    <input type="file" ref="fileInput" @change="uploadImage">
</div>
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
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
}

.container {
    display: grid;
    grid-template-rows: 1fr;
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