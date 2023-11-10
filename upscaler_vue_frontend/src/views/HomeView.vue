<template>
<body>


<div class="relative mt-36 mx-auto pl-5 grid grid-cols-1 md:grid-cols-2 gap-6 justify-items-center ">
    <!-- TODO: Fix this grid -->
    <div class="">
        <div class="text-7xl font-abril-fatface leading-[76px] text-white w-full">
            Upscale your
            <br />
            <span class="magic_text text-6xl">
            images
            </span>
            
        </div>
        <div class="text-[rgb(232,232,232)] mt-10 mb-4 font-larken-sans text-xl leading-6" >
            Enhance resolution of your images using 
            <br/>
            fast and reliable AI powered algorithms.
        </div>
		<div class="flex gap-14">
			<div class="bg-[#D6D6D6] hover:bg-[#f1f1f1] transition ease-in-out duration-300 rounded-[10px] w-[200px] h-9 text-[#070707] font-port-lligat-sans cursor-pointer flex items-center justify-center">
				<span class="  "> How does it work? </span>
			</div>
			<div>
				<input type="file" ref="fileInput" class="hidden" id="fileInput" @change="uploadImage" accept="image/*">
				<gradient-button label="Upload image" shape="round"/>
			</div>
		</div>
    </div>
	<div class=" w-full h-full">
		<div class="flex gap-4 absolute">
			<img src="../assets/imgs/1_downscaled.jpg" alt="Image1" class="object-cover rounded-[10px] w-[150px] h-[150px] hover:scale-105 ml-4 float-1">
			<img src="../assets/imgs/2_downscaled.jpg" alt="Image2" class="object-cover rounded-[10px] w-[170px] h-[113px] hover:scale-105 float-2">
			<img src="../assets/imgs/3_downscaled.jpg" alt="Image3" class="object-cover rounded-[10px] w-[85px] h-[113px] hover:scale-105 float-3">
			<img src="../assets/imgs/4_downscaled.jpg" alt="Image4" class="object-cover rounded-[10px] w-[150px] h-[113px] hover:scale-105 float-4">
		</div>
		<div class="flex gap-6 absolute top-[128px]">
			<img src="../assets/imgs/5_downscaled.jpg" alt="Image5" class="object-cover rounded-[10px] w-[150px] h-[100px] hover:scale-105 bottom-0 absolute float-5">
			<img src="../assets/imgs/6_downscaled.jpg" alt="Image6" class="object-cover rounded-[10px] w-[106px] h-[160px] hover:scale-105 ml-[182px] float-6">
			<img src="../assets/imgs/7_downscaled.jpg" alt="Image7" class="object-cover rounded-[10px] w-[113px] h-[113px] hover:scale-105 float-7">
			<img src="../assets/imgs/8_downscaled.jpg" alt="Image8" class="object-cover rounded-[10px] w-[85px] h-[113px] hover:scale-105 float-8">
			<img src="../assets/imgs/9_downscaled.jpg" alt="Image9" class="object-cover rounded-[10px] w-[113px] h-[113px] hover:scale-105 float-9">
		</div>
		<div class="flex gap-6 absolute top-[274px]">
			<img src="../assets/imgs/10_downscaled.jpg" alt="Image10" class="object-cover rounded-[10px] w-[267px] h-[113px] hover:scale-105 bottom-0 absolute ml-6 float-10">
			<img src="../assets/imgs/11_downscaled.jpg" alt="Image11" class="object-cover rounded-[10px] w-[113px] h-[150px] hover:scale-105 ml-[305px] float-11">
			<img src="../assets/imgs/12_downscaled.jpg" alt="Image12" class="object-cover rounded-[10px] w-[228px] h-[150px] hover:scale-105 float-12">
		</div>
	</div>
</div>



<div class="cursor"> <div class="first-circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> </div>
</body>
</template>


<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import GradientButton from '@/components/GradientButton.vue';
import GradientInfo from '@/components/GradientInfo.vue';

