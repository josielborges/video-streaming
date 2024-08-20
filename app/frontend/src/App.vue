<template>
  <div id="app">
    <h1>Camera Streams</h1>
    <div id="camera-container">
      <select v-model="selectedCamera" @change="changeCamera">
        <option v-for="(name, id) in cameras" :key="id" :value="id">{{ name }}</option>
      </select>
      <div id="video-container">
        <img :src="videoSrc" alt="Video Stream">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedCamera: 'camera_1',
      cameras: {
        'camera_1': 'Camera 1',
        'camera_2': 'Camera 2'
      }
    };
  },
  computed: {
    videoSrc() {
      return `/video_feed/${this.selectedCamera}`;
    }
  },
  methods: {
    changeCamera() {
      // A mudança no seletor automaticamente atualizará a fonte do vídeo
    }
  }
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 20px;
  text-align: center;
}

h1 {
  color: #333;
}

#camera-container {
  margin-top: 20px;
}

#video-container {
  margin-top: 20px;
}

img {
  width: 80%;
  height: auto;
  border: 2px solid #333;
}
</style>