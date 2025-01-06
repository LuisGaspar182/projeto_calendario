<template>
  <div id="app">
    <AppNavbar />

    <div class="container mt-4">
      <router-view /> <!-- Aqui o conteúdo da página será exibido -->
    </div>
  </div>
</template>

<script>
import AppNavbar from './components/AppNavbar.vue';  // Importando a Navbar

export default {
  name: 'App',
  components: {
    AppNavbar,
  },
};
</script>

<style>
/* Estilos adicionais para o layout */
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>