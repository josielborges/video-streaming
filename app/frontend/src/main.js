import {createApp} from 'vue'
import App from './App.vue'

// Import PrimeVue
import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/lara';
import './static/style.css';

const app = createApp(App);

app.use(PrimeVue, {
    // Default theme configuration
    theme: {
        preset: Aura,
        options: {
            prefix: 'p',
            darkModeSelector: '.p-app-dark', // not working
            cssLayer: false
        }
    }
});

app.mount('#app');