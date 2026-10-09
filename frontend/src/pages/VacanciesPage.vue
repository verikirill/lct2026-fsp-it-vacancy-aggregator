<template>
  <section>
    <h2>Вакансии</h2>
    <div class="card">
      <input v-model="q" placeholder="Поиск по названию" />
      <button class="btn" @click="load">Найти</button>
    </div>
    <div v-for="v in vacancies" :key="v.id" class="card">
      <h3>{{ v.title }}</h3>
      <p>{{ v.company }} · {{ v.city }}</p>
      <router-link :to="`/vacancy/${v.id}`">Подробнее</router-link>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getVacancies } from "../api";

const q = ref("");
const vacancies = ref([]);
const load = async () => (vacancies.value = await getVacancies({ q: q.value }));
onMounted(load);
</script>
