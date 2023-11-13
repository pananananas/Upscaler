<template>
<body @dragover.prevent="onDragOver">


<div class="relative mt-36 mx-auto pl-5 grid grid-cols-1 md:grid-cols-2 gap-6 justify-items-center ">

    <div class="">
        <div class="text-7xl font-abril-fatface leading-[76px] text-white w-full">
            Upscale your
            <br />
            <span class="magic_text text-6xl interactable">
            images
            </span>
            
        </div>
        <div class="text-[rgb(232,232,232)] mt-10 mb-4 font-larken-sans text-xl leading-6" >
            We use fast and reliable AI algorithms 
			<br/>
			to enhance resolution of your images.
        </div>
		<div class="flex gap-14">
			<div class="bg-[#D6D6D6] hover:bg-[#f1f1f1] transition ease-in-out duration-300 rounded-[10px] w-[200px] h-9 text-[#070707] font-port-lligat-sans flex items-center justify-center interactable" data-fa-icon="fa-question">
				<span class="  "> How does it work? </span>
			</div>
			<div class="interactable" data-svg-icon="arrow-up-right">
				<input type="file" ref="fileInput" class="hidden" id="fileInput" @change="uploadImage" accept="image/*">
				<gradient-button label="Upload image" shape="round"/>
			</div>
		</div>
    </div>
	<div class=" w-full h-full">
	<div class="flex gap-4 absolute">
		<img src="../assets/imgs/1_downscaled.jpg" alt="Image1" class="object-cover rounded-[10px] w-[180px] h-[180px] ml-4 float-1 interactable">
		<!-- <img src="../assets/imgs/1.jpg" alt="Image1" class="object-cover rounded-[10px] w-[180px] h-[180px]  ml-4 float-1 absolute"> -->
		<img src="../assets/imgs/2_downscaled.jpg" alt="Image2" class="object-cover rounded-[10px] w-[204px] h-[135.6px] float-2">
		<img src="../assets/imgs/3_downscaled.jpg" alt="Image3" class="object-cover rounded-[10px] w-[102px] h-[135.6px] float-3">
		<img src="../assets/imgs/4_downscaled.jpg" alt="Image4" class="object-cover rounded-[10px] w-[180px] h-[135.6px] float-4">
	</div>
	<div class="flex gap-6 absolute top-[154px]">
		<img src="../assets/imgs/5_downscaled.jpg" alt="Image5" class="object-cover rounded-[10px] w-[180px] h-[120px] bottom-0 absolute float-5">
		<img src="../assets/imgs/6_downscaled.jpg" alt="Image6" class="object-cover rounded-[10px] w-[127.2px] h-[192px] ml-[218px] float-6">
		<img src="../assets/imgs/7_downscaled.jpg" alt="Image7" class="object-cover rounded-[10px] w-[135.6px] h-[135.6px] float-7">
		<img src="../assets/imgs/8_downscaled.jpg" alt="Image8" class="object-cover rounded-[10px] w-[102px] h-[135.6px] float-8">
		<img src="../assets/imgs/9_downscaled.jpg" alt="Image9" class="object-cover rounded-[10px] w-[135.6px] h-[135.6px] float-9">
	</div>
	<div class="flex gap-6 absolute top-[328px]">
		<img src="../assets/imgs/10_downscaled.jpg" alt="Image10" class="object-cover rounded-[10px] w-[320.4px] h-[135.6px] bottom-0 absolute ml-6 float-10">
		<img src="../assets/imgs/11_downscaled.jpg" alt="Image11" class="object-cover rounded-[10px] w-[135.6px] h-[180px] ml-[366px] float-11">
		<img src="../assets/imgs/12_downscaled.jpg" alt="Image12" class="object-cover rounded-[10px] w-[273.6px] h-[180px] float-12">
	</div>
</div>

</div>

<div class="bg-[rgba(5,64,73,0.00)] aspect-[4/3] h-[280px] z-10 rounded-[10px] border-dashed border-[transparent] border flex flex-col gap-1  relative overflow-hidden items-center justify-center"/>



<div class="cursor" @drop.prevent="onDrop"> 
	<div class="first-circle">  
		<i v-if="currentIconClass" :class="['fa', currentIconClass]"></i>
  		<arrow-up-right-icon v-else-if="currentSvgIcon === 'arrow-up-right'"></arrow-up-right-icon>
	</div> 
	<div class="circle"/> <div class="circle"/><div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/><div class="circle"/> <div class="circle"/><div class="circle"/> <div class="circle"/><div class="circle"/> <div class="circle"/><div class="circle"/> <div class="circle"/><div class="circle"/> <div class="circle"/><div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> <div class="circle"/> 
</div>
</body>
</template>


<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import GradientInfo from '@/components/GradientInfo.vue';
import GradientButton from '@/components/GradientButton.vue';
import ArrowUpRightIcon from '@/components/ArrowUpRightIcon.vue';

