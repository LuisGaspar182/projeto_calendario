import { createRouter, createWebHistory } from 'vue-router';
import Home from './views/Home.vue';
import Calendario from './views/ViewCalendario.vue';
import Sobre from './views/Sobre.vue';
import GerenciarTatuador from './views/ViewGerenciarTatuador.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/calendario', component: Calendario },
  { path: '/sobre', component: Sobre },
  {path: '/admin/tatuador', component: GerenciarTatuador}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
