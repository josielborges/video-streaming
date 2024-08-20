<template>
  <div id="app">
    <div id="sidebar">
      <h2>Menu</h2>
      <!-- Adicione seus botões e menus aqui -->
      <button @click="clearLogs">Clear Logs</button>
      <!-- Mais botões ou menus -->
    </div>

    <div id="content">
      <div id="video-container">
        <h2>Live Stream</h2>
        <img :src="videoSrc" alt="Video Stream"/>
      </div>
      <div id="log-container">
        <h2>Logs</h2>
        <pre>{{ logs }}</pre>
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
      },
      logs: ''
    };
  },
  computed: {
    videoSrc() {
      return `/video_feed/${this.selectedCamera}`;
    }
  },
  methods: {
    clearLogs() {
      this.logs = ''; // Limpa os logs
    }
  }
};
</script>

<style>
#app {
  display: flex;
  height: 100vh;
  margin: 0;
  font-family: Arial, sans-serif;
}

#sidebar {
  width: 250px;
  background-color: #f0f0f0;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  box-sizing: border-box;
}

#content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
}

#video-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

#log-container {
  height: 150px;
  overflow-y: auto;
  background-color: #f4f4f4;
  padding: 10px;
  border-top: 1px solid #ddd;
}

h2 {
  margin-top: 0;
}

img {
  width: 100%;
  height: auto;
  border: 1px solid #ddd;
}
</style>