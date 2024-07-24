<script setup>
import router from "@/router";
import { onBeforeMount, ref } from "vue";
import { useAuthStore } from "@/stores";
const auth = useAuthStore();
const { musicId } = defineProps(["musicId"]);
const emit = defineEmits(["exit", "finish"]);

let companies = ref([]);
let selectedCompanyId = ref(null);

onBeforeMount(async () => {
  companies.value = await (await fetch(
    `${import.meta.env.VITE_API_HOST}/artists/${auth.user_id}/music/${musicId}/companies`,
    { headers: { Authorization: `Bearer ${auth.access_token}` } },
  )).json();
});

async function pitch(companyId) {
  if (companyId === null) { return; }
  const resp = await fetch(
    `${import.meta.env.VITE_API_HOST}/artists/${auth.user_id}/pitch`,
    {
      method: "POST",
      body: JSON.stringify({ music_id: musicId, company_id: companyId }),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${auth.access_token}`,
      },
    },
  );
  if (resp.ok) {
    window.alert("제출 성공");
    return emit("finish");
  } else {
    window.alert("제출 실패");
    return;
  }
}
</script>

<template>
  <div>
    <h3>피칭을 보낼 회사를 선택하세요</h3>
    <button @click="$emit('exit')">취소</button>
    <select v-model="selectedCompanyId">
      <option :value="null">-</option>
      <option v-for="company in companies" :key="company.id" :value="company.id">{{ company.email }}</option>
    </select>
  </div>
  <button @click="pitch(selectedCompanyId)">제출하기</button>
</template>

<style lang="scss">
</style>
