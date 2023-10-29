<template>
  <body class="bg-gray-800">
  </body>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'YourComponentName',
  setup() {
    const router = useRouter();

    onMounted(() => {
      router.push({ name: 'upload-image' });
    });
  }
});
</script>