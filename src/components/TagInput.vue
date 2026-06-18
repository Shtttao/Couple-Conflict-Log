<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  modelValue: { type: Array, default: () => [] },
  placeholder: { type: String, default: 'Type tag and press Enter' }
})
const emit = defineEmits(['update:modelValue'])

const input = ref('')

const tags = ref([...(props.modelValue || [])])

watch(() => props.modelValue, (next) => {
  tags.value = [...(next || [])]
})

function addTag () {
  const t = input.value.trim().replace(/^#/, '')
  if (!t) return
  if (tags.value.includes(t)) {
    input.value = ''
    return
  }
  if (tags.value.length >= 8) return
  tags.value.push(t)
  input.value = ''
  sync()
}

function removeTag (t) {
  tags.value = tags.value.filter((x) => x !== t)
  sync()
}

function onKey (e) {
  if (e.key === 'Enter' || e.key === ',') {
    e.preventDefault()
    addTag()
  } else if (e.key === 'Backspace' && !input.value && tags.value.length) {
    tags.value.pop()
    sync()
  }
}

function sync () {
  emit('update:modelValue', [...tags.value])
}
</script>

<template>
  <div class="tag-input">
    <span v-for="tag in tags" :key="tag" class="chip">
      #{{ tag }}
      <button type="button" class="chip-remove" @click="removeTag(tag)">×</button>
    </span>
    <input
      ref="input"
      v-model="input"
      type="text"
      :placeholder="tags.length ? '' : placeholder"
      @keydown="onKey"
      @blur="addTag"
    />
  </div>
</template>

<style scoped>
.tag-input {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
  padding: 8px 10px;
  border-radius: 14px;
  border: 1.5px solid #f0dbe8;
  background: #fffafc;
  min-height: 42px;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.tag-input:focus-within {
  border-color: var(--pink-strong);
  box-shadow: 0 0 0 4px rgba(255, 182, 193, 0.25);
}

.tag-input input {
  flex: 1;
  min-width: 120px;
  border: none;
  background: transparent;
  outline: none;
  font-size: 0.95rem;
  padding: 4px;
  color: var(--cocoa);
}

.chip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 999px;
  background: linear-gradient(135deg, #fff0f6, #eef3ff);
  color: #8a7b90;
  font-size: 0.82rem;
}

.chip-remove {
  border: none;
  background: transparent;
  color: #c45d7a;
  cursor: pointer;
  font-size: 1rem;
  line-height: 1;
  padding: 0 2px;
}
</style>
