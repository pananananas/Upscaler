<template>

    <a class="btn" shape="round" >
        <span>{{ label }}</span>
    </a>

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
body {
  margin: 5;
  padding: 5;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: rgba(28, 28, 28, 0.90);
  font-family: Port Lligat Sans;
  font-weight: 500;
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
  transition: background-color 0.2s ease-in-out;
  justify-content: center;
  text-align: center;
  cursor: pointer; /* Not included according to website */
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
    /* rgb(0, 220, 130),
    rgb(54, 228, 218) */
  );
  inset: -2px;
  z-index: -1;
  border-radius: 90.5px;
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