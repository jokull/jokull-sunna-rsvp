<script context="module">
  export const prerender = true;
  import { browser } from "$app/env";
  import { onMount } from "svelte";
</script>

<script>
  let responses = [];
  let guestCount = 0;
  let dietCounts = { pescatarian: 0, meat: 0, vegan: 0 };

  if (browser) {
    onMount(async () => {
      const url = `/api/responses`;
      const res = await fetch(url);

      responses = await res.json();
      responses.forEach((r) => {
        guestCount += r.guests.length;
        r.guests.forEach((g) => {
          dietCounts[g.diet] += 1;
        });
      });
    });
  }
</script>

<svelte:head>
  <title>Brúðkaupsgestir</title>
</svelte:head>

<div class="rounded-lg shadow-lg m-2 sm:m-4 p-4 sm:p-12 bg-white">
  {#if responses.length === 0}
    Loading
  {:else}
    <div class="">
      <div class="mx-auto max-w-xl">
        <div class="mb-6 flex items-center">
          <div class="mr-2">{guestCount} gestir:</div>
          <div
            class="inline-flex items-center p-1 px-2.5 mr-2 rounded-full text-xs font-medium bg-blue-100 text-blue-600"
          >
            {dietCounts.pescatarian} Fiskur
          </div>
          <div
            class="inline-flex items-center p-1 px-2.5 mr-2 rounded-full text-xs font-medium bg-red-100 text-red-600"
          >
            {dietCounts.meat} Kjöt
          </div>
          <div
            class="inline-flex items-center p-1 px-2.5 mr-2 rounded-full text-xs font-medium bg-green-100 text-green-600"
          >
            {dietCounts.vegan} Vegan
          </div>
        </div>
        {#each responses as response}
          <div class="border-b pb-4 mb-4">
            <div class="mb-2">
              {#each response.guests as guest}
                <div class="flex items-center">
                  <div
                    class={`inline-flex items-center p-1 rounded-full text-xs font-medium ${
                      guest.diet == "meat" && "bg-red-100 text-red-600"
                    } ${
                      guest.diet == "pescatarian" && "bg-blue-100 text-blue-600"
                    } ${
                      guest.diet == "vegan" && "bg-green-100 text-green-600"
                    }`}
                  >
                    <svg
                      class="h-2.5 w-2.5"
                      fill="currentColor"
                      viewBox="0 0 8 8"
                    >
                      <circle cx="4" cy="4" r="3" />
                    </svg>
                  </div>
                  <div class="font-semibold inline ml-1.5">{guest.name}</div>
                </div>
              {/each}
            </div>
            <div>
              <div class="flex items-center">
                <svg
                  class="flex-shrink-0 mr-1.5 h-5 w-5 text-gray-400"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                  aria-hidden="true"
                >
                  <path
                    d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"
                  />
                  <path
                    d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"
                  />
                </svg>
                <div class="text-sm text-gray-500">{response.email}</div>
              </div>
              {#if response.comment}
                <div
                  class="text-sm my-2 px-2 py-1.5 rounded-lg rounded-bl-none inline-block bg-gray-100"
                >
                  {response.comment}
                </div>
              {/if}
            </div>
          </div>
        {/each}
      </div>
    </div>
  {/if}
</div>
