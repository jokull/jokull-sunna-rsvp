<script>
  let responses = [];
  import { onMount } from "svelte";

  onMount(async () => {
    const res = await fetch("/api/responses");
    responses = await res.json();
  });
</script>

<div class="rounded-lg shadow-lg m-8 p-12 bg-white">
  {#if responses.length === 0}
    Loading
  {:else}
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-4 gap-y-8"
    >
      {#each responses as response}
        <div>
          <div class="font-bold font-lg">{response.email}</div>
          <div class="font-light text-sm mb-2">S: {response.phone}</div>
          {#each response.guests as guest}
            <div>
              <div>
                {#if guest.diet === "pescatarian"}
                  🐟
                {:else if guest.diet === "vegan"}
                  🥬
                {:else if guest.diet === "meat"}
                  🥩
                {/if}
                {guest.name}
              </div>
            </div>
          {/each}
        </div>
      {/each}
    </div>
  {/if}
</div>
