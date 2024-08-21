<template>
  <div>
    <div><b>LIGAR MOTOR</b></div>
    <img id="turn-on"
         :src="currentImage"
         @mousedown="changeToClickedImage"
         @mouseup="resetImage"
         @mouseleave="resetImage"
         alt="Turn on">
  </div>
</template>

<script>
export default {
  name: 'TurnOnButton',
  data() {
    return {
      image1: require('@/assets/start-button.png'),
      image2: require('@/assets/pressed-start-button.png'),
      currentImage: require('@/assets/start-button.png')
    };
  },
  methods: {
    changeToClickedImage() {
      this.currentImage = this.image2;
    },
    resetImage() {
      this.currentImage = this.image1;
    }
  }
};
</script>

<style scoped>

#turn-on {
  width: 100px;
  height: auto;
  cursor: pointer;
}

#turn-on:hover {
  opacity: 75%;
}

</style>
