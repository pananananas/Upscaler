<template>
<div class="cursor"> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> </div>
<!-- <svg class="absolute top-0 left-0 z-0" width="791" height="577" viewBox="0 0 791 577" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M467 404.5C354.5 505.5 62.5 438.5 0 577V-3.8147e-06L791 -1.20013e-07C791 -1.20013e-07 691.5 4.50001 620 117C548.5 229.5 579.5 303.5 467 404.5Z" fill="#054049"/>
</svg> -->
<body>
<div class="relative mt-24 z-10 mx-auto py-10 px-5 grid grid-cols-1 md:grid-cols-2 gap-6 justify-items-center items-center">
    <!-- TODO: Fix this grid -->
    <div class="">
        <div class="text-7xl font-abril-fatface leading-[76px] text-white w-full">
            Upscale your
            <br />
            <span class="magic_text text-6xl">
            images
            </span>
            
        </div>
        <div class="text-[rgb(232,232,232)] mt-7 mb-4 font-larken-sans font-italic text-xl leading-6" >
            Enhance resolution of your images using 
            <br/>
            fast and reliable AI powered algorithms.
        </div>
        <div class="bg-[rgba(22,22,22,0.80)] hover:bg-[rgba(22,22,22,0.9)] transition ease-in-out duration-300 rounded-[10px] w-[200px] h-9 text-white font-port-lligat-sans cursor-pointer flex items-center justify-center">
            <span class="  "> How does it work? </span>
        </div>
    </div>

    <div class="bg-[rgba(5,64,73,0.90)] aspect-[4/3] h-[280px] z-10 rounded-[10px] border-dashed border-[transparent] border flex flex-col gap-1  relative overflow-hidden items-center justify-center"
        @dragover.prevent="onDragOver" 
        @drop.prevent="onDrop">
        <div></div>
        <div></div>
        <div></div>
        <div>
            <input type="file" ref="fileInput" class="hidden" id="fileInput" @change="uploadImage" accept="image/*">
            <gradient-button label="Upload image" shape="round"/>
        </div>
        <span class="text-[#dddddd] text-center relative z-10 font-larken-sans text-xsm leading-6">
            Drop your images here
        </span>
        <div></div>
        <div class="pt-2"></div>
        
        <div class="bg-[rgba(30,30,30,0.80)] hover:bg-[rgba(30,30,30,0.9)] transition ease-in-out duration-300 rounded-lg shrink-0 w-[180px] h-[57px] z-10 relative">
            <span class="text-white text-center relative z-10 font-larken-sans text-xsm leading-6 px-3">
                Supported formats
            </span>
            <div class="grid grid-cols-3 justify-items-center gap-0">

                <gradient-info label="jpg"/>
                <gradient-info label="webp"/>
                <gradient-info label="png"/>

            </div>
        </div>
        <!-- <canvas ref="canvas" class="absolute top-0 left-0 aspect-[4/3] h-[280px]" ></canvas> -->
    </div>
</div>
<!-- <span class="relative text-white mt-7 mb-4 font-port-lligat-sans text-2xl leading-6" > 
    Test our service with these images  
</span> -->

</body>
</template>


<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import GradientButton from '@/components/GradientButton.vue';
import GradientInfo from '@/components/GradientInfo.vue';

export default defineComponent({
  	components: { GradientButton, GradientInfo },
	  

  	setup() {
        const cursorX = ref(-30);
        const cursorY = ref(-30);
        const circles = ref<HTMLElement[]>([]);
        const circlePositions = ref<{ x: number, y: number }[]>([]);

        const calculateMousePos = (e: MouseEvent) => {
            cursorX.value = e.clientX;
            cursorY.value = e.clientY;
        };

        const animateCursorCircles = () => {
            const cursor = document.querySelector(".cursor") as HTMLElement;
            if (!cursor) return;

            let x = cursorX.value;
            let y = cursorY.value;

            cursor.style.left = `${x}px`;
            cursor.style.top = `${y}px`;

            circles.value.forEach((circle, index) => {
                circle.style.left = `${x - 10}px`;
                circle.style.top = `${y - 10}px`;
                circle.style.transform = `scale(${(circles.value.length - index) / circles.value.length})`;

                circlePositions.value[index] = { x, y };

                const nextCircle = circlePositions.value[index + 1] || circlePositions.value[0];
                x += (nextCircle.x - x) * 0.3;
                y += (nextCircle.y - y) * 0.3;
            });

            requestAnimationFrame(animateCursorCircles);
        };

        onMounted(() => {
            document.addEventListener('mousemove', calculateMousePos);
            circles.value = Array.from(document.querySelectorAll(".circle")) as HTMLElement[];
            circlePositions.value = circles.value.map(() => ({ x: 0, y: 0 }));
            animateCursorCircles();
        });
		return {
		};
	},
	data() {
		return {
			selectedFile: null as File | null,
		};
	},
	methods: {
		onDragOver(event: Event) {
			event.preventDefault();
			// TODO: Change styles of the dropzone when an item is dragged over it
		},
		async onDrop(event: DragEvent) { 
			event.preventDefault();
			if (event.dataTransfer) {
				const files = event.dataTransfer.files;
				if (files.length == 1) {
					this.selectedFile = files[0];
					if (!this.selectedFile)
						return;

					const formData = new FormData();
					formData.append('image', this.selectedFile);
					await this.sendImageToDataBase(formData);
				} else if (files.length > 1) {
					alert("You can only upload one image at a time");
				}
			}
		},
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
			await this.sendImageToDataBase(formData);
		}, 
		async sendImageToDataBase(formData: FormData) {
			try {
				const response = await fetch('http://localhost:8000/upload/', {
					method: 'POST',
					body: formData
				});
				const data = await response.json();
				console.log(data);
				if (data.message === 'Image uploaded and processing started') {
					// Navigate to the next view with the image_id as a parameter
					this.$router.push({ name: 'display-result', params: { image_id: data.image_id.toString() } });
				}

			}
			catch (error) {
				console.error("Błąd podczas wysyłania obrazu:", error);
			}
		}
	}
});
</script>


<style>
body {
  background-color: #0A0A0A;
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
  background-clip: text;
  -webkit-text-fill-color: transparent;
  white-space: nowrap;
}

.cursor {
  pointer-events: none;

  display: block;
  border-radius: 0;
  mix-blend-mode: difference;
  top: 0;
  left: 0;
  z-index: 99999999;  
}

.circle {
    position: absolute;
    display: block;
    width: 20px;
    height: 20px;
    border-radius: 20px;
    background-color: #fff;
}

</style>