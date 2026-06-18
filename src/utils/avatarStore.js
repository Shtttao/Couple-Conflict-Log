// ============================================================
// 情侣头像存储 — 支持用户上传自定义图片（纯本地、无服务器）
// - 图片以 data URL (base64) 保存在 localStorage
// - 未设置时回退到默认头像 /images/couple-boy.png 和 /images/couple-girl.png
// ============================================================

import { reactive, readonly } from 'vue'

const STORAGE_KEY = 'ccl_avatars'
const MAX_DIM = 512 // 输出图片最大边（保证存储不太大）
const MAX_FILE_SIZE = 5 * 1024 * 1024 // 5MB 上限

const DEFAULTS = {
  boy: '/images/couple-boy.png',
  girl: '/images/couple-girl.png'
}

function readStore () {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) return { boy: null, girl: null }
    const parsed = JSON.parse(raw)
    return {
      boy: typeof parsed?.boy === 'string' && parsed.boy.startsWith('data:') ? parsed.boy : null,
      girl: typeof parsed?.girl === 'string' && parsed.girl.startsWith('data:') ? parsed.girl : null
    }
  } catch {
    return { boy: null, girl: null }
  }
}

function writeStore (data) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data))
    return true
  } catch (e) {
    // 可能是 localStorage 容量不足
    alert('保存失败：浏览器存储空间不足。请尝试使用更小的图片 ♡')
    return false
  }
}

const state = reactive(readStore())

export function getAvatar (role) {
  if (role === 'boy') return state.boy || DEFAULTS.boy
  if (role === 'girl') return state.girl || DEFAULTS.girl
  return DEFAULTS.boy
}

export function hasCustom (role) {
  if (role === 'boy') return !!state.boy
  if (role === 'girl') return !!state.girl
  return false
}

export function resetAvatar (role) {
  if (role === 'boy') state.boy = null
  if (role === 'girl') state.girl = null
  writeStore({ boy: state.boy, girl: state.girl })
}

export function resetAll () {
  state.boy = null
  state.girl = null
  localStorage.removeItem(STORAGE_KEY)
}

// 读取 File -> 压缩为正方形 JPEG data URL
function compressImage (file) {
  return new Promise((resolve, reject) => {
    if (file.size > MAX_FILE_SIZE) {
      reject(new Error('图片太大啦，请用小于 5MB 的图片 ♡'))
      return
    }

    const reader = new FileReader()
    reader.onload = (e) => {
      const img = new Image()
      img.onload = () => {
        // 裁剪为正方形（中心裁切）
        const side = Math.min(img.width, img.height)
        const sx = (img.width - side) / 2
        const sy = (img.height - side) / 2

        const outSize = Math.min(side, MAX_DIM)
        const canvas = document.createElement('canvas')
        canvas.width = outSize
        canvas.height = outSize
        const ctx = canvas.getContext('2d')
        ctx.drawImage(img, sx, sy, side, side, 0, 0, outSize, outSize)

        const dataUrl = canvas.toDataURL('image/jpeg', 0.85)
        resolve(dataUrl)
      }
      img.onerror = () => reject(new Error('图片解析失败，换一张试试 ♡'))
      img.src = e.target?.result
    }
    reader.onerror = () => reject(new Error('读取图片失败 ♡'))
    reader.readAsDataURL(file)
  })
}

export async function setAvatarFromFile (role, file) {
  if (role !== 'boy' && role !== 'girl') {
    alert('角色不对哦 ♡')
    return false
  }
  try {
    const dataUrl = await compressImage(file)
    if (role === 'boy') state.boy = dataUrl
    if (role === 'girl') state.girl = dataUrl
    if (!writeStore({ boy: state.boy, girl: state.girl })) {
      // 写入失败，回滚
      const fresh = readStore()
      state.boy = fresh.boy
      state.girl = fresh.girl
      return false
    }
    return true
  } catch (err) {
    alert(err.message || '更换头像失败')
    return false
  }
}

export function useAvatarStore () {
  return {
    state: readonly(state),
    getAvatar,
    hasCustom,
    setAvatarFromFile,
    resetAvatar,
    resetAll
  }
}
