<template>
  <section v-if="profile">
    <h2>{{ profile.full_name }}</h2>
    <div class="card">
      <p>Рейтинг ФСП: <b>{{ profile.fsp_rating }}</b></p>
      <button class="btn" @click="sync">Обновить из ФСП</button>
    </div>
    <div class="card">
      <h3>Достижения</h3>
      <table>
        <tr v-for="a in profile.achievements" :key="a.title">
          <td>{{ a.title }}</td>
          <td>{{ a.place }} место</td>
          <td>{{ a.level }}</td>
        </tr>
      </table>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { getProfile, syncFsp } from "../api";

const route = useRoute();
const profile = ref(null);
const load = async () => (profile.value = await getProfile(route.params.id));
const sync = async () => {
  await syncFsp(route.params.id);
  await load();
};
onMounted(load);
</script>
