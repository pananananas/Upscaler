<template>
    <body>
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
                <div class="text-7xl font-port-lligat-slab leading-[60px] text-white w-full">
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

            <div class="card">
                <input type="file" ref="fileInput" class="hidden" id="fileInput" @change="uploadImage" accept="image/*">
                <label for="fileInput" class="btn" shape="round">
                    <span> Upload Image </span>
                </label>
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

.btn {
    line-height: 1.3rem;
    border-radius: 90px;
    display: inline-flex;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    position: relative;
    background-color: #18181b;
    color: #f4f4f5;
    font-family: Port Lligat Sans;
    transition: background-color 0.2s ease-in-out;
    justify-content: center;
    text-align: center;
    cursor: pointer;
}

.btn:before {
    content: "";
    position: absolute;
    background: linear-gradient(
        to right,
        #FF9F9F,
        #8B5CF6
    );
    inset: -2px;
    z-index: 1;
    border-radius: 90px;
    transition: all 0.2s ease 0s;
}
.btn:after {
    content: "";
    position: absolute;
    background-color: #18181b;
    inset: 1px;
    z-index: 2;
    border-radius: 90px;
    /* transition: all 0.2s ease 0s; */
}

.btn:hover:before {
    box-shadow: rgba(255, 159, 159, 0.7)  0px 0px 10px 0px,
                rgba(139, 92, 246, 0.7)   0px 0px 20px 0px;
}

.btn:hover:after {
    background-color: #0c0c0d;
}

.btn > span {
    text-align: left;
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    word-break: break-all;
    z-index: 3;
}
</style>