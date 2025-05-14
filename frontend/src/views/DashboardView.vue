<script setup lang="ts">
// Inbox view component
import { useSampleHook } from "@/hooks/useSampleHook";
import { onMounted, ref } from "vue";

const { useSample } = useSampleHook();
const sampleData = ref(null);

onMounted(async () => {
  const data = await useSample();
  sampleData.value = data;
});
</script>

<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Dashboard</h1>
    <p>This is your dashboard page.</p>
    <p>{{ sampleData }}</p>
  </div>
</template>

<style scoped></style>

