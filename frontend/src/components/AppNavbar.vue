<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">MinhaApp</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link to="/" class="nav-link" active-class="active">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/calendario" class="nav-link">Calendário</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/tarefas" class="nav-link">Tarefas</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: "AppNavbar",
  };
  </script>
  
  <style>
  /* Estilização adicional opcional */
  .navbar-brand {
    font-weight: bold;
  }
  </style>