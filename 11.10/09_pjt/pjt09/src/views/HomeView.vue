<script setup>
</script>

<template>
  <div class="flex flex-col justify-center items-center bg-gray-100 h-[calc(100vh-56px)]">
    <h1 class="text-4xl font-bold text-blue-600 mb-8">
      동영상 검색 사이트
    </h1>
    <p class="text-lg text-gray-700 mb-6">
      원하는 동영상을 쉽고 빠르게 찾아보세요.
    </p>
    <router-link to="/search" class="text-white bg-blue-500 hover:bg-blue-600 font-bold py-3 px-6 rounded-lg shadow transition duration-300 ease-in-out">
      동영상 검색하기
    </router-link>
  </div>
</template>
