<template>
    <div>
        <div class="row align-items-start">
            <div class="col">
                <h2> Gerenciar Tatuador</h2>
            </div>
            <div class="col-md-4 offset-md-4">
                <img v-if="!addActive" src="../assets/plus-lg.svg" alt="adicionar tatuador" class="botao_adcionar" @click="addActive = true">
                <img v-if="addActive" src="../assets/x.svg" alt="adicionar tatuador" class="botao_adcionar" @click="addActive = false">
            </div>
        </div> 

      <form v-if="addActive" class="row g-3" @submit.prevent="adicionarTatuador">
        <div class="col-md-3">
            <label for="nomeTatuador" class="form-label">Nome</label>
            <input v-model="nome"  type="text" class="form-control" id="nomeTatuador" placeholder="Nome" required >
        </div>
        <div class="col-md-3">
            <label for="emailDoTatuador" class="form-label">Email</label>
            <input v-model="email"  type="email" class="form-control" id="emailDoTatuador" placeholder="name@example.com" required >
        </div>
        <div class="col-md-3">
            <label for="teledoneTatuador" class="form-label">Telefone</label>
            <input v-model="telefone"  type="text" class="form-control" id="teledoneTatuador" placeholder="(xx) xxxxx-xxxx" required >
        </div>
        <div class="col-md-3">
            <br>
            <button type="submit" class="btn btn-primary">Salvar</button>
        </div>
      </form>
      <div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
                <th class="text-nowrap" scope="col">#</th>
                <th class="text-nowrap" scope="col">Nome</th>
                <th class="text-nowrap" scope="col">Email</th>
                <th class="text-nowrap" scope="col">Telefone</th>
                <th class="text-nowrap" scope="col">Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="tatuador in tatuadores" :key="tatuador.id">
                    <th scope="row">{{ tatuador.id }}</th>
                    <td class="text-nowrap" v-if="tatuadorSelecionado != tatuador">{{ tatuador.nome }}</td>
                    <td class="text-nowrap" v-if="tatuadorSelecionado != tatuador">{{ tatuador.email }}</td>
                    <td class="text-nowrap" v-if="tatuadorSelecionado != tatuador">{{ tatuador.telefone }}</td>
                    <td class="text-nowrap" v-if="tatuadorSelecionado != tatuador">
                        <button @click="tatuadorSelecionado = tatuador" class="btn btn-primary btn-sm">Editar</button>
                        <button @click="excluirTatuador(tatuador.id)" class="btn btn-danger btn-sm" style="margin-left: 5px;">Excluir</button>
                    </td>

                    <td class="text-nowrap" v-if="tatuadorSelecionado == tatuador"><input v-model="tatuadorSelecionado.nome" type="text" class="form-control" id="nomeTatuador" required ></td>
                    <td class="text-nowrap" v-if="tatuadorSelecionado == tatuador"><input v-model="tatuadorSelecionado.email" type="email" class="form-control" id="emailDoTatuador" required ></td>
                    <td class="text-nowrap" v-if="tatuadorSelecionado == tatuador"><input v-model="tatuadorSelecionado.telefone" type="text" class="form-control" id="teledoneTatuador" required ></td>
                    <td class="text-nowrap" v-if="tatuadorSelecionado == tatuador">
                        <button @click="salvarEdicao()" class="btn btn-primary btn-sm">Salvar</button>
                        <button @click="tatuadorSelecionado = null" class="btn btn-danger btn-sm" style="margin-left: 5px;">Cancelar</button>
                    </td>
                </tr>
            </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        nome: '',
        email: '',
        telefone: '',
        tatuadores: [],
        tatuadorSelecionado: null,
        addActive: false,
      };
    },
    methods: {
        async buscarTatuadores() {
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/tatuadores/");
                this.tatuadores = response.data;
            } catch (error) {
                console.error("Erro ao buscar tatuadores:", error);
            }
        },    
        async adicionarTatuador() {
            try {
                await axios.post('http://127.0.0.1:8000/api/tatuadores/', {
                nome: this.nome,
                email: this.email,
                telefone: this.telefone,
                });
                this.nome = "";
                this.email = "";
                this.telefone = "";
                alert('Tatuador adicionado com sucesso!');
                this.buscarTatuadores();
            } catch (error) {
                console.error(error);
                alert('Erro ao adicionar tatuador.');
            }
        },
        async excluirTatuador(id) {
            if (confirm("Tem certeza que deseja excluir este tatuador?")) {
                try {
                await axios.delete(`http://127.0.0.1:8000/api/tatuadores/${id}/`);
                alert("Tatuador excluído com sucesso!");
                this.buscarTatuadores(); // Atualiza a lista
                } catch (error) {
                console.error("Erro ao excluir tatuador:", error);
                alert("Erro ao excluir tatuador.");
                }
            }
        },
        async salvarEdicao() {
            try {
                await axios.put(
                `http://127.0.0.1:8000/api/tatuadores/${this.tatuadorSelecionado.id}/`,
                    this.tatuadorSelecionado
                );
                alert("Tatuador editado com sucesso!");
                this.tatuadorSelecionado = null;
                this.buscarTatuadores(); // Atualiza a lista
            } catch (error) {
                console.error("Erro ao salvar edição:", error);
                alert("Erro ao salvar edição.");
            }
        },
    },
    mounted() {
        this.buscarTatuadores();
    }
  };
  </script>

<style>
    .botao_adcionar{
        min-height: 20px;
        cursor: pointer;
    }
</style>
  