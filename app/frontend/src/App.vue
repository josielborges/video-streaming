<template>
  <!--  <div>
      <Splitter id="splitter">
        <SplitterPanel class="flex items-center justify-center" :size="15" :minSize="10">
          <Sidebar @clear-logs="clearLogs"/>
        </SplitterPanel>
        <SplitterPanel :size="85">
          <Splitter layout="vertical">
            <SplitterPanel class="flex items-center justify-center" :size="80">
              <VideoStream :videoSrc="videoSrc"/>
            </SplitterPanel>
            <SplitterPanel :size="20">
              <Splitter>
                <SplitterPanel class="flex items-center justify-center" :size="100">
                  <Logs :logs="logs"/>
                </SplitterPanel>
              </Splitter>
            </SplitterPanel>
          </Splitter>
        </SplitterPanel>
      </Splitter>
    </div>-->
<!--  <Menubar :model="items"/>-->
  <div class="container">
    <div class="lado-esquerdo">
      <Sidebar @clear-logs="clearLogs"/>
    </div>
    <div class="lado-direito">
      <VideoStream :videoSrc="videoSrc"/>
<!--      <DigitalLabApp/>-->
<!--      <Logs :logs="logs"/>-->
    </div>
  </div>
</template>

<script>

// import Splitter from 'primevue/splitter';
// import SplitterPanel from 'primevue/splitterpanel';
// import Menubar from 'primevue/menubar';

import Sidebar from '@/components/AppSidebar.vue';
import VideoStream from '@/components/VideoStream.vue';
// import DigitalLabApp from "@/components/DigitalLabApp.vue";

// import Logs from './components/AppLogs.vue';

export default {
  components: {
    Sidebar,
    VideoStream,
    // DigitalLabApp
    // Logs,
    // Menubar
    // Splitter,
    // SplitterPanel
  },
  data() {
    return {
      selectedCamera: 'camera_2',
      cameras: {
        'camera_1': 'Camera 1',
        'camera_2': 'Camera 2'
      },
      logs: '',
      items: [
        {
          label: 'Home',
          icon: 'pi pi-home'
        },
        {
          label: 'Settings',
          icon: 'pi pi-cog'
        }
      ]
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
  },

};

</script>

<style scoped>
/*
#splitter {
  height: 98vh;
}
*/

.container {
  display: grid;
  grid-template-columns: 20% 80%;
  grid-template-rows: 100%;
  height: 90vh;
  width: 90vw;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
}

</style>