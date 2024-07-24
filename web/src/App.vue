<script setup>
import { RouterView } from 'vue-router'
import { useAuthStore } from './stores';
const auth = useAuthStore();
auth.checkStorage();
</script>

<template>
  <RouterView />
</template>

<style scoped>
</style>
