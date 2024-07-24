<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores';
import router from '@/router';

const auth = useAuthStore();
let selectedUserType = ref("artists");
let input = ref({email: "", password: ""});

async function signIn({ email, password }) {
  if (!email || !password) {
    return;
  }

  console.log(selectedUserType.value);
  try {
    if (selectedUserType.value === "artists") {
      await auth.artistSignIn({ email, password });
    } else if (selectedUserType.value === "companies") {
      await auth.companySignIn({ email, password });
    } else {
      console.error("[ERROR] invalid value for `selectedUserType`", selectedUserType.value);
      return;
    }
  } catch {
    window.alert("로그인에 실패하였습니다.");
    return;
  }

  router.push({ name: 'home' });
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
      </div>
      <button @click="signIn(input)">로그인</button>
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
