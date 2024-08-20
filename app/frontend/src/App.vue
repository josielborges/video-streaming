<template>
  <div id="app">
    <Sidebar @clear-logs="clearLogs"/>
    <div id="content">
      <VideoStream :videoSrc="videoSrc"/>
      <Logs :logs="logs"/>
    </div>
  </div>
</template>

<script>

import Sidebar from './components/AppSidebar.vue';
import VideoStream from './components/VideoStream.vue';
import Logs from './components/AppLogs.vue';

export default {
  components: {
    Sidebar,
    VideoStream,
    Logs
  },
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
      this.logs = '';
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

#content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
}
</style>