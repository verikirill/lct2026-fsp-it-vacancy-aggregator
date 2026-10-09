<template>
  <section v-if="vacancy" class="card">
    <h2>{{ vacancy.title }}</h2>
    <p><b>{{ vacancy.company }}</b>, {{ vacancy.city }}</p>
    <p>{{ vacancy.salary_from }} - {{ vacancy.salary_to }} ₽</p>
    <div v-html="vacancy.description"></div>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { getVacancy } from "../api";

const route = useRoute();
const vacancy = ref(null);
onMounted(async () => (vacancy.value = await getVacancy(route.params.id)));
</script>
