<template>
  <div id="video">
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

img {
  width: auto;
  height: 100%;
}

#video {
  text-align: center;
  background-color: #323039;
  height: 100%;
}
</style>