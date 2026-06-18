// ============================================================
// Auth store — two pre-set accounts only. No registration.
// Credentials live only in memory + sessionStorage on this device.
// ============================================================

import { reactive, readonly } from 'vue'

const PRESET_USERS = {
  loverA: {
    username: 'loverA',
    password: 'together4ever',
    displayName: 'Little Bear',
    role: 'me',
    color: 'sky'
  },
  loverB: {
    username: 'loverB',
    password: 'myheartforyou',
    displayName: 'Sweet Bunny',
    role: 'partner',
    color: 'pink'
  }
}

const STORAGE_KEY = 'ccl_auth'

function readSession () {
  try {
    const raw = sessionStorage.getItem(STORAGE_KEY)
    if (!raw) return null
    const parsed = JSON.parse(raw)
    return parsed?.role ? parsed : null
  } catch {
    return null
  }
}

const state = reactive({
  user: readSession()
})

export const usersMeta = PRESET_USERS

export function login (username, password) {
  const user = PRESET_USERS[username]
  if (!user || user.password !== password) {
    return { ok: false, message: 'Oops… wrong username or password. This log is only for two of you ♡' }
  }
  const profile = {
    username: user.username,
    displayName: user.displayName,
    role: user.role,
    color: user.color
  }
  state.user = profile
  sessionStorage.setItem(STORAGE_KEY, JSON.stringify(profile))
  return { ok: true, user: profile }
}

export function logout () {
  state.user = null
  sessionStorage.removeItem(STORAGE_KEY)
}

export function isLoggedIn () {
  return !!state.user
}

export function currentUser () {
  return state.user ? readonly(state.user) : null
}

export function useAuth () {
  return {
    state,
    login,
    logout,
    isLoggedIn,
    currentUser
  }
}