export default defineComponent({
  	components: { GradientButton, GradientInfo },
	  

  	setup() {
        const cursorX = ref<number | null> (null);
        const cursorY = ref<number | null> (null);
        const circles = ref<HTMLElement[]> ([]);
		const firstCircle = ref<HTMLElement[]> ([]);
        const circlePositions = ref<{ x: number, y: number }[]> ([]);

        const calculateMousePos = (e: MouseEvent) => {
			if (cursorX.value === null || cursorY.value === null) {
				const firstCircleEl = document.querySelector(".first-circle") as HTMLElement;
				// Initialize positions
				cursorX.value = e.clientX;
				cursorY.value = e.clientY;
				circlePositions.value.forEach(pos => {
					pos.x = e.clientX;
					pos.y = e.clientY;
				});

				circles.value.forEach(circle => {
					circle.classList.add("visible");
				});
				if (!firstCircleEl.classList.contains('visible')) {
					firstCircleEl.classList.add('visible');
				}

			} else {
				cursorX.value = e.clientX;
				cursorY.value = e.clientY;
			}
		};

		const animateCursorCircles = () => {
			const cursor = document.querySelector(".cursor") as HTMLElement;
			const firstCircleEl = document.querySelector(".first-circle") as HTMLElement;
			if (!cursor || !firstCircleEl) return;

			let x = cursorX.value ?? 0;
			let y = cursorY.value ?? 0;

			// Update the position of the first circle directly
			firstCircleEl.style.left = `${x - 8}px`;
			firstCircleEl.style.top = `${y - 8}px`;

			// Only apply the pop effect to the first circle on the initial mouse move


			// Update positions of the other circles
			circles.value.forEach((circle, index) => {
				circle.style.left = `${x - 8}px`;
				circle.style.top  = `${y - 8}px`;

				const scale = (circles.value.length - index) / circles.value.length;
				circle.style.transform = `scale(${scale})`;

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
  	background-color: #0e0e0e;

	/* overflow-x: hidden; */


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
	display: block;
	border-radius: 0;
	pointer-events: none;
	mix-blend-mode: difference;
	top: 0;
	left: 0;
	z-index: 1000;
}

.first-circle {
	position: absolute;
	display: block;
	width: 16px;
	height: 16px;
	border-radius: 16px;
	background-color: #fff;
	/* Initially hide the circles */
	visibility: hidden;
	/* Scale transition */
	transition: transform 5s ease-out;
	z-index: 101;
}

.circle {
    position: absolute;
    display: block;
    width: 16px;
    height: 16px;
    border-radius: 16px;
    background-color: #fff;
	/* Initially hide the circles */
	visibility: hidden;
	/* Scale transition */
	transition: transform 5s ease-out;
	z-index: 100;  
}

@keyframes popEffect {
  0% {
    transform: scale(0);
  }
  30% {
    transform: scale(1.8);
  }
  100% {
	transform: scale(1);
  }
}

.first-circle.visible {
  /* Make the circle visible and apply the pop effect */
  visibility: visible;
  animation: popEffect 0.5s ease-out forwards;
}

@keyframes floatInFromLeft {
  from {
    transform: translateX(100vw);
    opacity: 0.9;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.float-1 {
  animation: floatInFromLeft 0.5s ease-out forwards;
}
.float-2 {
  animation: floatInFromLeft 0.6s ease-out forwards;
}
.float-3 {
  animation: floatInFromLeft 0.72s ease-out forwards;
}
.float-4 {
  animation: floatInFromLeft 0.84s ease-out forwards;
}
.float-5 {
  animation: floatInFromLeft 0.4s ease-out forwards;
}
.float-6 {
  animation: floatInFromLeft 0.54s ease-out forwards;
}
.float-7 {
  animation: floatInFromLeft 0.66s ease-out forwards;
}
.float-8 {
  animation: floatInFromLeft 0.78s ease-out forwards;
}
.float-9 {
  animation: floatInFromLeft 0.9s ease-out forwards;
}
.float-10 {
  animation: floatInFromLeft 0.48s ease-out forwards;
}
.float-11 {
  animation: floatInFromLeft 0.6s ease-out forwards;
}
.float-12 {
  animation: floatInFromLeft 0.72s ease-out forwards;
}

</style>