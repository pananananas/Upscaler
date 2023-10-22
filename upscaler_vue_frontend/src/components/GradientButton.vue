<template>
    <button class="btn" shape="round" >
        <span>{{ label }}</span>
    </button>
</template>


<script setup>
import { defineProps, } from 'vue';

const props = defineProps({
    label: {
        type: String,
    },
}
);
</script>


<style>
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

.btn:hover {
  background-color: #0c0c0d;
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
  z-index: -1;
  border-radius: 90px;
  transition: all 0.2s ease 0s;
}

.btn:hover:before {
  box-shadow: rgba(255, 159, 159, 0.7)  0px 0px 10px 0px,
              rgba(139, 92, 246, 0.7)   0px 0px 20px 0px;
}

.btn > span {
  text-align: left;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  word-break: break-all;
}
</style>