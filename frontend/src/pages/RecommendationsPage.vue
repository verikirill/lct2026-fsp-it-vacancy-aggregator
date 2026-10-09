<template>
  <section>
    <h2>Подходящие вакансии</h2>
    <div v-for="r in items" :key="r.vacancy_id" class="card">
      <h3>{{ r.title }}</h3>
      <p>Совпадение: {{ (r.score * 100).toFixed(0) }}%</p>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { getRecommendations } from "../api";

const route = useRoute();
const items = ref([]);
onMounted(async () => (items.value = await getRecommendations(route.params.userId)));
</script>
