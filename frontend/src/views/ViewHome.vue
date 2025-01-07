<template>
    <div>
      <div v-show="!adminActive">
        <h1>Bem-vindo ao MinhaApp!</h1>
        <p>Este é o conteúdo da página inicial.</p>
      </div>
      <div v-show="adminActive">
        <h1>Área de administração</h1>
        <div class="btn-group" role="group" aria-label="Basic example">
          <button type="button" class="btn btn-primary"><router-link to="/admin/tatuador" class="nav-link">Gerenciar Tatuadores</router-link></button>
          <button type="button" class="btn btn-primary">Gerenciar Clientes</button>
          <button type="button" class="btn btn-primary"><router-link to="/admin/tatuador" class="nav-link">Gerenciar Tatuagens</router-link></button>
        </div>
      </div>
    </div>
</template>
  
<script>
  export default {
    name: 'ViewHome',
    data()  {
      return  {
        adminActive: true,
      };
    },
  };
</script>