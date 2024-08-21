<template>
  <div>
    <div><b>DESLIGAR MOTOR</b></div>
    <img id="turn-off"
         :src="currentImage"
         @mousedown="changeToClickedImage"
         @mouseup="resetImage"
         @mouseleave="resetImage"
         alt="Desligar motor">
  </div>
</template>

<script>
export default {
  name: 'TurnOffButton',
  data() {
    return {
      image1: require('@/assets/stop-button.png'),
      image2: require('@/assets/pressed-stop-button.png'),
      currentImage: require('@/assets/stop-button.png')
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

#turn-off {
  width: 100px;
  height: auto;
  cursor: pointer;
}

#turn-off:hover {
  opacity: 75%;
}

</style>

