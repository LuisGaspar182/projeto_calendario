import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css';
import { createRouter, createWebHistory } from 'vue-router';
import Home from './views/ViewHome.vue';
import Calendario from './views/ViewCalendario.vue';
import Tarefas from './views/ViewTarefas.vue';
import GerenciarTatuador from './views/ViewGerenciarTatuador.vue';
import GerenciarTatuagem from './views/ViewGerenciarTatuagem.vue';

const routes = [
    {path: '/', component: Home},
    {path: '/calendario', component: Calendario},
    {path: '/tarefas', component: Tarefas},
    {path: '/admin/tatuador', component: GerenciarTatuador},
    {path: '/admin/tatuagem', component: GerenciarTatuagem},
  ];
  
  const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  createApp(App)
    .use(router)  // Usando o Vue Router
    .mount('#app');
