<template>
  <div class="container mx-auto p-4">
    <div class="flex gap-4 mb-4">
      <input 
        type="text" 
        id="search" 
        v-model="searchQuery" 
        @keyup.enter="searchVideos" 
        placeholder="검색어를 입력하세요..." 
        class="flex-grow p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-300"
      />
      <button 
        @click="searchVideos" 
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        검색
      </button>
    </div>
    <div v-if="videos.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
      <div v-for="video in videos" :key="video.id.videoId" class="max-w-sm rounded overflow-hidden shadow-lg">
        <router-link :to="`/search/${video.id.videoId}`">
          <img :src="video.snippet.thumbnails.high.url" class="w-full" :alt="video.snippet.title">
          <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">{{ video.snippet.title }}</div>
          </div>
        </router-link>
      </div>
    </div>
    <div v-else>
      검색 결과가 없습니다.
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'

const route = useRoute();
const router = useRouter();

// 검색어를 저장할 반응형 참조
const searchQuery = ref('')

// 동영상 목록을 저장할 반응형 참조
const videos = ref([])

// YouTube Data API 키
const apiKey = import.meta.env.VITE_YOUTUBE_API_KEY

// 동영상을 검색하는 함수
const searchVideos = async () => {
  if (searchQuery.value) {
    router.push({ query: { q: searchQuery.value } }).catch(() => {});
    try {
      const response = await axios.get(`https://www.googleapis.com/youtube/v3/search`, {
        params: {
          part: 'snippet',
          maxResults: 10,
          q: searchQuery.value,
          key: apiKey
        }
      })
      videos.value = response.data.items
    } catch (error) {
      console.error('YouTube Data API에서 데이터를 가져오는 데 실패했습니다.', error)
    }
  }
}

onMounted(() => {
  if (route.query.q) {
    searchQuery.value = route.query.q;
    searchVideos();
  }
})
</script>