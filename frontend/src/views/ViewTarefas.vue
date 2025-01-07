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
          <button type="button" class="btn btn-primary" id="adicionar_tatuagem" @click="menu_adicionar_tatu = true" style="margin-left: 5px;">Adicionar</button>
        </div>
      </form>

      <div v-if="isLoading" class="d-flex justify-content-center">
        <div class="spinner-border text-primary" role="status">
          <span class="sr-only">Carregando...</span>
        </div>
      </div>

      <table v-else class="table">
        <thead>
          <tr>
            <th scope="col">Nome</th>
            <th scope="col">Contato</th>
            <th scope="col">Tatuador</th>
            <th scope="col">Data</th>
            <th scope="col">Horário</th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr v-for="tatuagem in tatuagens" :key="tatuagem.id">
            <td>{{ getNomeCliente(tatuagem.cliente) }}</td>
            <td>{{ getTelefoneCliente(tatuagem.cliente) }}</td>
            <td>{{ getNomeTatuador(tatuagem.tatuador) }}</td>
            <td>{{ tatuagem.data }}</td>
            <td>{{ tatuagem.horas }}</td>
          </tr>
        </tbody>
      </table>
      <div 
      v-if="menu_adicionar_tatu" 
        class="modal d-flex justify-content-center align-items-center show" 
        tabindex="-1" 
        role="dialog"
        style="display: block; background-color: rgba(0, 0, 0, 0.5);"
      >
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Menu Centralizado</h5>
              <img src="../assets/x.svg" alt="Fechar" @click="menu_adicionar_tatu = false" class="botao-fechar">
            </div>
            <div class="modal-body">
              <form @submit.prevent="handleSubmit">
                <div class="form-group">
                  <label for="exampleInput">Digite algo:</label>
                  <input type="text" class="form-control" id="exampleInput" v-model="inputValue" />
                </div>
                <button type="submit" class="btn btn-success">Enviar</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';


  export default {
    name: 'ViewTarefas',
    data(){
      return {
        FormData: {
          Nome: "",
          Tatuador: "",
          Data: "",
          Horas: "",
          Email: "",
          Telefone: "",
          tatuagens: [],
          clientes: [],
          tatuadores: [],
          isLoading: true,
        },
        submitted_filter: false,
        menu_adicionar_tatu: false,
      };
    },
    methods: {
      submitForm() {
        this.submitted_filter= true;
        console.log(this.FormData);
      },
      handleSubmit() {
      alert(`Formulário enviado com: ${this.inputValue}`);
      this.menu_adicionar_tatu = false;
      },
      async buscarTatuagem() {
        this.isLoading = true;
        try {
            const tatuagensResponse = await axios.get("http://127.0.0.1:8000/api/tatuagens/");
            this.tatuagens = tatuagensResponse.data;
            console.log(this.tatuagens)
            const clientesResponse = await axios.get("http://127.0.0.1:8000/api/clientes/");
            this.clientes = clientesResponse.data;
            const tatuadoresResponse = await axios.get("http://127.0.0.1:8000/api/tatuadores/");
            this.tatuadores = tatuadoresResponse.data;
        } catch (error) {
            console.error("Erro ao buscar dados:", error);
        } finally {
          this.isLoading = false;
        }
      },
      getNomeTatuador(tatuadorId) {
        const tatuador = this.tatuadores.find(t => t.id === tatuadorId);
        return tatuador ? tatuador.nome : "Desconhecido";
      },
      getNomeCliente(clienteId) {
        const cliente = this.clientes.find(t => t.id === clienteId);
        return cliente ? cliente.nome : "Desconhecido";
      },
      getTelefoneCliente(clienteId) {
        const cliente = this.clientes.find(t => t.id === clienteId);
        return cliente ? cliente.telefone : "Desconhecido";
      }, 

    },
    mounted() {
      this.buscarTatuagem();
    },
  };
  </script>
  <style>
    .botao-fechar{
      cursor: pointer; 
      margin-left:auto; 
      min-height: 30px;
    }
  </style>