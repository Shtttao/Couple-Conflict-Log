<script setup>
import { ref, computed } from 'vue'
import TagInput from './TagInput.vue'
import MoodStars from './MoodStars.vue'
import { useAvatarStore } from '../utils/avatarStore.js'

const avatarStore = useAvatarStore()
const boyAvatar = computed(() => avatarStore.getAvatar('boy'))
const girlAvatar = computed(() => avatarStore.getAvatar('girl'))

const props = defineProps({
  user: { type: Object, required: true }
})
const emit = defineEmits(['created', 'cancel'])

const date = ref(new Date().toISOString().slice(0, 10))
const tags = ref([])
const myReflection = ref('')
const partnerReflection = ref('')
const myMood = ref(0)
const partnerMood = ref(0)

const isMe = computed(() => props.user?.role === 'me')

function submit () {
  if (!date.value) {
    alert('请选择日期 ♡')
    return
  }
  if (isMe && !myReflection.value.trim()) {
    if (!window.confirm('你这一侧的反思是空的，确定保存吗？')) return
  }
  if (!isMe && !partnerReflection.value.trim()) {
    if (!window.confirm('你这一侧的反思是空的，确定保存吗？')) return
  }
  emit('created', {
    date: date.value,
    tags: [...tags.value],
    myReflection: myReflection.value.trim(),
    partnerReflection: partnerReflection.value.trim(),
    myMood: myMood.value,
    partnerMood: partnerMood.value
  })
}
</script>

<template>
  <form class="conflict-form" @submit.prevent="submit">
    <h3 class="form-title">✎ 新的吵架回忆</h3>

    <div class="row row-top">
      <label class="field field-date">
        <span>日期</span>
        <input v-model="date" type="date" />
      </label>
      <div class="field field-tags">
        <span>标签（例如：金钱 / 家人 / 习惯…）</span>
        <TagInput v-model="tags" placeholder="输入后按回车…" />
      </div>
    </div>

    <div class="dual-col">
      <section class="panel panel-sky">
        <header class="panel-head">
          <span class="avatar-img bear">
            <img :src="boyAvatar" alt="小熊" />
          </span>
          <h4>小熊</h4>
          <span v-if="!isMe" class="lock-tag">🔒 对方区域</span>
        </header>
        <textarea
          v-model="myReflection"
          :disabled="!isMe"
          :placeholder="isMe ? '写下你的感受、哪里被刺到了、你希望什么…' : '这一侧属于小熊，去写你自己那一栏就好。'"
          rows="7"
        ></textarea>
        <div class="mood-row">
          <span class="mood-label">反思后的心情：</span>
          <MoodStars
            v-model="myMood"
            :read-only="!isMe"
            accent="sky"
          />
        </div>
      </section>

      <section class="panel panel-pink">
        <header class="panel-head">
          <span class="avatar-img bunny">
            <img :src="girlAvatar" alt="小兔" />
          </span>
          <h4>小兔</h4>
          <span v-if="isMe" class="lock-tag">🔒 对方区域</span>
        </header>
        <textarea
          v-model="partnerReflection"
          :disabled="isMe"
          :placeholder="!isMe ? '写下你的感受、哪里被刺到了、你希望什么…' : '这一侧属于小兔，去写你自己那一栏就好。'"
          rows="7"
        ></textarea>
        <div class="mood-row">
          <span class="mood-label">反思后的心情：</span>
          <MoodStars
            v-model="partnerMood"
            :read-only="isMe"
            accent="pink"
          />
        </div>
      </section>
    </div>

    <div class="actions">
      <button type="button" class="btn btn-ghost" @click="emit('cancel')">取消</button>
      <button type="submit" class="btn btn-primary">保存这条回忆 ♡</button>
    </div>
  </form>
</template>

<style scoped>
.conflict-form {
  background: rgba(255, 255, 255, 0.92);
  border-radius: 24px;
  padding: 22px 20px 20px;
  box-shadow: 0 18px 40px rgba(255, 182, 193, 0.2);
  margin-bottom: 18px;
}

.form-title {
  margin: 0 0 14px;
  color: var(--cocoa);
  font-size: 1.2rem;
}

.row-top {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 14px;
  margin-bottom: 14px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field span {
  font-size: 0.88rem;
  color: #8a7b90;
  padding-left: 4px;
}

.field input,
.field textarea {
  font-family: inherit;
  padding: 11px 13px;
  border-radius: 14px;
  border: 1.5px solid #f0dbe8;
  background: #fffafc;
  font-size: 0.98rem;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
  -webkit-appearance: none;
  appearance: none;
}

.field input:focus {
  border-color: var(--pink-strong);
  box-shadow: 0 0 0 4px rgba(255, 182, 193, 0.25);
}

.dual-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.panel {
  padding: 18px;
  border-radius: 20px;
  box-shadow: 0 8px 20px rgba(180, 190, 255, 0.2);
}

.panel-sky {
  background: linear-gradient(135deg, #eaf3ff, #fdf7ff);
  border-top: 3px solid #a8cce8;
}

.panel-pink {
  background: linear-gradient(135deg, #ffeef5, #fff7f1);
  border-top: 3px solid #ffb6c1;
}

.panel-head {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.panel-head h4 {
  margin: 0;
  color: var(--cocoa);
  font-size: 1.05rem;
}

.avatar-img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  box-shadow: 0 4px 10px rgba(180, 190, 255, 0.3);
  background: #fff;
}

.avatar-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.avatar-img.bear {
  box-shadow: 0 4px 10px rgba(168, 204, 232, 0.45), inset 0 0 0 2px rgba(168, 204, 232, 0.7);
}

.avatar-img.bunny {
  box-shadow: 0 4px 10px rgba(255, 182, 193, 0.45), inset 0 0 0 2px rgba(255, 182, 193, 0.7);
}

.lock-tag {
  margin-left: auto;
  padding: 5px 12px;
  border-radius: 999px;
  background: #fff3b8;
  color: #8a6a24;
  font-size: 0.76rem;
}

.panel textarea {
  font-family: inherit;
  width: 100%;
  box-sizing: border-box;
  padding: 12px 14px;
  border-radius: 14px;
  border: 1.5px solid transparent;
  background: rgba(255, 255, 255, 0.9);
  font-size: 0.95rem;
  line-height: 1.7;
  resize: vertical;
  outline: none;
  color: var(--cocoa);
  transition: border-color 0.2s;
  min-height: 120px;
}

.panel textarea:focus {
  border-color: #c9b8ff;
}

.panel textarea:disabled {
  color: #b8a8b8;
  background: rgba(255, 255, 255, 0.5);
  cursor: not-allowed;
}

.mood-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 14px;
  flex-wrap: wrap;
}

.mood-label {
  font-size: 0.88rem;
  color: #7c6d84;
}

.actions {
  margin-top: 18px;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

@media (max-width: 720px) {
  .row-top { grid-template-columns: 1fr; }
  .dual-col { grid-template-columns: 1fr; }
  .actions { justify-content: stretch; }
  .actions .btn { flex: 1; min-height: 44px; }
}
</style>
