<template>
  <div id="labApp">
    <div class="app_background">
      <iframe
          src="https://guilhermeouriques.github.io/protolabdigital/"
          allowfullscreen>
      </iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DigitalLabApp'
};
</script>

<style scoped>
iframe {
  border: none; /* Remove as bordas do iframe, se necessário */
  width: 960px;
  height: 642px;
}

#labApp {
  text-align: center;
  background-color: #323039;
  height: 100%;
}

.app_background {
  background: white;
  width: 960px;
  margin: 0 auto;
}


</style>