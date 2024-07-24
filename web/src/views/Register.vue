<script setup>
import { ref } from 'vue';
import router from '@/router';

let selectedUserType = ref("artists");
let input = ref({email: "", password: "", passwordCheck: ""});

async function register({ email, password, passwordCheck }) {
  if (!email || !password || !passwordCheck) {
    window.alert("모든 필드를 입력해주세요.");
    return;
  }
  if (password !== passwordCheck) {
    window.alert("비밀번호가 일치하지 않습니다.");
    return;
  }

  const resp = await fetch(
    `${import.meta.env.VITE_API_HOST}/${selectedUserType.value}/auth/register`,
    { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email, password }) }
  );

  if (resp.status === 200) {
    window.alert("회원가입에 성공했습니다.");
    router.push({ name: 'sign-in' });
  }
}
</script>

<template>
  <main>
    <div>
      <div class="selector">
        <label :class="{ selected: selectedUserType === 'artists' }">
          작곡가
          <input type="radio" name="user_type" value="artists" v-model="selectedUserType"></input>
        </label>
        <label :class="{ selected: selectedUserType === 'companies' }">
          기획사
          <input type="radio" name="user_type" value="companies" v-model="selectedUserType"></input>
        </label>
      </div>
      <div>
        <label>
          <p>이메일</p>
          <input type="email" v-model="input.email">
        </label>
        <label>
          <p>비밀번호</p>
          <input type="password" v-model="input.password">
        </label>
        <label>
          <p>비밀번호 확인</p>
          <input type="password" v-model="input.passwordCheck">
        </label>
      </div>
      <button @click="register(input)">회원가입</button>
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
}

div.selector {
  display: flex;
  justify-content: space-between;

  label {
    background-color: #ccc;
    padding: 0.2em;
    margin: 0.2em;
    border-radius: 5px;
    text-align: center;
    flex-grow: 1;

    &:not(.selected):hover {
      cursor: pointer;
      outline: 2px solid #388cf9;
    }

    &.selected {
      background-color: #eee;
      outline: 2px solid #ccc;
    }
  }
  input[type=radio] {
    display: none;
  }
}
</style>
