<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div>
    <nav class="bg-blue-500 p-4 text-white shadow-md">
      <ul class="flex space-x-4 justify-center">
        <li>
          <RouterLink to="/" class="hover:bg-blue-700 px-3 py-2 rounded transition duration-300 ease-in-out">
            Home
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/search" class="hover:bg-blue-700 px-3 py-2 rounded transition duration-300 ease-in-out">
            Search
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/later" class="hover:bg-blue-700 px-3 py-2 rounded transition duration-300 ease-in-out">
            Later
          </RouterLink>
        </li>
      </ul>
    </nav>

    <RouterView />
  </div>
</template>