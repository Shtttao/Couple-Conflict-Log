<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { login } from '../utils/auth.js'
import CoupleAvatar from '../components/CoupleAvatar.vue'

const router = useRouter()
const route = useRoute()
const username = ref('')
const password = ref('')
const shake = ref(false)
const error = ref('')

function onSubmit () {
  error.value = ''
  const result = login(username.value.trim(), password.value)
  if (!result.ok) {
    error.value = result.message
    shake.value = true
    setTimeout(() => (shake.value = false), 600)
    return
  }
  const redirect = route.query.redirect || '/home'
  router.replace(redirect)
}

function quickFill (who) {
  if (who === 'A') {
    username.value = 'loverA'
    password.value = 'together4ever'
  } else {
    username.value = 'loverB'
    password.value = 'myheartforyou'
  }
  onSubmit()
}
</script>

<template>
  <div class="login-wrap">
    <div class="login-card" :class="{ shake }">
      <div class="login-hero">
        <CoupleAvatar variant="together" size="big" />
        <h1 class="login-title">情侣吵架日记</h1>
        <p class="login-sub">两颗心一起反思的温暖小角落 ♡</p>
      </div>

      <form class="login-form" @submit.prevent="onSubmit">
        <label class="field">
          <span>账号</span>
          <input
            v-model.trim="username"
            type="text"
            placeholder="loverA / loverB"
            autocomplete="username"
          />
        </label>
        <label class="field">
          <span>密码</span>
          <input
            v-model="password"
            type="password"
            placeholder="只有你们两个人知道的小秘密"
            autocomplete="current-password"
          />
        </label>

        <p v-if="error" class="form-error">{{ error }}</p>

        <button type="submit" class="btn btn-primary btn-block">进来吧 💕</button>
      </form>

      <div class="quick-login">
        <p class="quick-title">或一键登录你的角色：</p>
        <div class="quick-buttons">
          <button type="button" class="btn btn-ghost btn-sky" @click="quickFill('A')">
            ♂ 小熊
            <small>（他的账号）</small>
          </button>
          <button type="button" class="btn btn-ghost btn-pink" @click="quickFill('B')">
            ♀ 小兔
            <small>（她的账号）</small>
          </button>
        </div>
      </div>

      <p class="privacy-note">
        🔒 所有内容仅保存在你的设备浏览器中。不上传、不追踪、安全私密。
      </p>
    </div>

    <ul class="float-decor">
      <li class="heart h1">♡</li>
      <li class="heart h2">✿</li>
      <li class="heart h3">☆</li>
      <li class="heart h4">♡</li>
      <li class="heart h5">✿</li>
    </ul>
  </div>
</template>

<style scoped>
.login-wrap {
  position: relative;
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px 16px;
  background:
    radial-gradient(circle at 10% 15%, rgba(255, 200, 221, 0.55), transparent 40%),
    radial-gradient(circle at 90% 85%, rgba(190, 220, 255, 0.6), transparent 45%),
    linear-gradient(160deg, #fff6f9 0%, #f5f2ff 60%, #eef5ff 100%);
  overflow: hidden;
}

.login-card {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 440px;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(8px);
  border-radius: 28px;
  padding: 28px 24px 22px;
  box-shadow:
    0 20px 45px rgba(255, 182, 193, 0.25),
    0 6px 14px rgba(180, 190, 255, 0.25),
    inset 0 0 0 1px rgba(255, 255, 255, 0.8);
}

.shake {
  animation: shake 0.5s ease;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-8px); }
  40% { transform: translateX(8px); }
  60% { transform: translateX(-6px); }
  80% { transform: translateX(6px); }
}

.login-hero {
  text-align: center;
  margin-bottom: 18px;
}

.login-title {
  margin: 12px 0 4px;
  font-size: 1.7rem;
  color: var(--cocoa);
  letter-spacing: 1px;
}

.login-sub {
  margin: 0;
  color: #9a8ca0;
  font-size: 0.92rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 16px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field span {
  font-size: 0.88rem;
  color: #7c6d84;
  padding-left: 4px;
}

.form-error {
  margin: 0;
  padding: 10px 12px;
  background: #fff0f4;
  border: 1.5px dashed #ffb6c1;
  border-radius: 14px;
  font-size: 0.88rem;
  color: #c45d7a;
}

.quick-login {
  margin-top: 18px;
  padding: 14px;
  background: linear-gradient(135deg, #fff0f6, #eef3ff);
  border-radius: 18px;
}

.quick-title {
  margin: 0 0 8px;
  font-size: 0.85rem;
  color: #8a7b90;
  text-align: center;
}

.quick-buttons {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.quick-buttons .btn small {
  display: block;
  font-weight: 400;
  color: #8a7b90;
  font-size: 0.75rem;
  margin-top: 2px;
}

.privacy-note {
  text-align: center;
  font-size: 0.78rem;
  color: #a494a8;
  margin: 14px 0 0;
  line-height: 1.6;
}

.float-decor {
  position: absolute;
  inset: 0;
  pointer-events: none;
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  z-index: 1;
}

.heart {
  position: absolute;
  font-size: 2rem;
  opacity: 0.35;
  animation: floaty 9s ease-in-out infinite;
  color: #ffb6c1;
}

.h1 { top: 8%; left: 6%; animation-delay: 0s; color: #ffb6c1; }
.h2 { top: 20%; right: 8%; animation-delay: 1.5s; color: #b6c9ff; font-size: 2.4rem; }
.h3 { bottom: 22%; left: 10%; animation-delay: 2.8s; color: #ffd59e; font-size: 2.2rem; }
.h4 { bottom: 10%; right: 12%; animation-delay: 4s; color: #c4a3ff; }
.h5 { top: 55%; left: 4%; animation-delay: 5.2s; color: #a6e3c9; font-size: 1.8rem; }

@keyframes floaty {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-12px) rotate(8deg); }
}

@media (max-width: 480px) {
  .login-card {
    padding: 22px 16px 18px;
    border-radius: 22px;
  }
  .login-title { font-size: 1.4rem; }
  .login-sub { font-size: 0.88rem; }
}
</style>
