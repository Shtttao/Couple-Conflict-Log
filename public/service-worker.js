/* ============================================================
 * Couple Conflict Log — Service Worker
 * 策略：
 *   1) 预缓存 App Shell（核心 HTML / JS / CSS / 图标）
 *   2) 运行时缓存：静态资源 stale-while-revalidate
 *   3) HTML 导航请求：网络优先，失败回退到缓存
 *   4) 所有数据存储在浏览器 IndexedDB（由主页面管理，SW不干预）
 * ============================================================ */

const CACHE_VERSION = 'ccl-v1.0.0'
const APP_SHELL_CACHE = `${CACHE_VERSION}-app-shell`
const RUNTIME_CACHE = `${CACHE_VERSION}-runtime`

// 预缓存列表：构建产物由 Vite 生成，路径模式固定
const APP_SHELL_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/favicon.png',
  '/icons/icon-48.png',
  '/icons/icon-72.png',
  '/icons/icon-96.png',
  '/icons/icon-144.png',
  '/icons/icon-192.png',
  '/icons/icon-256.png',
  '/icons/icon-384.png',
  '/icons/icon-512.png',
  '/icons/maskable-192.png',
  '/icons/maskable-512.png',
  '/images/couple-boy.png',
  '/images/couple-girl.png'
]

// ============================================================
// 安装阶段：预缓存 App Shell
// ============================================================
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(APP_SHELL_CACHE).then((cache) => {
      // cache.addAll 是原子操作：任何一个失败都会导致整个安装失败
      return cache.addAll(APP_SHELL_ASSETS).catch((err) => {
        console.warn('[SW] 部分 App Shell 资源无法缓存（可能正在开发模式）：', err)
        // 即便失败也要继续，用单个资源的方式重试
        return Promise.all(
          APP_SHELL_ASSETS.map((url) =>
            cache.add(url).catch(() => null)
          )
        )
      })
    }).then(() => {
      console.log('[SW] App Shell 缓存完成 ✓')
      // 立即接管页面
      return self.skipWaiting()
    })
  )
})

// ============================================================
// 激活阶段：清理旧版本缓存
// ============================================================
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name.startsWith('ccl-') && name !== APP_SHELL_CACHE && name !== RUNTIME_CACHE)
          .map((name) => {
            console.log('[SW] 清理旧缓存：', name)
            return caches.delete(name)
          })
      )
    }).then(() => {
      console.log('[SW] 激活完成，开始控制页面 ✓')
      return self.clients.claim()
    })
  )
})

// ============================================================
// 拦截请求：根据资源类型选择缓存策略
// ============================================================
self.addEventListener('fetch', (event) => {
  const request = event.request

  // 只处理 GET 请求（其他如 POST/PUT/DELETE 交给网络）
  if (request.method !== 'GET') return

  const url = new URL(request.url)

  // 1) 跨域资源（Google Fonts、CDN 等）：stale-while-revalidate
  if (url.origin !== location.origin) {
    event.respondWith(
      caches.open(RUNTIME_CACHE).then((cache) =>
        cache.match(request).then((cached) => {
          const networkFetch = fetch(request)
            .then((response) => {
              if (response && response.status === 200) {
                cache.put(request, response.clone())
              }
              return response
            })
            .catch(() => cached)
          return cached || networkFetch
        })
      )
    )
    return
  }

  // 2) HTML 导航请求：网络优先，失败回退缓存
  if (request.mode === 'navigate' || (request.headers.get('accept') || '').includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then((networkResponse) => {
          // 成功：更新缓存
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone()
            caches.open(APP_SHELL_CACHE).then((cache) => cache.put(request, clone))
          }
          return networkResponse
        })
        .catch(() => {
          // 离线：回退到缓存的 index.html（让 SPA 路由接管）
          return caches.match(request).then((cached) => {
            return cached || caches.match('/index.html')
          })
        })
    )
    return
  }

  // 3) 静态资源（JS / CSS / 图片 / JSON）：stale-while-revalidate
  const isStatic = url.pathname.match(/\.(js|css|png|jpg|jpeg|svg|gif|webp|ico|json|woff2?|ttf|otf)$/i)
  if (isStatic) {
    event.respondWith(
      caches.open(RUNTIME_CACHE).then((cache) =>
        cache.match(request).then((cached) => {
          const networkFetch = fetch(request)
            .then((response) => {
              if (response && response.status === 200) {
                cache.put(request, response.clone())
              }
              return response
            })
            .catch(() => cached)
          return cached || networkFetch
        })
      )
    )
    return
  }

  // 4) 其他请求：默认交给浏览器处理
})

// ============================================================
// 来自主页面的消息事件（例如：手动触发更新提示）
// ============================================================
self.addEventListener('message', (event) => {
  const { type } = event.data || {}
  if (type === 'SKIP_WAITING') {
    self.skipWaiting()
  } else if (type === 'CHECK_VERSION') {
    event.source.postMessage({ type: 'VERSION', version: CACHE_VERSION })
  } else if (type === 'CLEAR_CACHE') {
    caches.keys().then((keys) => {
      keys.forEach((k) => {
        if (k.startsWith('ccl-')) caches.delete(k)
      })
    })
  }
})

console.log('[SW] Service Worker 脚本已加载 ♡')
