<template>
<!--  <div id="log-container">-->
    <h2>Logs</h2>
    <canvas id="line-chart" width="100%" height="100%"></canvas>
<!--  </div>-->
</template>

<script>
export default {
  name: 'AppLogs',
  props: ['logs']
};
</script>

<!--
<style scoped>
#log-container {
  height: 150px;
  overflow-y: auto;
  background-color: #f4f4f4;
  padding: 10px;
  border-top: 1px solid #ddd;
}
</style>-->
