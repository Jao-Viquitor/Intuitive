<template>
  <div class="space-y-6 backdrop-grayscale-100 m-6">
    <div class="flex gap-2">
      <input
          v-model="termo"
          @keydown.enter="buscar"
          placeholder="Buscar operadora..."
          class="flex-1 px-4 py-2 border border-gray-300 rounded-xl shadow-sm"
      />
      <button
          @click="buscar"
          class="px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-xl hover:bg-indigo-700 transition"
      >
        Buscar
      </button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div
          v-for="operadora in operadoras"
          :key="operadora.registro_ans"
          class="rounded-2xl border border-gray-200 p-4 shadow-sm bg-white transition hover:shadow-md"
      >
        <h2 class="text-lg font-semibold text-gray-900">
          {{ operadora.razao_social }}
        </h2>
        <p class="text-sm text-gray-600">
          Nome Fantasia: <span class="font-medium">{{ operadora.nome_fantasia }}</span>
        </p>
        <p class="text-sm text-gray-600">
          CNPJ: {{ operadora.cnpj }}
        </p>
        <p class="text-sm text-gray-600">
          Localização: {{ operadora.cidade }} - {{ operadora.uf }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const termo = ref('')
const operadoras = ref([])

const buscar = async () => {
  try {
    const { data } = await axios.get(`http://localhost:5000/api/busca_operadoras?q=${termo.value}`)
    operadoras.value = data
  } catch (e) {
    console.error('Erro ao buscar:', e)
  }
}
</script>
