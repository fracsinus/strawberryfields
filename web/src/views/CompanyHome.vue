<script setup>
import { onBeforeMount, ref } from 'vue';
import { useAuthStore } from '@/stores';

const auth = useAuthStore();

let pitchList = ref([]);

onBeforeMount(async () => {
  pitchList.value = await (await fetch(
    `${import.meta.env.VITE_API_HOST}/companies/${auth.user_id}/pitch`,
    {
      headers: {
        Authorization: `Bearer ${auth.access_token}`,
      },
    },
  )).json();
});

</script>

<template>
  <div>
    <h2>피칭 목록</h2>
    <table>
      <thead>
        <tr>
          <th>제목</th>
          <th>보낸 사람</th>
          <th>생성일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="pitch in pitchList">
          <td>{{ pitch.title }}</td>
          <td>{{ pitch.email }}</td>
          <td>{{ pitch.created_at }}</td>
        </tr>
        <td>-</td>
        <td>-</td>
        <td>-</td>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
</style>
