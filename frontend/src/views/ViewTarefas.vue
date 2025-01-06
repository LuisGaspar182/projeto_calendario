<template>
    <div>
      <h1>Tarefas</h1>
      <form class="row g-3" @submit.prevent="submitForm">
        <div class="col-md-3">
          <label for="inputNome">Nome</label>
          <input type="text" class="form-control" id="inputNome" v-model="FormData.Nome">
        </div>
        <div class="col-md-3">
          <label for="inputTatuador">Tatuador</label>
          <select class="form-select form-select-sm" id="inputTatuador" v-model="FormData.Tatuador">
            <option value="" selected>Qualquer</option>
            <option value="Rafael">Rafael</option>
            <option value="Matheus">Matheus</option>
            <option value="Joao">Joao</option>
          </select>
        </div>
        <div class="col-md-3">
          <label for="inputData">Data</label>
          <input type="date" class="form-control" id="inputData" v-model="FormData.Data">
        </div>
        <div class="col-md-3">
          <br>
          <button type="submit" class="btn btn-primary" id="filtrar">Filtrar</button>
        </div>
      </form>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Nome</th>
            <th scope="col">Contato</th>
            <th scope="col">Tatuador</th>
            <th scope="col">Data</th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr>
            <td>Mark Otto</td>
            <td>31 191919191</td>
            <td>Rafael</td>
            <td>23/12/2030</td>
          </tr>
          <tr>
            <td>Mark Otto</td>
            <td>31 191919191</td>
            <td>Rafael</td>
            <td>23/12/2030</td>
          </tr>
          <tr>
            <td>Mark Otto</td>
            <td>31 191919191</td>
            <td>Rafael</td>
            <td>23/12/2030</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ViewTarefas',
    data(){
      return {
        FormData: {
          Nome: "",
          Tatuador: "",
          Data: "",
        },
        submitted_filter: false,
      };
    },
    methods: {
      submitForm() {
        this.submitted_filter= true;
        console.log(this.FormData);
      }
    }
  };
  </script>