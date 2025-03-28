<template>
  <div class="rounded-2xl border border-gray-200 p-4 shadow-sm bg-white transition hover:shadow-md">
    <div class="flex justify-between items-start">
      <h2 class="text-lg font-semibold text-slate-900">
        {{ operadora.razao_social }}
      </h2>
      <span class="text-xs text-slate-600">#{{ operadora.registro_ans }}</span>
    </div>

    <div class="mt-2 space-y-1 text-sm text-slate-800">
      <p><strong>Nome Fantasia: </strong> {{ operadora.nome_fantasia }}</p>
      <p><strong>CNPJ: </strong> {{ operadora.cnpj }}</p>
      <p v-if="operadora.cidade && operadora.uf">
        <strong>Localização:</strong> {{ operadora.cidade }} - {{ operadora.uf }}
      </p>
      <p v-if="mostrarDespesas && operadora.total_despesa">
        <strong>Total de Despesas: </strong>
        <span class="text-emerald-800 font-semibold">
          {{ formatarValor(operadora.total_despesa) }}
        </span>
      </p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  operadora: {
    type: Object,
    required: true
  },
  mostrarDespesas: {
    type: Boolean,
    default: false
  }
})

const formatarValor = (valor) => {
  return Number(valor).toLocaleString('pt-BR', {
    style: 'currency',
    currency: 'BRL',
  })
}
</script>
