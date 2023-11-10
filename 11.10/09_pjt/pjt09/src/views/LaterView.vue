<template>
  <div class="container mx-auto p-4">
    <h1 class="text-4xl font-bold text-blue-600 mb-8">
      나중에 볼 동영상 목록
    </h1>
    <div v-if="videoList.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
      <div v-for="video in videoList" :key="video.id" class="max-w-sm rounded overflow-hidden shadow-lg">
        <router-link :to="`/search/${video.id}`">
          <img :src="video.thumbnails.high.url" class="w-full" :alt="video.title">
          <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">{{ video.title }}</div>
          </div>
        </router-link>
      </div>
    </div>
    <div v-else class="text-lg text-gray-700 mb-6">
      저장된 동영상이 없습니다.
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const videoList = ref(JSON.parse(localStorage.getItem('later')) || [])
</script>
