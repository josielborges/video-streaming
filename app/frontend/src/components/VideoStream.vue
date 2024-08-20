<template>
  <div id="video-container">
    <h2>Live Stream</h2>
    <img :src="videoSrc" alt="Video Stream"/>
  </div>
</template>

<script>
export default {
  name: 'VideoStream',
  props: ['videoSrc']
};
</script>

<style scoped>
#video-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

img {
  width: 100%;
  height: auto;
  border: 1px solid #ddd;
}
</style>