<template>
  <div class="flex flex-col min-h-screen bg-white">
    <Header />

    <main class="flex flex-col md:flex-row flex-1 items-center justify-between gap-6 px-6 py-12 md:px-48">
      <div class="max-w-xl">
        <h2 class="text-xs font-semibold text-gray-600 tracking-wide uppercase">
          OPERADORAS DE SAÚDE ANS
        </h2>
        <h1 class="mt-2 text-3xl md:text-2xl font-bold text-gray-900 leading-snug motion-safe:animate-fadeInUp fade-in">
          Dados inteligentes e acessíveis <br>
          sobre operadoras de planos de saúde <br>
          baseado em fontes oficiais da ANS
        </h1>
      </div>

      <img
          src="../assets/mushroom.webp"
          alt="Cogumelo"
          class="w-full max-w-lg rounded-2xl shadow-md"
      />
    </main>

    <Footer />
  </div>
</template>

<script setup>
import Header from '@/components/layout/Header.vue'
import Footer from '@/components/layout/Footer.vue'
</script>

<style scoped>
main img {
  object-fit: cover;
}
</style>
