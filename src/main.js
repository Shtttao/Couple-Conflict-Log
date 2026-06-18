import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import './styles/global.css'

// ============================================================
// PWA: 注册 Service Worker（仅在生产/HTTPS环境中生效）
// Service Worker 负责：
//   1) 预缓存 App Shell（HTML / JS / CSS / 图标 / 头像）
//   2) 离线状态下提供缓存内容
//   3) 静态资源 stale-while-revalidate 策略
// ============================================================
function registerServiceWorker () {
  if (!('serviceWorker' in navigator)) {
    console.log('[PWA] 此浏览器不支持 Service Worker')
    return
  }

  // HTTPS 或 localhost 才能注册 SW
  const isSecure = window.isSecureContext ||
    location.hostname === 'localhost' ||
    location.hostname === '127.0.0.1' ||
    location.protocol === 'file:'

  if (!isSecure) {
    console.log('[PWA] Service Worker 需要 HTTPS 或 localhost 环境')
    return
  }

  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/service-worker.js', { scope: '/' })
      .then((registration) => {
        console.log('[PWA] Service Worker 注册成功 ✓ 范围:', registration.scope)

        // 当发现新版本时提示更新（可选）
        registration.addEventListener('updatefound', () => {
          const newWorker = registration.installing
          if (newWorker) {
            newWorker.addEventListener('statechange', () => {
              if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                console.log('[PWA] 发现新版本，刷新页面即可启用 ♡')
              }
            })
          }
        })
      })
      .catch((error) => {
        console.error('[PWA] Service Worker 注册失败：', error)
      })
  })
}

// 离线状态提示
function setupOfflineIndicator () {
  if (!('onLine' in navigator)) return
  const updateStatus = () => {
    if (!navigator.onLine) {
      console.log('[PWA] 当前处于离线模式，数据仍保存在本地 ✓')
    } else {
      console.log('[PWA] 已恢复连接 ♡')
    }
  }
  window.addEventListener('online', updateStatus)
  window.addEventListener('offline', updateStatus)
  updateStatus()
}

// 启动应用
createApp(App).use(router).mount('#app')

// 注册 PWA 相关功能
registerServiceWorker()
setupOfflineIndicator()
