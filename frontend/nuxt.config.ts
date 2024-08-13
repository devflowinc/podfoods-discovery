// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  css: ['~/assets/styles/main.css'],
  app: {
    head: {
      title: "Trieve Search Demo - Pod Foods",
      meta: [
        {
          charset: 'utf-8'
        }
      ],
      link: [
        {
          rel: 'stylesheet',
          href: 'https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css'
        },
        {
          rel: 'icon',
          type: 'image/x-icon',
          href: '/favicon.png'
        }
      ]
    }
  },
  serverHandlers: [
    { route: '/api/*', handler: '~/server/server.ts' }
  ]
})