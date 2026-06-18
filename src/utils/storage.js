// ============================================================
// Couple Conflict Log — IndexedDB Storage Layer
// All data lives only in the user's local browser.
// ============================================================

const DB_NAME = 'CoupleConflictLog'
const DB_VERSION = 1
const STORE_CONFLICTS = 'conflicts'

function openDB () {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, DB_VERSION)
    request.onupgradeneeded = (event) => {
      const db = event.target.result
      if (!db.objectStoreNames.contains(STORE_CONFLICTS)) {
        const store = db.createObjectStore(STORE_CONFLICTS, {
          keyPath: 'id',
          autoIncrement: true
        })
        store.createIndex('date', 'date', { unique: false })
        store.createIndex('resolved', 'resolved', { unique: false })
      }
    }
    request.onsuccess = () => resolve(request.result)
    request.onerror = () => reject(request.error)
  })
}

function uid () {
  return 'c_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2, 8)
}

export async function addConflict (conflict) {
  const db = await openDB()
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_CONFLICTS, 'readwrite')
    const store = tx.objectStore(STORE_CONFLICTS)
    const record = {
      id: uid(),
      date: conflict.date || new Date().toISOString().slice(0, 10),
      tags: conflict.tags || [],
      myReflection: conflict.myReflection || '',
      partnerReflection: conflict.partnerReflection || '',
      myMood: conflict.myMood || 0,
      partnerMood: conflict.partnerMood || 0,
      resolved: false,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    }
    const request = store.add(record)
    request.onsuccess = () => resolve(record)
    request.onerror = () => reject(request.error)
  })
}

export async function updateConflict (conflict) {
  const db = await openDB()
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_CONFLICTS, 'readwrite')
    const store = tx.objectStore(STORE_CONFLICTS)
    const record = { ...conflict, updatedAt: new Date().toISOString() }
    const request = store.put(record)
    request.onsuccess = () => resolve(record)
    request.onerror = () => reject(request.error)
  })
}

export async function deleteConflict (id) {
  const db = await openDB()
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_CONFLICTS, 'readwrite')
    const store = tx.objectStore(STORE_CONFLICTS)
    const request = store.delete(id)
    request.onsuccess = () => resolve(true)
    request.onerror = () => reject(request.error)
  })
}

export async function getAllConflicts () {
  const db = await openDB()
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_CONFLICTS, 'readonly')
    const store = tx.objectStore(STORE_CONFLICTS)
    const request = store.getAll()
    request.onsuccess = () => {
      const list = request.result || []
      list.sort((a, b) => (b.date || '').localeCompare(a.date || ''))
      resolve(list)
    }
    request.onerror = () => reject(request.error)
  })
}

export async function wipeAllData () {
  const db = await openDB()
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_CONFLICTS, 'readwrite')
    const store = tx.objectStore(STORE_CONFLICTS)
    const request = store.clear()
    request.onsuccess = () => resolve(true)
    request.onerror = () => reject(request.error)
  })
}
