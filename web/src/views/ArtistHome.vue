<script setup>
import router from '@/router';
import { onBeforeMount, ref } from 'vue';
import { useAuthStore } from '@/stores';
import PitchModal from '@/components/PitchModal.vue';

const auth = useAuthStore();

let musicList = ref([]);
let pitchList = ref([]);
let input = ref({title: ''});
let pitchingMusicId = ref(null);

onBeforeMount(async () => {
  musicList.value = await (await fetch(
    `${import.meta.env.VITE_API_HOST}/artists/${auth.user_id}/music`,
    {
      headers: {
        Authorization: `Bearer ${auth.access_token}`,
      },
    },
  )).json();
  pitchList.value = await (await fetch(
    `${import.meta.env.VITE_API_HOST}/artists/${auth.user_id}/pitch`,
    {
      headers: {
        Authorization: `Bearer ${auth.access_token}`,
      },
    },
  )).json();
});

async function upload({ title }) {
  if (!title) {
    window.alert("곡명을 입력하세요");
    return;
  }
  const data = new FormData();
  const fileInput = document.querySelector("input[type=file]");
  data.append("file", fileInput.files[0]);
  data.append("title", title);
  try {
    await fetch(
      `${import.meta.env.VITE_API_HOST}/artists/${auth.user_id}/music`,
      {
        method: "POST",
        body: data,
        headers: {
          Authorization: `Bearer ${auth.access_token}`,
        },
      },
    );
  } catch {
    window.alert("업로드 실패");
    return;
  }

  window.alert("업로드 성공");
  router.go();
}

async function startPitching(musicId) {
  pitchingMusicId.value = musicId;
}

</script>

<template>
  <div>
    <h2>새 음악 업로드</h2>
    <label>
      곡명
      <input type="text" v-model="input.title">
    </label>
    <input type="file">
    <button @click="upload(input)">업로드</button>
  </div>
  <div>
    <h2>업로드한 음악</h2>
    <table>
      <thead>
        <tr>
          <th>제목</th>
          <th>파일명</th>
          <th>생성일</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="music in musicList">
          <td>{{ music.title }}</td>
          <td>{{ music.filename }}</td>
          <td>{{ music.created_at }}</td>
          <td>
            <button @click="startPitching(music.id)">피칭하기</button>
          </td>
        </tr>
        <td>-</td>
        <td>-</td>
        <td>-</td>
      </tbody>
    </table>
  </div>
  <PitchModal v-if="pitchingMusicId !== null" :musicId="pitchingMusicId" @exit="pitchingMusicId = null" @finish="router.go()"/>
  <div>
    <h2>피칭한 음악</h2>
    <table>
      <thead>
        <tr>
          <th>제목</th>
          <th>받는이</th>
          <th>보낸 날짜</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="pitch in pitchList">
          <td>{{ pitch.title }}</td>
          <td>{{ pitch.email }}</td>
          <td>{{ pitch.created_at }}</td>
          <td>
            <button @click="startPitching(pitch.id)">피칭하기</button>
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
td {
  padding: 10px;
}
</style>
