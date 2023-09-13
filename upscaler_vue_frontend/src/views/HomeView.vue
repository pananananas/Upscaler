<template>
  <div>
    <input type="file" ref="fileInput" @change="uploadImage">
    <button @click="sendToBackend">Prześlij do backendu</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null
    };
  },
  methods: {
    uploadImage(event) {
      this.selectedFile = event.target.files[0];
    },
    async sendToBackend() {
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













<!-- <template>
  <div class="flex flex-wrap">
    <div class="font-port-lligat-sans text-5xl">
      This text is in Port Lligat Sans.
    </div>

    <div class="font-port-lligat-slab text-5xl">
      This text is in Port Lligat Slab.
    </div>
  </div>
</template>


<script lang="ts">


import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  components: {

  },
});
</script> -->
