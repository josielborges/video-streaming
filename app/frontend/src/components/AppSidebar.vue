<template>
  <div id="sidebar">
    <h2>Menu</h2>
    <button @click="$emit('clear-logs')">Clear Logs</button>
  </div>
</template>

<script>
export default {
  name: 'AppSidebar'
};
</script>

<style scoped>
#sidebar {
  width: 250px;
  background-color: #f0f0f0;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  box-sizing: border-box;
}
</style>