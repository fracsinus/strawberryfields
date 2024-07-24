import { defineStore } from 'pinia';

const APIHost = import.meta.env.VITE_API_HOST;

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user_type: null,
    access_token: null,
  }),
  getters: {
    isSignedIn(state) {
      return state.access_token !== null;
    },
  },
  actions: {
    async checkStorage() {
      const stored = sessionStorage.getItem('access_token');
      if (stored) {
        this.access_token = stored;
        this.user_type = sessionStorage.getItem('user_type');
        this.user_id = sessionStorage.getItem('user_id');
      }
    },
    async artistSignIn({email, password}) {
      const resp = await fetch(
        `${APIHost}/artists/auth/sign-in`,
        { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email, password }) },
      );
      if (resp.status === 200) {
        const json = await resp.json();
        this.user_id = json.id
        this.user_type = json.user_type;
        this.access_token = json.access_token;
        sessionStorage.setItem('access_token', this.access_token);
        sessionStorage.setItem('user_type', this.user_type);
        sessionStorage.setItem('user_id', this.user_id);
      }

      return this.isSignedIn;
    },
    async companySignIn({email, password}) {
      const resp = await fetch(
        `${APIHost}/companies/auth/sign-in`,
        { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email, password }) },
      );
      if (resp.status === 200) {
        const json = await resp.json();
        this.user_id = json.id
        this.user_type = json.user_type;
        this.access_token = json.access_token;
        sessionStorage.setItem('access_token', this.access_token);
        sessionStorage.setItem('user_type', this.user_type);
        sessionStorage.setItem('user_id', this.user_id);
      }

      return this.isSignedIn;
    },
    async signOut() {
      sessionStorage.removeItem('access_token');
      sessionStorage.removeItem('user_type');
      sessionStorage.removeItem('user_id');
      this.$reset();
    }
  }
})