export default defineComponent({
  	components: { GradientButton, GradientInfo, ArrowUpRightIcon},
	  

  	setup() {
		const cursorX = ref<number | null>(null);
		const cursorY = ref<number | null>(null);
		const cursorTail = ref(0.2);
		const interacting = ref(false);

		const currentIconClass = ref<string>(''); 
		const currentSvgIcon = ref<string>('');

		const circles = ref<HTMLElement[]>([]);
		const cursor = ref<HTMLElement | null>(null);
		const firstCircleEl = ref<HTMLElement | null>(null);
		const circlePositions = ref<{ x: number, y: number }[]>([]);

		onMounted(() => {
			cursor.value = document.querySelector(".cursor") as HTMLElement;
			firstCircleEl.value = document.querySelector(".first-circle") as HTMLElement;
			circles.value = Array.from(document.querySelectorAll(".circle")) as HTMLElement[];
			circlePositions.value = circles.value.map(() => ({ x: 0, y: 0 }));
			animateCursorCircles();
		});

		const initializeMousePosition = (e: MouseEvent) => {
			cursorX.value = e.clientX;
			cursorY.value = e.clientY;
			circlePositions.value.forEach(pos => {
				pos.x = e.clientX;
				pos.y = e.clientY;
			});
			circles.value.forEach(circle => {
				circle.classList.add("visible");
			});
			applyPopEffectToFirstCircle();
		};

		const updateMousePosition = (e: MouseEvent) => {
			cursorX.value = e.clientX;
			cursorY.value = e.clientY;
		};

		const applyPopEffectToFirstCircle = () => {
			if (!firstCircleEl.value) return;
			if (!firstCircleEl.value.classList.contains('pop-effect')) {
				firstCircleEl.value.classList.add('pop-effect');
				setTimeout(() => {
					firstCircleEl.value?.classList.remove('pop-effect');
					firstCircleEl.value?.classList.add('visible');
				}, 600);
			}
		};

		const handleInteractableElements = (e: MouseEvent) => {
			if (!(e.target instanceof Element)) return;

			const interactableElement = e.target.closest(".interactable");
			interacting.value = !!interactableElement;

			if (!firstCircleEl.value) return;

			if (interactableElement) {
				firstCircleEl.value.classList.add('interacting');
				firstCircleEl.value.classList.remove('visible');
				cursorTail.value = 0.1;

				setCursorIcon(interactableElement);
			} else {
				firstCircleEl.value.classList.remove('interacting');
				firstCircleEl.value.classList.add('visible');
				cursorTail.value = 0.2;
				clearCursorIcons();
			}
		};

		const setCursorIcon = (element: Element) => {
			const faIconName = element.getAttribute('data-fa-icon');
			const svgIconName = element.getAttribute('data-svg-icon');

			if (faIconName) {
				currentIconClass.value = faIconName;
				currentSvgIcon.value = ''; // Clear SVG icon
			} else if (svgIconName) {
				currentSvgIcon.value = svgIconName;
				currentIconClass.value = ''; // Clear FontAwesome icon
			} else {
				clearCursorIcons();
			}
		};

		const clearCursorIcons = () => {
			currentIconClass.value = ''; // Clear FontAwesome icon
			currentSvgIcon.value = '';   // Clear SVG icon
		};

		const calculateMousePos = (e: MouseEvent) => {
			if (cursorX.value === null || cursorY.value === null)	initializeMousePosition(e);
			else 													updateMousePosition(e);
			handleInteractableElements(e);
		};

		const animateCursorCircles = () => {
			if (!cursor.value || !firstCircleEl.value) return;
			let x = cursorX.value ?? 0;
			let y = cursorY.value ?? 0;
			firstCircleEl.value.style.left = `${x - 8}px`;
			firstCircleEl.value.style.top = `${y - 8}px`;

			circles.value.forEach((circle, index) => {
				circle.style.left = `${x - 8}px`;
				circle.style.top  = `${y - 8}px`;
				const scale = (circles.value.length - index) / circles.value.length;``
				circle.style.transform = `scale(${scale})`;
				circlePositions.value[index] = { x, y };
				const nextCircle = circlePositions.value[index + 1] || circlePositions.value[0];
				x += (nextCircle.x - x) * cursorTail.value;
				y += (nextCircle.y - y) * cursorTail.value;
			});

			requestAnimationFrame(animateCursorCircles);
		};

		document.addEventListener('mousemove', calculateMousePos);

		return {
			calculateMousePos,
			animateCursorCircles,
			currentIconClass,
			currentSvgIcon,
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
			console.log("Drag over");
			this.calculateMousePos(event as MouseEvent);
			this.animateCursorCircles();

			// Change pointer events on cursor for the duration of the drag
			const cursor = document.querySelector(".cursor") as HTMLElement;
			if (cursor) {
				cursor.style.pointerEvents = "auto";
			}

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
  	background-color: #040404;
	overflow-x: hidden;
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
	visibility: hidden;
}

.first-circle {
	position: absolute;
	display: flex;
	width: 16px;
	height: 16px;
	border-radius: 16px;
	background-color: #fff;
	visibility: hidden;
	transition: transform 0.3s ease-out;
	z-index: 101;
	align-items: center; /* Center items vertically */
    justify-content: center; /* Center items horizontally */
}

.circle {
	mix-blend-mode: normal;
    position: absolute;
    display: block;
    width: 16px;
    height: 16px;
    border-radius: 16px;
    background-color: #fff;
	visibility: hidden;
	transition: transform 5s ease-out;
	z-index: 100;  
}

@keyframes popEffect {
	0% {
		transform: scale(0);
	}
	40% {
		transform: scale(2.5);
	}
	100% {
		transform: scale(1);
	}
}

.first-circle.pop-effect {
	visibility: visible;
	animation: popEffect 0.6s ease-out forwards;
}

.first-circle.visible {
  	visibility: visible;
}

.first-circle.interacting {
	visibility: visible;
	transform: scale(4);
	background-color: #fff;
}

.first-circle .fa, .first-circle svg {
    font-size: 8px; 		/* For FontAwesome */
	width: 8px; 			/* For SVG */
    height: 8px; 			/* For SVG */
	
    transition: opacity 0.3s ease-out;
	display: flex;
	justify-content: center; 	/* Center items horizontally */
}

/* Fade-in animation for the icon */
@keyframes fadeIn {
    from { scale: 0; }
    to { scale: 1; }
}

/* Apply the fade-in animation */
.first-circle.interacting .fa, .first-circle.interacting svg {
    animation: fadeIn 0.3s ease-out;
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