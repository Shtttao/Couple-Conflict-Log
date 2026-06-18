<script setup>
import { ref, computed } from 'vue'
import TagInput from './TagInput.vue'
import MoodStars from './MoodStars.vue'

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
    alert('Please pick a date for this memory ♡')
    return
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
    <h3 class="form-title">✎ New Conflict Memory</h3>

    <div class="row row-top">
      <label class="field field-date">
        <span>Date</span>
        <input v-model="date" type="date" />
      </label>
      <div class="field field-tags">
        <span>Tags (e.g. Money, Family, Habits…)</span>
        <TagInput v-model="tags" placeholder="Type and press Enter…" />
      </div>
    </div>

    <div class="dual-col">
      <section class="panel panel-sky">
        <header class="panel-head">
          <span class="avatar">🐻</span>
          <h4>Little Bear</h4>
          <span v-if="!isMe" class="lock-tag">Locked for partner only</span>
        </header>
        <textarea
          v-model="myReflection"
          :disabled="!isMe"
          :placeholder="isMe ? 'Write down your feelings, what hurt you, what you wish…' : 'This side belongs to your partner — edit your own panel instead.'"
          rows="7"
        ></textarea>
        <div class="mood-row">
          <span class="mood-label">Mood after reflecting:</span>
          <MoodStars
            v-model="myMood"
            :read-only="!isMe"
            accent="sky"
          />
        </div>
      </section>

      <section class="panel panel-pink">
        <header class="panel-head">
          <span class="avatar">🐰</span>
          <h4>Sweet Bunny</h4>
          <span v-if="isMe" class="lock-tag">Locked for partner only</span>
        </header>
        <textarea
          v-model="partnerReflection"
          :disabled="isMe"
          :placeholder="!isMe ? 'Write down your feelings, what hurt you, what you wish…' : 'This side belongs to your partner — edit your own panel instead.'"
          rows="7"
        ></textarea>
        <div class="mood-row">
          <span class="mood-label">Mood after reflecting:</span>
          <MoodStars
            v-model="partnerMood"
            :read-only="isMe"
            accent="pink"
          />
        </div>
      </section>
    </div>

    <div class="actions">
      <button type="button" class="btn btn-ghost" @click="emit('cancel')">Cancel</button>
      <button type="submit" class="btn btn-primary">Save this memory ♡</button>
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
  font-size: 1.15rem;
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
  font-size: 0.85rem;
  color: #8a7b90;
  padding-left: 4px;
}

.field input,
.field textarea {
  padding: 11px 13px;
  border-radius: 14px;
  border: 1.5px solid #f0dbe8;
  background: #fffafc;
  font-size: 0.98rem;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
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
  padding: 16px;
  border-radius: 20px;
  box-shadow: 0 8px 20px rgba(180, 190, 255, 0.18);
}

.panel-sky {
  background: linear-gradient(135deg, #eaf3ff, #fdf7ff);
}

.panel-pink {
  background: linear-gradient(135deg, #ffeef5, #fff7f1);
}

.panel-head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.panel-head h4 {
  margin: 0;
  color: var(--cocoa);
}

.panel-head .avatar {
  font-size: 1.3rem;
  width: 36px;
  height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border-radius: 50%;
  box-shadow: 0 4px 10px rgba(180, 190, 255, 0.25);
}

.lock-tag {
  margin-left: auto;
  padding: 4px 10px;
  border-radius: 999px;
  background: #fff3b8;
  color: #8a6a24;
  font-size: 0.75rem;
}

.panel textarea {
  width: 100%;
  box-sizing: border-box;
  padding: 12px;
  border-radius: 14px;
  border: 1.5px solid transparent;
  background: rgba(255, 255, 255, 0.9);
  font-size: 0.95rem;
  line-height: 1.6;
  resize: vertical;
  outline: none;
  color: var(--cocoa);
  transition: border-color 0.2s;
}

.panel textarea:focus {
  border-color: #c9b8ff;
}

.panel textarea:disabled {
  color: #8a7b90;
  background: rgba(255, 255, 255, 0.6);
  cursor: not-allowed;
}

.mood-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 12px;
  flex-wrap: wrap;
}

.mood-label {
  font-size: 0.85rem;
  color: #7c6d84;
}

.actions {
  margin-top: 16px;
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

@media (max-width: 720px) {
  .row-top { grid-template-columns: 1fr; }
  .dual-col { grid-template-columns: 1fr; }
  .actions { justify-content: stretch; }
  .actions .btn { flex: 1; }
}
</style>
