<template>
  <div class="layout">
    <header class="topbar">
      <h1>ФСП Карьера</h1>
      <nav>
        <router-link to="/">Вакансии</router-link>
        <router-link to="/profile/1">Профиль</router-link>
        <router-link to="/recommendations/1">Рекомендации</router-link>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>
