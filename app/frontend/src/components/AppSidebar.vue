<template>
  <div id="sidebar">
    <div id="command-buttons">
      <div>
        <TurnOnButton/>
        <br>
        <TurnOffButton/>
        <br>
        <br>
      </div>
    </div>
  </div>
</template>

<script>
import TurnOnButton from '@/components/TurnOnButton.vue';
import TurnOffButton from '@/components/TurnOffButton.vue';

export default {
  name: 'AppSidebar',
  components: {
    TurnOnButton,
    TurnOffButton,
  }
};
</script>

<style scoped>
#sidebar {
  height: 100%;
  text-align: center;
  background-color: #aebcc2;
  color: #534e4e;
}

#command-buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>