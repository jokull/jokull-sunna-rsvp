<script context="module">
  export const prerender = true;
  import { browser } from "$app/env";
  import { onMount } from "svelte";
</script>

<script>
  import Response from "../components/Response.svelte";
  let responses = [];
  let guestCount = 0;
  let dietCounts = {};

  $: {
    guestCount = 0;
    dietCounts = { pescatarian: 0, meat: 0, vegan: 0 };
    responses
      .filter((r) => {
        return !r.deleted;
      })
      .forEach((r) => {
        guestCount += r.guests.length;
        r.guests.forEach((g) => {
          dietCounts[g.diet] += 1;
        });
      });
  }

  const toggleDeleted = async (response, visible) => {
    const res = await fetch(`/api/responses/${response.email}`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({ deleted: visible }),
    });
    if (!res.ok) {
      console.error(res);
    } else {
      const json = await res.json();
      responses = responses.map((r) => {
        if (r.email === response.email) {
          return json;
        }
        return r;
      });
    }
  };

  const getResponses = async () => {
    const url = `/api/responses`;
    const res = await fetch(url);
    return await res.json();
  };

  if (browser) {
    onMount(async () => {
      responses = await getResponses();
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
          <Response
            toggleDeleted={async (visible) => {
              await toggleDeleted(response, visible);
            }}
            {...response}
          />
        {/each}
      </div>
    </div>
  {/if}
</div>
