<template>
  <select
      :value="modelValue"
      @change="$emit('update:modelValue', $event.target.value)"
      class="px-4 py-2 border border-gray-300 focus:ring-slate-500 rounded-xl shadow-sm"
  >
    <option value="">UF</option>
    <option v-for="uf in ufs" :key="uf" :value="uf">{{ uf }}</option>
  </select>
</template>

<script setup>
const ufs = [
  'AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT',
  'MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO',
  'RR','SC','SP','SE','TO'
]

defineProps({ modelValue: String })
defineEmits(['update:modelValue'])
</script>
