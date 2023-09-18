<template>
<div className="overflow-hidden bg-[#1a1a1a] relative flex flex-row gap-4 w-full items-end"  id="LoadPhotoRoot">

  <svg
    class="relative overflow-visible"
    style=""
    width="795"
    height="593"
    viewBox="0 0 795 593"
    fill="none"
    xmlns="http://www.w3.org/2000/svg">
    <path d="M424 428C311.5 529 62.5 438.5 0 577V-3.8147e-06L791 0C791 0 691.5 4.50001 620 117C548.5 229.5 536.5 327 424 428Z" fill="#054049"/>
  </svg>

  <div class="text-6xl font-port-lligat-slab leading-[50px] text-white w-full">
    Upscale your
    <br />
    <div class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600" id="UpscaleYourImages">
      images
    </div>
  </div>







  <div>
    <input type="file" ref="fileInput" @change="uploadImage">
  </div>
</div>

<svg>
    <filter id="grainy">
      <feTurbulence type="fractalNoise" baseFrequency="0.01" />
      <feComposite operator="in" in2="SourceGraphic" />

    </filter>

    <rect x="0.5" y="0.5" width="415" height="281" rx="9.5" fill="#054049" fill-opacity="0.9" stroke="#6D6D6D" stroke-dasharray="6 4"/>
</svg>







</template>


<script lang="ts">
export default {
  data() {
    return {
      selectedFile: null
    };
  },
  methods: {
    async uploadImage(event: { target: { files: null[]; }; }) {
      
      this.selectedFile = event.target.files[0];
      if (!this.selectedFile) return;

      const formData = new FormData();
      formData.append('image', this.selectedFile);

      try {
        const response = await fetch('http://localhost:8000/upload/', {
          method: 'POST',
          body: formData
        });

        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error("Błąd podczas wysyłania obrazu:", error);
      }
    }
  }
};
</script>

<style>
/* .container{
  filter: url(#grainy);
} */


</style>
```