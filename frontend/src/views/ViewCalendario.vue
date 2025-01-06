<template>
    <div id="app" class="container mt-4">
      <h1 class="text-center mb-4">Calendário</h1>
      <div class="row">
        <div class="col text-center">
          <button class="btn btn-outline-primary me-2" @click="prevMonth">Anterior</button>
          <span><strong>{{ currentMonth }} {{ currentYear }}</strong></span>
          <button class="btn btn-outline-primary ms-2" @click="nextMonth">Próximo</button>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th v-for="day in daysOfWeek" :key="day" class="text-center">{{ day }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="week in weeks" :key="week">
                <td
                  v-for="date in week"
                  :key="date"
                  :class="['text-center', date.isToday ? 'bg-primary text-white' : '', date.isCurrentMonth ? '' : 'text-muted']"
                >
                  {{ date.day }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ViewCalendario",
    data() {
      return {
        currentDate: new Date(),
        daysOfWeek: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'],
      };
    },
    computed: {
      currentMonth() {
        return this.currentDate.toLocaleString('default', { month: 'long' });
      },
      currentYear() {
        return this.currentDate.getFullYear();
      },
      weeks() {
        const startOfMonth = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth(), 1);
        const endOfMonth = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth() + 1, 0);
  
        const startDay = startOfMonth.getDay();
        const totalDays = endOfMonth.getDate();
  
        const dates = [];
        for (let i = 0; i < startDay; i++) {
          dates.push({ day: '', isToday: false, isCurrentMonth: false });
        }
        for (let i = 1; i <= totalDays; i++) {
          const date = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth(), i);
          const isToday = date.toDateString() === new Date().toDateString();
          dates.push({ day: i, isToday, isCurrentMonth: true });
        }
  
        const weeks = [];
        for (let i = 0; i < dates.length; i += 7) {
          weeks.push(dates.slice(i, i + 7));
        }
        return weeks;
      },
    },
    methods: {
      prevMonth() {
        this.currentDate = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth() - 1, 1);
      },
      nextMonth() {
        this.currentDate = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth() + 1, 1);
      },
    },
  };
  </script>
  
  <style>
  table {
    table-layout: fixed;
  }
  td {
    height: 100px;
    vertical-align: top;
  }
  td.text-muted {
    background-color: #f9f9f9;
  }
  td.bg-primary {
    cursor: pointer;
  }
  </style>
  