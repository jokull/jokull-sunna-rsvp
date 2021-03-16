<script>
  let responses = [];
  import { onMount } from "svelte";

  onMount(async () => {
    const res = await fetch("/api/responses");
    responses = await res.json();
  });
</script>

<svelte:head>
  <title>Brúðkaupsgestir</title>
</svelte:head>

<div class="rounded-lg shadow-lg m-2 sm:m-4 p-4 sm:p-12 bg-white">
  {#if responses.length === 0}
    Loading
  {:else}
    <div
      class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-8 gap-y-4 sm:gap-y-12"
    >
      {#each responses as response}
        <div
          class="pb-4 sm:p-4 rounded border-b sm:border border-gray-200 flex flex-col"
        >
          <div class="mb-2 flex-grow">
            {#each response.guests as guest}
              <div class="flex">
                <div class="flex-grow font-semibold">{guest.name}</div>
                <div class="w-14 text-right">
                  {#if guest.diet === "pescatarian"}
                    Fiskur
                  {:else if guest.diet === "vegan"}
                    Vegan
                  {:else if guest.diet === "meat"}
                    Kjöt
                  {/if}
                </div>
              </div>
            {/each}
          </div>
          {#if response.comment}
            <div class="text-sm mb-2">{response.comment}</div>
          {/if}
          <div class="text-xs text-gray-400">{response.email}</div>
        </div>
      {/each}
    </div>
  {/if}
</div>
