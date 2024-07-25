<script setup>
import { onBeforeMount, ref } from 'vue';
import { useAuthStore } from '@/stores';

const auth = useAuthStore();

let pitchList = ref([]);

onBeforeMount(async () => {
  pitchList.value = await (await fetch(
    `${import.meta.env.VITE_API_HOST}/companies/${auth.user_id}/pitch`,
    { headers: { Authorization: `Bearer ${auth.access_token}` } },
  )).json();
});

async function getPitch(companyId, musicId) {
  const resp = await fetch(
    `${import.meta.env.VITE_API_HOST}/companies/${companyId}/pitch/${musicId}`,
    { headers: { Authorization: `Bearer ${auth.access_token}` } },
  );
  const filename = (/filename="(.*)"/.exec(resp.headers.get("Content-Disposition")) || [])[1] || "download";
  const blob = await resp.blob();
  const objectURL = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = objectURL;
  a.download = filename;
  a.click();
  window.URL.revokeObjectURL(objectURL);
}

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
          <th>-</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="pitch in pitchList">
          <td>{{ pitch.title }}</td>
          <td>{{ pitch.email }}</td>
          <td>{{ pitch.created_at }}</td>
          <td>
            <button @click="getPitch(auth.user_id, pitch.music_id)">다운로드</button>
          </td>
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
