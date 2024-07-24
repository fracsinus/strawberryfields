<script setup>
import router from '@/router';
import { useAuthStore } from '@/stores';
import ArtistHome from './ArtistHome.vue';
import CompanyHome from './CompanyHome.vue';

const auth = useAuthStore();

async function signOut() {
  await auth.signOut();
  router.push('sign-in');
}
</script>

<template>
  <nav>
    <button @click="signOut()">로그아웃</button>
  </nav>
  <main>
    <ArtistHome v-if="auth.user_type === 'artists'" />
    <CompanyHome v-else />
  </main>
</template>

<style scoped>
</style>
